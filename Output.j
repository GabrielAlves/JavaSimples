.class public Output.j
.super java/lang/Object

.method public static lerInteiro()I
   .limit stack 3
   .limit locals 1

   new java/util/Scanner
   dup
   getstatic java/lang/System/in Ljava/io/InputStream;
   invokespecial java/util/Scanner/<init>(Ljava/io/InputStream;)V
   invokevirtual java/util/Scanner/nextInt()I ; usa o nextInt do Scanner
   ireturn
.end method

.method public static main([Ljava/lang/String;)V
	.limit stack 1
	.limit locals 2
	; inicio das declaracoes
	ldc 0
	istore 0
	ldc 0
	istore 1
	; fim das declaracoes
; Comando scanf
	invokestatic Output.j/lerInteiro()I
	istore 0
	invokestatic Output.j/lerInteiro()I
	istore 1
.end method