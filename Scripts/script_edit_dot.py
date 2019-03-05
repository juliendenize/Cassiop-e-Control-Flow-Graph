"""
script_edit_dot.py
"""

import re
import sys
import pydot
from pydot import Edge
from pydot import Node

SUBGRAPHS = {}
PARENTS = {}



###
# Key functions
###

# Import a graph from dot and return the pydot graph

def graph_from_dot(dot_file):
    """
       Import a graph from dot and return the pydot graph
       
       :param dot_file: path to the file to import
       :return: pydot graph
       :rtype: Dot
    """
    (graph, ) = pydot.graph_from_dot_file(str(dot_file))
    return graph


# Extract subgraphs, edges, nodes

def extract_subgraphs(subgraph_list):
    global SUBGRAPHS, PARENTS
    """
       Extract subgraphs recursively from a list of subgraphs, and the hierarchy of the subgraphs
       
       :param graph: graph or subgraph from which subgraphs are to be extracted
       :return: List of subgraphs
       :rtype: List
    """
    new_subgraphs = []
    for subgraph in subgraph_list:
        subgraph.set_name(subgraph.get_name().strip("\"").replace("cluster_", ""))
        SUBGRAPHS[subgraph.get_name()] = subgraph
        children_subgraphs = subgraph.get_subgraph_list() 
        new_subgraphs += children_subgraphs
        for child in children_subgraphs:
            PARENTS[child.get_name().strip("\"").replace("cluster_", "")] = subgraph
    if(new_subgraphs == []):
        return
    else:
        return extract_subgraphs(new_subgraphs)


def extract_nodes(graph):
    """
       Extract nodes from a graph or subgraph
       
       :param graph: graph or subgraph from which nodes are to be extracted
       :return: List of nodes
       :rtype: List
    """
    return graph.get_nodes()


def extract_edges(graph):
    """
       Extract edges from a graph or subgraph
       
       :param graph: graph or subgraph from which edges are to be extracted
       :return: List of edges
       :rtype: List
    """
    return graph.get_edges()


# Add an edge, a node

def add_edge(graph, tail_node, head_node, label="[0%]", style="solid, bold", color="black", constraint="true"):
    """
       Add an edge to a graph or subgraph
       
       :param graph: graph or subgraph to which the edge is added
       :param tail_node: origin of the edge
       :param head_node: destination of the edge
       :param label: the label
       :param style: the style
       :param color: the color
       :param constraint: the constraint
    """
    edge = Edge(tail_node, head_node, label=label, style=style, color=color, constraint="true")
    graph.add_edge(edge)
    return


def add_node(graph, node_name, label, shape='record', style='filled', fillcolor='lightgrey'):
    """
       Add a node to a graph or subgraph
       
       :param graph: graph or subgraph to which the node is added
       :param node_name: name of the node
       :param label: label of the node
       :param shape: shape of the node (default "record")
       :param style: style of the node (default "field")
       :param fillcolor: color of the node (default "lightgrey")
       :return: the node created
       :rtype: Node
    """
    node = Node(name=node_name, shape=shape, style=style, fillcolor=fillcolor, label=label)
    graph.add_node(node)
    return node


###
# Create the new node
###

# Analyse and create labels if a function call is found¶

def analyse_label_function_calls(node):
    """
        Find if it exists, the first call to a function in a node
        
        :param node: the node examined
        :return: tuple containing the name of the function, the function call and its position in the label of the 
                 node
        :rtype: tuple
    """
    global SUBGRAPHS
    regex = r"(?:\|_\w+\\ \=\\ |\|)\w+\\\s\(\w*\)"
    label = node.get_attributes()['label']
    for match in re.finditer(regex, label, re.MULTILINE):
        function_call = re.search(r'\w+\\\s\(\w*\)', match.group()).group()
        function_name = re.search(r'\w+', function_call)
        if function_name is not None:
            if function_name.group() in SUBGRAPHS:
                return (function_name.group(), function_call, match.start())
    return (None, None, None)


