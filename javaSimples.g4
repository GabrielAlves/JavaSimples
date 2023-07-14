grammar javaSimples;
import lexerJavaSimples;

/* Ponto de partida */
programa: dec_de_func* funcao_main;

/* Regras da função main */
funcao_main: 'main' ':' dec_de_var? comando* 'end';

/* Regras de funções */
dec_de_func: cabecalho_de_func dec_de_var? comando* 'end';
cabecalho_de_func: IDENTIFICADOR '(' lista_de_param_de_func ')' ':' (TIPO | 'void');
lista_de_param_de_func : (parametro (',' parametro)*)?;
parametro: TIPO IDENTIFICADOR;

/* Regras de variáveis */
dec_de_var: 'var' ':' ((dec_de_var_nao_const | dec_de_var_const) ';')+;
dec_de_var_nao_const: lista_de_var ':' TIPO;
dec_de_var_const: 'const' lista_de_var_com_atrib;

/* Regras auxiliares */
lista_de_var : IDENTIFICADOR (',' IDENTIFICADOR)*;
lista_de_var_com_atrib : IDENTIFICADOR '=' expressao (',' IDENTIFICADOR '=' expressao)*;
lista_de_expr_aritmetica: expr_aritimetica (',' expr_aritimetica)*;
lista_de_expr_relacional: expr_relacional (OPERADOR_LOGICO expr_relacional)*;


expressao: expr_aritimetica | expr_relacional;

expr_aritimetica: '-'? parentese_aritimetico expr_aritimetica_2?;
expr_aritimetica_2: OPERADOR_ARIT_LVL_2 expr_aritimetica
    | OPERADOR_ARIT_LVL_1 expr_aritimetica;
parentese_aritimetico: termo | '(' expr_aritimetica ')';

expr_relacional: '!'? parentese_relacional expr_relacional_2?;
expr_relacional_2: OPERADOR_RELACIONAL_LVL_2 expr_relacional
    | OPERADOR_RELACIONAL_LVL_1 expr_relacional;
parentese_relacional: termo | '(' expr_relacional ')';

termo: IDENTIFICADOR
    | (VALOR_INT | VALOR_FLOAT)
    |  chamada_funcao;

/* Regras de comandos */
comando: comando_if
       | comando_while
       | comando_scanf
       | comando_print
       | comando_atrib
       | comando_return
       | comando_break
       | chamada_funcao ';';

comando_if: 'if' '(' lista_de_expr_relacional ')' ':' comando* ('else' ':' comando*)? 'end';
comando_while: 'while' '(' lista_de_expr_relacional ')' ':' (comando)+ 'end';
comando_scanf: 'scanf' '(' lista_de_var ')' ';';
comando_atrib : IDENTIFICADOR '=' expressao ';';
comando_print: 'print' '(' lista_de_expr_aritmetica ')' ';';
comando_break: 'break' ';';
comando_return: 'return' expressao ';';
chamada_funcao: IDENTIFICADOR '(' (lista_de_var | expressao)? ')';
