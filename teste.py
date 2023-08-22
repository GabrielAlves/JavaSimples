f".method public static readBoolean()I\n\
    \t.limit stack 3\n\
    \t.limit locals 4\n\
    \tnew java/util/Scanner        ; Cria uma nova instância de Scanner\n\
    \tdup\n\
    \tgetstatic java/lang/System/in Ljava/io/InputStream;\n\
    \tinvokespecial java/util/Scanner/<init>(Ljava/io/InputStream;)V\n\
    \tinvokevirtual java/util/Scanner/nextBoolean()Z  ; Lê o valor booleano\n\
    \tifeq false_value   ; Se o valor booleano for falso, vá para o rótulo false_value\n\
    \tldc 1              ; Se for verdadeiro, carrega o valor 1 na pilha\n\
    \tgoto end\n\
false_value:\n\
    \tldc 0              ; Carrega o valor 0 na pilha\n\
end:\n\
    \tireturn            ; Retorna o valor inteiro na pilha\n\
.end method\n"