def create_labels(node, function_call, function_call_line):
    """
        Create the labels for the new node, and for the node cut in half.
        
        :param node: the node cut
        :param function_call: the string containing the function call used as a regex expression
        :param function_call_line: the line where the function call is made
        :return: tuple containing the new label for the node cut, the label for the new node, and the value of
                 the cut node's bb
        :rtype: tuple
    """
    
    label_node = node.get_attributes()["label"]
    label_node_from_function_line = label_node[function_call_line:]
    regex = re.escape(function_call) + r';\\l\\\n'
    match_function = re.search(regex, label_node_from_function_line, re.S)
    
    bb = int(re.search(r'\d+', re.search(r'<bb\\\ \d+\\>', label_node).group()).group())
    
    label_node1 = label_node[0:function_call_line] + '|call\ ' + function_call + ';\l\\\n}"'
    
    match_variable = re.search(r'\w+\\ =\\ ' + re.escape(function_call), label_node_from_function_line)

    label_node2 = '"{ FREQ:0 |\<bb\ ' + str(bb) + '\>:\l\\\n|'
    
    if match_variable is not None:
        variable = re.search(r'\w+', match_variable.group()).group()
        label_node2 += variable + '\ =\ '
    label_node2 += 'return\ ' + function_call + ';\\l\\\n' + label_node_from_function_line[match_function.end():]
    
    return (label_node1, label_node2, int(bb))


# Update the value of the nodes: name and labels

def update_node(node, attribute, value):
    """
        Update the node's attribute value.
        
        :param node: the node updated
        :param attribute: the attribute
        :param value: the value
    """
    node.set(attribute, value)
    return


def update_bb_string(string, bb):
    """ 
        update recursivly the values of the bb found in the string. The first string is a node label
        
        :param string: the string
        :param bb: the bb
        :return: the new string
        :rtype: string
    """
    match = re.search(r'<bb\\\ \d+\\>', string)
    
    if match == None:
        return string
    match_bb = int(re.search(r'\d+', match.group()).group())
    
    if match_bb > bb:
        string = string.replace('<bb\ ' + str(match_bb), '<bb\ ' + str(match_bb + 1))
    return string[0:match.end()] + update_bb_string(string[match.end():], bb)


def update_node_name(node_name, bb):
    """
        Update the node_name if its bb is superior to the bb given
        
        :param node_name: the name to update
        :param bb: the bb threshold
        :return: the node_name (updated)
        :rtype: String
    """
    node_number = int(re.search(r'\d+', re.search(r'block_\d+', node_name).group()).group())
    if bb < node_number:
        return node_name.replace('block_' + str(node_number), 'block_' + str(node_number+1))
    return node_name


def update_nodes(nodes, bb):
    """
        Updates all the nodes whose bb are greater or equal to the bb given.
        
        :param nodes: the nodes to update
        :param bb: the bb
    """
    
    for node in nodes:
        node.set("label", update_bb_string(node.get_attributes()["label"], bb))
        node.set_name(update_node_name(node.get_name(), bb))


# On veut récupérer les noeuds qui pourront être update ce qui veut dire qu'il faut itérer dans les sous-graphes enfants et parents

def get_nodes_to_update(subgraph, graph_name, starter=0):
    """
        Retrive all the nodes to update from the parents to the children.
        
        :param subgraph: the current subgraph
        :param graph_name: the name of the global graph
        :param starter: the flag, 0 if you are the subgraph starter, 1 else
        :return: the nodes to update
        :rtype: list
    """
    global SUBGRAPHS, PARENTS
    
    nodes = extract_nodes(subgraph)
    
    for child_subgraph in subgraph.get_subgraph_list():
        nodes += get_nodes_to_update(child_subgraph, graph_name, 1)
    
    parent = PARENTS[subgraph.get_name()].get_name()
    while(parent != graph_name and starter == 0):
        nodes += extract_nodes(PARENTS[subgraph.get_name()])
        parent = PARENTS[parent].get_name()
    return nodes


# Create the new node

def create_new_node(subgraph, prev_node, label, bb):
    """
        Create a new node
        
        :param subgraph: the subgraph where lives the new node
        :param prev_node: the node that necessits a child
        :param label: the label of the new node
        :param bb: the bb of the previous node
        :return: the new node
        :rtype: Node
    """
    return add_node(subgraph, update_node_name(prev_node.get_name(), bb-1), label=update_bb_string(label, bb-1))


###
# Create the edges
###

def get_top_parent(subgraph, graph_name):
    """
        Get the top parent in the arborescence of the graph after the root (graph_name)
        
        :param subgraph: the subgraph to find the parent
        :param graph_name: the root of the arborescence
        :return: The top parent of the subgraph
        :rtype: Subgraph
    """
    global PARENTS
    
    if(subgraph.get_name() == graph_name):
        return None
    
    current = subgraph
    while(PARENTS[current.get_name()].get_name() != graph_name):
        current = PARENTS[current.get_name()]
    return current


def get_bb(node_name):
    """
        Get the bb of a node_name
        
        :param node_name: the string to find the bb
        :return: the bb
        :rtype: int
    """
    return int(re.search(r'\d+', re.search(r'block_\d+', node_name).group()).group())


