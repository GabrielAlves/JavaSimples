grammar javaSimples;
import lexerJavaSimples;

/* Ponto de partida */
programa: dec_de_func* funcao_main;

/* Regras da função main */
funcao_main: 'main' ':' declaracoes? comando* 'end';

/* Regras de funções */
dec_de_func: cabecalho_de_func declaracoes? comando* 'end';
cabecalho_de_func: IDENTIFICADOR '(' lista_de_parametros ')' ':' (TIPO | 'void');
lista_de_parametros : (parametro (',' parametro)*)?;
parametro: TIPO IDENTIFICADOR;

/* Regras de variáveis */
declaracoes: 'var' ':' ((decl_de_var | decl_de_const) ';')+;
decl_de_var: lista_de_var ':' TIPO;
decl_de_const: 'const' IDENTIFICADOR '=' (VALOR_INT | VALOR_FLOAT | VALOR_STR | VALOR_BOOL) (',' IDENTIFICADOR '=' (VALOR_INT | VALOR_FLOAT | VALOR_STR | VALOR_BOOL))*;

/* Regras de listas */
lista_de_var : IDENTIFICADOR (',' IDENTIFICADOR)*;
lista_de_expressoes: expressao (',' expressao)*;

/* Regras de expressões */
expressao: expr_aritimetica | expr_relacional | VALOR_STR | chamada_funcao;
/* Expressões Aritimeticas  */
expr_aritimetica: expr_aritimetica OPERADOR_ARIT_LVL_2 expr_aritimetica
    | expr_aritimetica OPERADOR_ARIT_LVL_1 expr_aritimetica
    | OPERADOR_UNARIO_ARIT? termo_aritimetico;
termo_aritimetico:IDENTIFICADOR
    | (VALOR_INT | VALOR_FLOAT)
    | '(' expr_aritimetica ')';
/* Expressões Booleanas */
expr_relacional: OPERADOR_UNARIO_RELACIONAL? termo_relacional OPERADOR_RELACIONAL_LVL_2 OPERADOR_UNARIO_RELACIONAL? termo_relacional
    | OPERADOR_UNARIO_RELACIONAL? termo_relacional OPERADOR_RELACIONAL_LVL_1 OPERADOR_UNARIO_RELACIONAL? termo_relacional
    | OPERADOR_UNARIO_RELACIONAL? termo_relacional;
termo_relacional: IDENTIFICADOR
    | (VALOR_INT | VALOR_FLOAT | VALOR_BOOL)
    | OPERADOR_UNARIO_RELACIONAL? '(' expr_relacional ')';

/* Regras de comandos */
comando: comando_if
       | comando_while
       | comando_scanf
       | comando_print
       | comando_atrib
       | comando_return
       | comando_break
       | chamada_funcao ';';

comando_if: 'if' '(' expr_relacional ')' ':' comando* (comando_else)? 'end';
comando_else: 'else' ':' comando*;
comando_while: 'while' '(' expr_relacional ')' ':' (comando)+ 'end';
comando_scanf: 'scanf' '(' lista_de_var ')' ';';
comando_atrib : IDENTIFICADOR '=' expressao ';';
comando_print: 'print' '(' lista_de_expressoes ')' ';';
comando_break: 'break' ';';
comando_return: 'return' expressao ';';
chamada_funcao: IDENTIFICADOR '(' (lista_de_var | lista_de_expressoes)? ')';
