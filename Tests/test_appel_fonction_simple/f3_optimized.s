	.file	"f3_optimized.c"
	.text
	.p2align 4,,15
	.globl	foo1
	.type	foo1, @function
foo1:
.LFB23:
	.cfi_startproc
	movl	%edi, %eax
	movl	$1374389535, %edx
	imull	%edx
	movl	%edx, %eax
	movl	%edi, %edx
	sarl	$4, %eax
	sarl	$31, %edx
	subl	%edx, %eax
	imull	$50, %eax, %eax
	subl	%eax, %edi
	movl	%edi, %eax
	ret
	.cfi_endproc
.LFE23:
	.size	foo1, .-foo1
	.p2align 4,,15
	.globl	foo2
	.type	foo2, @function
foo2:
.LFB24:
	.cfi_startproc
	movl	%edi, %eax
	movl	$1717986919, %edx
	imull	%edx
	movl	%edx, %eax
	movl	%edi, %edx
	sarl	$2, %eax
	sarl	$31, %edx
	subl	%edx, %eax
	leal	(%rax,%rax,4), %eax
	addl	%eax, %eax
	subl	%eax, %edi
	movl	%edi, %eax
	ret
	.cfi_endproc
.LFE24:
	.size	foo2, .-foo2
	.section	.rodata.str1.1,"aMS",@progbits,1
.LC0:
	.string	"%d"
	.section	.text.startup,"ax",@progbits
	.p2align 4,,15
	.globl	main
	.type	main, @function
main:
.LFB25:
	.cfi_startproc
	subq	$8, %rsp
	.cfi_def_cfa_offset 16
	cmpl	$1, %edi
	jle	.L5
	movq	8(%rsi), %rax
	movsbl	(%rax), %r8d
.L5:
	movl	%r8d, %eax
	movl	$1374389535, %ecx
	leaq	.LC0(%rip), %rsi
	imull	%ecx
	movl	$1, %edi
	movl	%edx, %eax
	movl	%r8d, %edx
	sarl	$31, %edx
	sarl	$4, %eax
	subl	%edx, %eax
	movl	%r8d, %edx
	imull	$50, %eax, %eax
	subl	%eax, %edx
	xorl	%eax, %eax
	call	__printf_chk@PLT
	xorl	%eax, %eax
	addq	$8, %rsp
	.cfi_def_cfa_offset 8
	ret
	.cfi_endproc
.LFE25:
	.size	main, .-main
	.ident	"GCC: (Ubuntu 7.3.0-27ubuntu1~18.04) 7.3.0"
	.section	.note.GNU-stack,"",@progbits
