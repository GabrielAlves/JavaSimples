.class public funcao_prof
.super java/lang/Object

.method public static fatorial(I)I
	.limit stack 5
	.limit locals 1
; Comando if
	iload 0
	ldc 1
	if_icmple loop0
	; Comando print
	getstatic java/lang/System/out Ljava/io/PrintStream;
	iload 0
	invokevirtual java/io/PrintStream/println(I)V
	iload 0
; Comando funcao
	iload 0
	ldc 1
	isub
	invokestatic funcao_prof/fatorial(I)I
	imult
	ireturn
	goto loop1
loop0:
	ldc 1
	ireturn
loop1:
.end method

.method public static mostrarMedia(II)V
	.limit stack 3
	.limit locals 4
	; inicio das declaracoes
	ldc 0.0
	fstore 2
	ldc 0
	istore 3
	; fim das declaracoes
	; Comando atrib
	iload 0
	iload 1
	iadd
	ldc 2
	idiv
	i2f
	fstore 2
	; Comando print
	getstatic java/lang/System/out Ljava/io/PrintStream;
	ldc "Resultado: "
	invokevirtual java/io/PrintStream/println(Ljava/lang/String;)V
	getstatic java/lang/System/out Ljava/io/PrintStream;
	fload 2
	invokevirtual java/io/PrintStream/println(F)V
.end method

.method public static media(FF)F
	.limit stack 3
	.limit locals 3
	; inicio das declaracoes
	ldc 0.0
	fstore 2
	; fim das declaracoes
	; Comando atrib
	fload 0
	fload 1
	fadd
	ldc 2
	i2f
	fdiv
	fstore 2
	fload 2
	freturn
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
	.limit locals 3
	; inicio das declaracoes
	ldc 0
	istore 0
	ldc 0
	istore 1
	ldc 0
	istore 2
	; fim das declaracoes
	; Comando print
	getstatic java/lang/System/out Ljava/io/PrintStream;
	ldc "Programa Fatorial. Digite o valor?"
	invokevirtual java/io/PrintStream/println(Ljava/lang/String;)V
; Comando scanf
	invokestatic funcao_prof/lerInteiro()I
	istore 0
	; Comando print
	getstatic java/lang/System/out Ljava/io/PrintStream;
; Comando funcao
	iload 0
	invokestatic funcao_prof/fatorial(I)I
	invokevirtual java/io/PrintStream/println(I)V
	; Comando print
	getstatic java/lang/System/out Ljava/io/PrintStream;
	ldc "Programa Media. Digite o valores?"
	invokevirtual java/io/PrintStream/println(Ljava/lang/String;)V
; Comando scanf
	invokestatic funcao_prof/lerInteiro()I
	istore 1
	invokestatic funcao_prof/lerInteiro()I
	istore 2
; Comando funcao
	iload 1
	iload 2
	invokestatic funcao_prof/mostrarMedia(II)I
	return
.end method
