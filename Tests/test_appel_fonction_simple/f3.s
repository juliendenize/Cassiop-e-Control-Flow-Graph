	.file	"f3.c"
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
	cmpl	$1, %edi
	pushq	%rbx
	.cfi_def_cfa_offset 16
	.cfi_offset 3, -16
	jle	.L5
	movq	8(%rsi), %rax
	movsbl	(%rax), %ecx
.L5:
	movl	%ecx, %eax
	movl	$1374389535, %edx
	imull	%edx
	movl	%ecx, %eax
	sarl	$31, %eax
	sarl	$4, %edx
	movl	%edx, %ebx
	movl	$1717986919, %edx
	subl	%eax, %ebx
	imull	$50, %ebx, %ebx
	subl	%ebx, %ecx
	movl	%ecx, %eax
	movl	%ecx, %esi
	movl	%ecx, %ebx
	imull	%edx
	movl	%ecx, %eax
	sarl	$31, %eax
	sarl	$2, %edx
	subl	%eax, %edx
	leal	(%rdx,%rdx,4), %eax
	addl	%eax, %eax
	subl	%eax, %esi
	cmpl	%ecx, %esi
	jle	.L6
	leaq	.LC0(%rip), %rsi
	movl	%ecx, %edx
	movl	$1, %edi
	xorl	%eax, %eax
	call	__printf_chk@PLT
.L6:
	leaq	.LC0(%rip), %rsi
	movl	%ebx, %edx
	movl	$1, %edi
	xorl	%eax, %eax
	call	__printf_chk@PLT
	xorl	%eax, %eax
	popq	%rbx
	.cfi_def_cfa_offset 8
	ret
	.cfi_endproc
.LFE25:
	.size	main, .-main
	.ident	"GCC: (Ubuntu 7.3.0-27ubuntu1~18.04) 7.3.0"
	.section	.note.GNU-stack,"",@progbits
