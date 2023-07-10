grammar javaSimples;
// lexerJavaSimples;

/*
Estrutura básica:
programa: dec_de_func* funcao_main;
funcao_main: 'main' ':' dec_de_var? comando* 'end';
etc
*/

/* Ponto de partida */
programa: funcao_main;


/* Regras de funções */
dec_de_func: cabecalho_de_func dec_de_var? comando* 'end';
cabecalho_de_func: IDENTIFICADOR '(' lista_de_param_de_func ')' ':' (TIPO | 'void');
lista_de_param_de_func : (parametro(',' parametro)*)*;
parametro: TIPO IDENTIFICADOR;


/* Regras de variáveis */
dec_de_var: 'var' ':' ((dec_de_var_nao_const | dec_de_var_const) ';')+;
dec_de_var_nao_const: lista_de_var ':' TIPO;
dec_de_var_const: 'const' lista_de_var_com_atrib;


/* Regras auxiliares */
lista_de_var : IDENTIFICADOR (',' IDENTIFICADOR)*;
expr: termo expr*
    | (OPERADOR_ARITMETICO | OPERADOR_RELACIONAL) termo;
termo: '(' expr ')'
     | IDENTIFICADOR
     | (VALOR_INT | VALOR_FLOAT | VALOR_STR | VALOR_BOOL);

lista_de_expr_relacional: expr_relacional (OPERADOR_LOGICO expr_relacional)*;
expr_relacional: expr OPERADOR_RELACIONAL expr;

lista_de_var_com_atrib : IDENTIFICADOR '=' expr (',' IDENTIFICADOR '=' expr)*;
lista_de_expr: expr (',' expr)*;


/* Regras de comandos */
comando: comando_if
       | comando_while
       | comando_scanf
       | comando_print
       | comando_atrib
       | comando_return
       | comando_break;

comando_if: 'if' '(' lista_de_expr_relacional ')' ':' comando+ ('else' ':' comando+)? 'end';
comando_while: 'while' '(' lista_de_expr_relacional ')' ':' (comando)+ 'end';
comando_scanf: 'scanf' '(' lista_de_var ')' ';';
comando_atrib : IDENTIFICADOR '=' expr ';';
comando_print: 'print' '(' lista_de_expr ')' ';';
comando_break: 'break' ';';
comando_return: 'return' expr ';';


/* Regras da função main */
funcao_main: 'main' ':' dec_de_var? comando* 'end';

/* VALOR: VALOR_INT
     | VALOR_FLOAT
     | VALOR_STR
     | VALOR_BOOL; */

VALOR_INT : [0-9]+;
VALOR_FLOAT : [0-9]+ '.' [0-9]+;
VALOR_STR : '"' ( ~[\\\r\n\f"] )* '"'
          | '“' ( ~[\\\r\n\f"] )* '”'
          | '\'' ( ~[\\\r\n\f"] )* '\'';
// ( ~[\\\r\n\f"] )* significa qualquer char, exceto  "\", "\r", "\n", "\f" e """.

VALOR_BOOL : 'true'
           | 'false';

OPERADOR_UNARIO: '!'
               | '-';

OPERADOR_ARITMETICO: '*'
                   | '/'
                   | '+'
                   | '-';

OPERADOR_RELACIONAL: '=='
                   | '!='
                   | '>='
                   | '<='
                   | '>'
                   | '<';

OPERADOR_LOGICO: '&&'
               | '||';

TIPO : 'int'
     | 'str'
     | 'float'
     | 'bool';

IDENTIFICADOR : [a-zA-Z][a-zA-Z0-9_]*;
WS : [ \t\r\n] -> skip;
