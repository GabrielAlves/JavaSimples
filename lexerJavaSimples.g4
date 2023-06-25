lexer grammar lexerJavaSimples;

VALOR_INT : [0-9]+;
VALOR_FLOAT : [0-9]+ '.' [0-9]+;
VALOR_STR : '"' [a-zA-Z0-9_]* '"'; // TODO: Encontrar definição mais abrangente.
VALOR_BOOL : 'true' | 'false';
VALOR: VALOR_INT | VALOR_FLOAT | VALOR_STR | VALOR_BOOL;
//EXPRESSAO: VALOR | VALOR OPERADOR EXPRESSAO;
OPERADOR: '!' | '-' | '*' | '/' | '+' | '==' | '!=' | '>=' | '<=' | '>' | '<';
TIPO : 'int' | 'str' | 'float' | 'bool';
IDENTIFICADOR : [a-zA-Z][a-zA-Z0-9_]*;
WS : [ \t\r\n] -> skip;