def update_edge_node_name(node_name, node_number):
    """
        Update the node_name coming from an edge based on the node_number
        
        :param node_name: the node name
        :param node_number: the number to update
        :return: The new node_name
        :rype: String
    """
    return node_name.replace('block_' + str(node_number), 'block_' + str(node_number+1))


def update_edges(subgraph, graph_name, bb):
    """
        Update the edges of the top parent of the subgraph
        
        :param subgraph: the subgraph which top parent's edges has to be updated
        :param graph_name: the root of the arborescence of subgraph
        :param bb: the bb from which it updates the edges
    """
    top_subgraph = get_top_parent(subgraph, graph_name)
    edges = extract_edges(top_subgraph)
    for edge in edges:
        if(edge.get_style() is not None):
            style = edge.get_style()
        if(edge.get_color() is not None):
            color = edge.get_color()
        if(edge.get_label() is not None):
            label = edge.get_label()
        node_head = edge.get_source()
        node_tail = edge.get_destination()
        bb_head = get_bb(node_head)
        bb_tail = get_bb(node_tail)
        if(bb_head >= bb or bb_tail > bb):
            top_subgraph.del_edge(node_head, node_tail, 0)
            if bb_head >= bb:
                if bb_tail > bb:
                    add_edge(top_subgraph, update_edge_node_name(node_head, bb_head), update_edge_node_name
                             (node_tail, bb_tail), style=style, color=color, label=label)
                else:
                    add_edge(top_subgraph, update_edge_node_name(node_head, bb_head), node_tail, style=style, 
                             color=color, label=label)
            else:
                add_edge(top_subgraph, node_head, update_edge_node_name(node_tail, bb_tail), 
                         style=style, color=color, label=label)
                
            #si bb_n < bb et bb_s <= bb on touche pas
            #sinon
            #    si bb_n >= bb:
            #        si bb_s >= bb:
            #            creer edge (n+1, s+1)
            #        sinon:
            #            creer edge (n+1, s)
            #    sinon:
            #        si bb_s > bb:
            #          creer edge (n, s+1)


def create_new_edge(graph, node_name, subgraph_function):
    """
        Create the edges corresponding of the call and return of the function
        
        :param graph: edges are added in the graph
        :param node_name: the node from where the call is made
        :param subgraph_function: the subgraph of the function called
    """
    nodes_function = extract_nodes(subgraph_function)
    add_edge(graph, node_name+":s", nodes_function[0].get_name()+":n", color="green")
    add_edge(graph, nodes_function[1].get_name()+":s", update_edge_node_name(node_name, get_bb(node_name))+":n", color="red")
    return


###
# The export
###

# For all the subgraph, we need to update their names because there is a syntax error during the output otherwise

def recreate_subgraphs_name():
    """
        Recreate the name of the subgraphs to write them in dot format
    """
    global SUBGRAPHS
    for (name, subgraph) in SUBGRAPHS.items():
        subgraph.set_name("\"cluster_" + subgraph.get_name() + "\"")


# Export the graph

def export_graph(graph, name_file, format_export):
    """
        Export the graph with its name and its format given
        
        :param graph: the graph
        :param name_file: the name of the file
        :param format_export: the format of the export
    """
    im_name = ('{}.' + format_export).format('./' + name_file)
    if (format_export == "png"):
        graph.write_png(im_name)
    elif (format_export ==  "dot"):
        graph.write_dot(im_name)
    else:
        raise LookupError


###
# Main
###

def main(dot_file):
    """
        Take a graph from the file and format it to adopt our constraints
        
        :param file: the file to get
        :return: the graph
        :rtype: Graph
    """
    global SUBGRAPHS, PARENTS
    graph = graph_from_dot(dot_file)
    SUBGRAPHS = {}
    PARENTS = {}
    extract_subgraphs([graph])
    
    for (name, subgraph) in SUBGRAPHS.items():
        nodes = extract_nodes(subgraph)
        for node in nodes:
            (name_function, result, function_call_line) = analyse_label_function_calls(node)
            if name_function is not None:
                (label_node1, label_node2, bb) = create_labels(node, result, function_call_line)
                node.set_label(label_node1)
                nodes_to_update = get_nodes_to_update(subgraph, graph.get_name())
                update_nodes(nodes_to_update, bb)
                nodes.append(create_new_node(subgraph, node, label_node2, bb))
                update_edges(subgraph, graph.get_name(), bb)
                create_new_edge(graph, node.get_name(), SUBGRAPHS[name_function])
    recreate_subgraphs_name()
    export_graph(graph, "main_output", "png")
    export_graph(graph, "main_output", "dot")
    return graph


print(sys.argv[1])
FILE = main(sys.argv[1])
