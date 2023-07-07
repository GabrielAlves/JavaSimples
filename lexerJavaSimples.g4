lexer grammar lexerJavaSimples;

//EXPR: DADO OPERADOR_BINARIO DADO (OPERADOR_BINARIO DADO)* | OPERADOR_UNARIO+ DADO;
DADO: VALOR | IDENTIFICADOR;
VALOR: VALOR_INT | VALOR_FLOAT | VALOR_STR | VALOR_BOOL;
VALOR_INT : [0-9]+;
VALOR_FLOAT : [0-9]+ '.' [0-9]+;
VALOR_STR : '"' [a-zA-Z0-9_ ]* '"'; // TODO: Encontrar definição mais abrangente.
VALOR_BOOL : 'true' | 'false';
//EXPRESSAO: VALOR | VALOR OPERADOR EXPRESSAO;
OPERADOR_UNARIO: '!' | '-';
OPERADOR_BINARIO: OPERADOR_ARITMETICO | OPERADOR_RELACIONAL;
OPERADOR_ARITMETICO: '*' | '/' | '+' | '-';
OPERADOR_RELACIONAL: '==' | '!=' | '>=' | '<=' | '>' | '<';
TIPO : 'int' | 'str' | 'float' | 'bool';
IDENTIFICADOR : [a-zA-Z][a-zA-Z0-9_]*;
WS : [ \t\r\n] -> skip;
