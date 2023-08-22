.class public somaSimples
.super java/lang/Object

.method public static Soma(II)I
	.limit stack 3
	.limit locals 2
	iload 0
	iload 1
	iadd
	ireturn
.end method

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
.method public static readFloat()F
    	.limit stack 3
    	.limit locals 3
    	new java/util/Scanner       ; Cria uma nova inst�ncia de Scanner
    	dup
    	getstatic java/lang/System/in Ljava/io/InputStream;
    	invokespecial java/util/Scanner/<init>(Ljava/io/InputStream;)V
    	invokevirtual java/util/Scanner/nextFloat()F   ; L� o valor float
    	freturn    ; Retorna o valor float lido
.end method
.method public static readString()Ljava/lang/String;
    	.limit stack 3
    	.limit locals 4
    	new java/util/Scanner        ; Cria uma nova inst�ncia de Scanner
    	dup
    	getstatic java/lang/System/in Ljava/io/InputStream;
    	invokespecial java/util/Scanner/<init>(Ljava/io/InputStream;)V
    	invokevirtual java/util/Scanner/nextLine()Ljava/lang/String;  ; L� a linha inteira
    	astore_0    ; Armazena a string lida na vari�vel local 0
    	aload_0     ; Carrega a string na pilha
    	areturn     ; Retorna a string lida
.end method
.method public static readBoolean()I
    	.limit stack 3
    	.limit locals 4
    	new java/util/Scanner        ; Cria uma nova inst�ncia de Scanner
    	dup
    	getstatic java/lang/System/in Ljava/io/InputStream;
    	invokespecial java/util/Scanner/<init>(Ljava/io/InputStream;)V
    	invokevirtual java/util/Scanner/nextBoolean()Z  ; L� o valor booleano
    	ifeq false_value   ; Se o valor booleano for falso, v� para o r�tulo false_value
    	ldc 1              ; Se for verdadeiro, carrega o valor 1 na pilha
    	goto end
false_value:
    	ldc 0              ; Carrega o valor 0 na pilha
end:
    	ireturn            ; Retorna o valor inteiro na pilha
.end method


.method public static main([Ljava/lang/String;)V
	.limit stack 2
	.limit locals 2
	; inicio das declaracoes
	ldc 0
	istore 0
	ldc ""
	astore 1
	; fim das declaracoes
	; Comando atrib
	ldc 2
	istore 0
; Comando scanf
	invokestatic somaSimples/readString()Ljava/lang/String;
 	astore 1
	; Comando print
	getstatic java/lang/System/out Ljava/io/PrintStream;
	aload 1
	invokevirtual java/io/PrintStream/println(Ljava/lang/String;)V
	return
.end method
