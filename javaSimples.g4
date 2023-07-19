grammar javaSimples;
import lexerJavaSimples;

/* Ponto de partida */
programa: dec_de_func* funcao_main;

/* Regras da função main */
funcao_main: 'main' ':' decl_de_variaveis? comando* 'end';

/* Regras de funções */
dec_de_func: cabecalho_de_func decl_de_variaveis? comando* 'end';
cabecalho_de_func: IDENTIFICADOR '(' lista_de_parametros ')' ':' (TIPO | 'void');
lista_de_parametros : (parametro (',' parametro)*)?;
parametro: TIPO IDENTIFICADOR;

/* Regras de variáveis */
decl_de_variaveis: 'var' ':' ((decl_de_var | decl_de_var_const) ';')+;
decl_de_var: lista_de_var ':' TIPO;
decl_de_var_const: 'const' lista_de_atribuicao;

/* Regras auxiliares */
lista_de_var : IDENTIFICADOR (',' IDENTIFICADOR)*;
lista_de_atribuicao : IDENTIFICADOR '=' expressao (',' IDENTIFICADOR '=' expressao)*;
lista_expressao: expressao (',' expressao)*;
//lista_expr_aritmetica: expr_aritimetica (',' expr_aritimetica)*;
//lista_expr_relacional: expr_relacional (',' expr_relacional)*;

expressao: expr_aritimetica | expr_relacional;

expr_aritimetica: chamada_funcao
    | expr_aritimetica OPERADOR_ARIT_LVL_2 expr_aritimetica
    | expr_aritimetica OPERADOR_ARIT_LVL_1 expr_aritimetica
    | termo_aritimetico;
termo_aritimetico: OPERADOR_UNARIO_ARIT termo_aritimetico
    | IDENTIFICADOR
    | (VALOR_INT | VALOR_FLOAT | VALOR_STR)
    | '(' expr_aritimetica ')';

expr_relacional: chamada_funcao
    | termo_relacional OPERADOR_RELACIONAL_LVL_2 termo_relacional
    | termo_relacional OPERADOR_RELACIONAL_LVL_1 termo_relacional;
termo_relacional: OPERADOR_UNARIO_RELACIONAL expr_relacional
    | IDENTIFICADOR
    | (VALOR_INT | VALOR_FLOAT | VALOR_BOOL)
    | '(' expr_relacional ')';

/* Regras de comandos */
comando: comando_if
       | comando_while
       | comando_scanf
       | comando_print
       | comando_atrib
       | comando_return
       | comando_break
       | chamada_funcao ';';

comando_if: 'if' '(' expr_relacional ')' ':' comando* ('else' ':' comando*)? 'end';
comando_while: 'while' '(' expr_relacional ')' ':' (comando)+ 'end';
comando_scanf: 'scanf' '(' lista_de_var ')' ';';
comando_atrib : IDENTIFICADOR '=' expressao ';';
comando_print: 'print' '(' lista_expressao ')' ';';
comando_break: 'break' ';';
comando_return: 'return' expressao ';';
chamada_funcao: IDENTIFICADOR '(' (lista_de_var | expressao)? ')';
