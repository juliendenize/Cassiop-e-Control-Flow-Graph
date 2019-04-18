	.file	"f4_optimized.c"
	.text
	.p2align 4,,15
	.globl	foo1
	.type	foo1, @function
foo1:
.LFB41:
	.cfi_startproc
	movl	%edi, %edx
	shrl	$31, %edx
	leal	(%rdi,%rdx), %eax
	andl	$1, %eax
	subl	%edx, %eax
	ret
	.cfi_endproc
.LFE41:
	.size	foo1, .-foo1
	.p2align 4,,15
	.globl	foo2
	.type	foo2, @function
foo2:
.LFB42:
	.cfi_startproc
	jmp	rand@PLT
	.cfi_endproc
.LFE42:
	.size	foo2, .-foo2
	.section	.rodata.str1.1,"aMS",@progbits,1
.LC0:
	.string	"%d"
	.section	.text.startup,"ax",@progbits
	.p2align 4,,15
	.globl	main
	.type	main, @function
main:
.LFB43:
	.cfi_startproc
	subq	$8, %rsp
	.cfi_def_cfa_offset 16
	cmpl	$1, %edi
	jle	.L5
	movq	8(%rsi), %rax
	movsbl	(%rax), %edx
.L5:
	leaq	.LC0(%rip), %rsi
	addl	%edx, %edx
	movl	$1, %edi
	xorl	%eax, %eax
	call	__printf_chk@PLT
	xorl	%eax, %eax
	addq	$8, %rsp
	.cfi_def_cfa_offset 8
	ret
	.cfi_endproc
.LFE43:
	.size	main, .-main
	.ident	"GCC: (Ubuntu 7.3.0-27ubuntu1~18.04) 7.3.0"
	.section	.note.GNU-stack,"",@progbits
