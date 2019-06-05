#!/usr/bin/env python
# coding: utf-8

from pycparser import parse_file, c_ast
from numpy import inf

class Condition:
    def __init__(self, condition):
        self.condition = condition
        (self.left_operand, self.operator,
         self.right_operand) = self.handleCondition()

    def handleCondition(self):
        left_operand = self.condition.left
        right_operand = self.condition.right
        operator = self.condition.op

        if operator == ">":
            return (right_operand, "<", left_operand)
        elif operator == ">=":
            return (right_operand, "<=", left_operand)
        else:
            return (left_operand, operator, right_operand)


class Context:
    def __init__(self, condition=None, bool_condition=True, next_nodes=[],                 previous_context=None):
        if previous_context is not None:
            self.conditions = previous_context.conditions.append(
                (condition, bool_condition))
            self.variables = previous_context.variables
            self.nexts = previous_context.nexts + next_nodes
            self.checkCondition()
        else:
            self.conditions = [(condition, bool_condition)]
            self.variables = {}
            self.nexts = next_nodes

    def addParam(self, param):
        name = param.name
        types = param.type.type.names
        if 'int' not in types:
            raise 'Only int type allowed'
        # if 'unsigned' in types:
        if 'unsigned' in types:
            self.variables[name] = Variable(
                name, [Interval(Value(constante=0), Value(constante=inf))])
        else:
            self.variables[name] = Variable(
                name, [Interval(Value(constante=-inf), Value(constante=inf))])

    def addVariable(self, node_decl):
        name = node_decl.name
        types = node_decl.type.type.names
        if 'int' not in types:
            raise 'Only int type allowed'
        if node_decl.init is not None:
            if type(node_decl.init) is c_ast.Constant:
                singleton = Singleton(
                    Value(constante=int(node_decl.init.value)))
                variable = Variable(name, singletons=[singleton])
            elif type(node_decl.init) is c_ast.ID:
                singleton = Singleton(Value(variables=[node_decl.init.name]))
                variable = Variable(name, singletons=[singleton])
            elif type(node_decl.init) is c_ast.BinaryOp:
                left, right, op = node_decl.init.left, node_decl.init.right, node_decl.init.op
                if type(left) is c_ast.ID and type(right) is c_ast.ID:
                    variable = Operation(
                        self.variables[left.name], op, self.variables[right.name]).compute()
                    variable.name = name
                elif type(left) is c_ast.Constant and type(right) is c_ast.ID:
                    singleton = Singleton(Value(int(left.value)))
                    variable = Operation(
                        Variable(singletons=[singleton]), op, self.variables[right.name]).compute()
                    variable.name = name
                elif type(left) is c_ast.ID and type(right) is c_ast.Constant:
                    singleton = Singleton(Value(int(right.value)))
                    print(singleton)
                    print(Variable(singletons=[singleton]))
                    variable = Operation(self.variables[left.name], op, Variable(
                        singletons=[singleton])).compute()
                    variable.name = name
                else:
                    if op is "+":
                        singleton = [
                            Singleton(Value(constante=(int(left.value) + int(right.value))))]
                        variable = Variable(name=name, singletons=[singleton])
                    elif op is "-":
                        singleton = [
                            Singleton(Value(constante=(int(left.value) - int(right.value))))]
                        variable = Variable(name=name, singletons=[singleton])
        else:
            variable = Variable(name=name)
        self.variables[name] = variable

    def pop(self):
        if self.nexts != []:
            return self.nexts.pop(0)
        return None

    def checkCondition(self):
        """
        Si self.state = True condition possible
        Si self.state = False condition impossible donc le branchement est inutile
        """

        # simplification des deux listes représentant les variables
        # propagation des singletons grâce à leur valeur trouvée dans la bibliothèque
        # si il y a encore des variables entièrement non définies de chaque côté ->
        # deux contexte et pas d'update
        # si non définie d'un seul côté -> on a les deux contextes et update de la valeur
        # de la variable
        # sinon -> un seul contexte et pas d'update
        self.state = True
        return

class Singleton():
    """
        Représente un singleton

        Attributs
        ----------
        value: @Value
            valeur du singleton
    """

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return "{" + str(self.value) + "}"

class Interval():
    """
        Représente un interval

        Attributs
        ----------
        min: @Value
            Minimum de l'intervalle
        max: @Value 
            Maximum de l'intervalle
    """

    def __init__(self, minimum, maximum):
        self.min = minimum
        self.max = maximum

    def __str__(self):
        return "[" + str(self.min) + "," + str(self.max) + "]"

