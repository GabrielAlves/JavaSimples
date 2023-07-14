lexer grammar lexerJavaSimples;

/* Regras léxicas */
VALOR_INT : [0-9]+;
VALOR_FLOAT : [0-9]+ '.' [0-9]+;
VALOR_STR : '"' ( ~[\\\r\n\f"] )* '"'
          | '“' ( ~[\\\r\n\f"] )* '”'
          | '\'' ( ~[\\\r\n\f"] )* '\'';
// ( ~[\\\r\n\f"] )* significa qualquer char, exceto  "\", "\r", "\n", "\f" e """.

VALOR_BOOL : 'true'
           | 'false';

OPERADOR_ARIT_LVL_1: '+'
                   | '-';
OPERADOR_ARIT_LVL_2: '*'
                   | '/';

OPERADOR_RELACIONAL_LVL_2: '==';
OPERADOR_RELACIONAL_LVL_1: '!='
                   | '>='
                   | '<='
                   | '>'
                   | '<';

OPERADOR_LOGICO: '&&'
               | '||';

OPERADOR_UNARIO: '!'
               | '-';

TIPO : 'int'
     | 'str'
     | 'float'
     | 'bool';

IDENTIFICADOR : [a-zA-Z][a-zA-Z0-9_]*;

COMENTARIO_BLOCO: '/*' .*? '*/' -> skip;
COMENTARIO_LINHA : '//' ~[\r\n]* -> skip;
WS : [ \t\r\n] -> skip;
