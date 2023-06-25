lexer grammar lexerJavaSimples;

VALOR: VALOR_INT | VALOR_FLOAT | VALOR_STR | VALOR_BOOL;
VALOR_INT : [0-9]+;
VALOR_FLOAT : [0-9]+ '.' [0-9]+;
VALOR_STR : '"' [a-zA-Z0-9]* '"'; // TODO: Descobrir definição mais abrangente.
VALOR_BOOL : 'true' | 'false';
TIPO : 'int' | 'str' | 'float' | 'bool';
IDENTIFICADOR : [a-zA-Z][a-zA-Z0-9_]*;
WS : [ \t\r\n] -> skip;