class Variable():
    """
        Représente une variable

        Attributs
        ----------
        name: String 
            Nom de la varialbe
        intervals: list[@Interval] 
            Ensemble d'intervalles pour la variable
        singletons: list[@Singletons] 
            Ensemble de singletons pour la variable
    """

    def __init__(self, name="", intervals=[], singletons=[]):
        self.name = name
        self.intervals = intervals
        self.singletons = singletons

    def __str__(self):
        return self.name + " : " + ''.join((str(interval) + ' ') for interval in self.intervals) + ''.join(str(singleton) + ' ' for singleton in self.singletons)

class Value():
    """
        Représente une valeur de variable qui est sous la forme: @Variable + Constante

        Attributs
        ----------
        constante: Int
            Constante
        variables: list[@Variable, String]
            Variables et opérateurs
    """

    def __init__(self, constante=0, variable=None):
        self.variable = variable
        self.constante = constante

    def __str__(self):
        if self.variable is None:
            return str(self.constante)
        return self.variable.name + ' + ' + str(self.constante)


class Operation():
    def __init__(self, left, operator, right):
        self.left = left
        self.operator = operator
        self.right = right

    def computeValue(self, left, operator, right):
        value_computed = Value()

        if left.variable is None:
            value_computed.variable = right.variable
        else:
            if right.variable is not None:
                raise "Addition de deux valeurs dépendantes de deux variables"
            value_computed.variable = left.variable

        if(operator == "+"):
            value_computed.constante = left.constante + right.constante
        elif(operator == "-"):
            value_computed.constante = left.constante - right.constante

        return value_computed

    def compute(self):
        variable_computed = Variable()
        for left in self.left.intervals:
            for right in self.right.intervals:
                variable_computed.intervals.append(Interval(self.computeValue(left.min, self.operator, right.min), self.computeValue(left.max, self.operator, right.max)))
            for right in self.right.singletons:
                variable_computed.intervals.append(Interval(self.computeValue(left.min, self.operator, right.value), self.computeValue(left.max, self.operator, right.value)))
        for left in self.left.singletons:
            for right in right.intervals:
                variable_computed.intervals.append(Interval(self.computeValue(left.value, self.operator, right.min), self.computeValue(left.value, self.operator, right.max)))
            for right in self.right.singletons:
                variable_computed.singletons.append(Singleton(self.computeValue(left.value, self.operator, right.value)))
        return variable_computed

def parse_c_file(file):
    ast = parse_file(file, use_cpp=True,
                     cpp_path='gcc',
                     cpp_args=['-E', r'-Iutils/fake_libc_include'])
    return ast

def isIf(node):
    return type(node) == c_ast.If


def getCoord(node):
    return node.coord

def isDeclaration(node):
    return type(node) == c_ast.Decl

def isAssignment(node):
    return type(node) == c_ast.Assignment

def visitParamsFunction(context, params):
    for param in params:
        context.addParam(param)

def visitNode(context):
    node = context.pop()
    if node is not None:
        if isIf(node):
            condition = Condition(node.cond)
            context1 = Context(condition=condition, bool_condition=True,
                               next_nodes=[node.iftrue], previous_context=context)
            context2 = Context(condition=condition, bool_condition=False,
                               next_nodes=[node.iffalse], previous_context=context)
            if context1.state and context2.state:
                return visitNode(context1) + visitNode(context2)
            elif context1.state and not context2.state:
                return visitNode(context1) + [context2]
            elif not context1.state and context2.state:
                return visitNode(context2) + [context1]
            else:
                return [context1, context2]
        elif isDeclaration(node):
            context.addVariable(node)
        elif isAssignment(node):
            context.assign(node)
        else:
            for (string, child) in node.children():
                context.nexts.append(child)
        return visitNode(context)
    return []

def visitFunction(function):
    context = Context(next_nodes=[function.body])
    visitParamsFunction(context, function.decl.type.args.params)
    return visitNode(context)


ast_graph = parse_c_file('/home/julien/Dev/Cassiopee-Control-Flow-Graph/Optimizer Script/C files/if.c')
foo_graph = ast_graph.ext[0]

contexts = visitFunction(foo_graph)
context1, context2 = contexts[0], contexts[1]

print(context1.variables)