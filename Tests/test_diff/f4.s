	.file	"f4.c"
	.text
	.p2align 4,,15
	.globl	foo
	.type	foo, @function
foo:
.LFB0:
	.cfi_startproc
	leal	(%rdi,%rsi), %eax
	cmpl	%eax, %edi
	jle	.L1
	addl	$9, %edi
	cmpl	%edi, %eax
	jle	.L4
.L3:
	jmp	.L3
	.p2align 4,,10
	.p2align 3
.L4:
	movl	$11, %eax
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
