	.file	"f7.c"
	.text
	.p2align 4,,15
	.globl	foo
	.type	foo, @function
foo:
.LFB23:
	.cfi_startproc
	leal	(%rdi,%rsi), %eax
	movl	$10, %edx
	cmpl	%eax, %esi
	cmovl	%edx, %eax
	ret
	.cfi_endproc
.LFE23:
	.size	foo, .-foo
	.section	.text.startup,"ax",@progbits
	.p2align 4,,15
	.globl	main
	.type	main, @function
main:
.LFB24:
	.cfi_startproc
	xorl	%eax, %eax
	ret
	.cfi_endproc
.LFE24:
	.size	main, .-main
	.ident	"GCC: (Ubuntu 7.4.0-1ubuntu1~18.04) 7.4.0"
	.section	.note.GNU-stack,"",@progbits
