	.file	"f2.c"
	.text
	.p2align 4,,15
	.globl	foo
	.type	foo, @function
foo:
.LFB0:
	.cfi_startproc
	leal	-1(%rdi), %edx
	xorl	%eax, %eax
	cmpl	$98, %edx
	ja	.L1
	movl	%edi, %eax
	movl	$780903145, %edx
	imull	%edx
	movl	%edi, %eax
	sarl	$31, %eax
	sarl	%edx
	subl	%eax, %edx
	leal	(%rdx,%rdx,4), %eax
	leal	(%rdx,%rax,2), %eax
	subl	%eax, %edi
	cmpl	$1, %edi
	sbbl	%eax, %eax
	andl	$11, %eax
.L1:
	rep ret
	.cfi_endproc
.LFE0:
	.size	foo, .-foo
	.section	.text.startup,"ax",@progbits
	.p2align 4,,15
	.globl	main
	.type	main, @function
main:
.LFB1:
	.cfi_startproc
	xorl	%eax, %eax
	ret
	.cfi_endproc
.LFE1:
	.size	main, .-main
	.ident	"GCC: (Ubuntu 7.3.0-27ubuntu1~18.04) 7.3.0"
	.section	.note.GNU-stack,"",@progbits
