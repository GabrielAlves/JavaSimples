.class public funcao_testes_do_daniel
.super java/lang/Object

.method public static soma(II)I
	.limit stack 3
	.limit locals 2
	; Comando atrib
	iload 0
	iload 1
	iadd
	istore 0
	iload 0
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
    	new java/util/Scanner       ; Cria uma nova instância de Scanner
    	dup
    	getstatic java/lang/System/in Ljava/io/InputStream;
    	invokespecial java/util/Scanner/<init>(Ljava/io/InputStream;)V
    	invokevirtual java/util/Scanner/nextFloat()F   ; Lê o valor float
    	freturn    ; Retorna o valor float lido
.end method
.method public static readString()Ljava/lang/String;
    	.limit stack 3
    	.limit locals 4
    	new java/util/Scanner        ; Cria uma nova instância de Scanner
    	dup
    	getstatic java/lang/System/in Ljava/io/InputStream;
    	invokespecial java/util/Scanner/<init>(Ljava/io/InputStream;)V
    	invokevirtual java/util/Scanner/nextLine()Ljava/lang/String;  ; Lê a linha inteira
    	astore_0    ; Armazena a string lida na variável local 0
    	aload_0     ; Carrega a string na pilha
    	areturn     ; Retorna a string lida
.end method
.method public static readBoolean()I
    	.limit stack 3
    	.limit locals 4
    	new java/util/Scanner        ; Cria uma nova instância de Scanner
    	dup
    	getstatic java/lang/System/in Ljava/io/InputStream;
    	invokespecial java/util/Scanner/<init>(Ljava/io/InputStream;)V
    	invokevirtual java/util/Scanner/nextBoolean()Z  ; Lê o valor booleano
    	ifeq false_value   ; Se o valor booleano for falso, vá para o rótulo false_value
    	ldc 1              ; Se for verdadeiro, carrega o valor 1 na pilha
    	goto end
false_value:
    	ldc 0              ; Carrega o valor 0 na pilha
end:
    	ireturn            ; Retorna o valor inteiro na pilha
.end method


.method public static main([Ljava/lang/String;)V
	.limit stack 3
	.limit locals 2
	; inicio das declaracoes
	ldc 0
	istore 0
	ldc 0
	istore 1
	; fim das declaracoes
	; Comando atrib
; Comando funcao
	iload 0
	ldc 1
	iadd
	iload 1
	invokestatic funcao_testes_do_daniel/soma(II)I
	istore 0
	; Comando print
	getstatic java/lang/System/out Ljava/io/PrintStream;
	iload 0
	invokevirtual java/io/PrintStream/println(I)V
	return
.end method
