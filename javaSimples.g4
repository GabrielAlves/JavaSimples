grammar javaSimples;
import lexerJavaSimples;

/*
Estrutura básica:
programa: dec_de_func* main;
main: 'main' ':' dec_de_var comando* 'end';
etc
*/

programa: dec_de_var;

cabecalho_de_func: IDENTIFICADOR '(' lista_de_param_de_func ')' ':' (TIPO | 'void');
dec_de_func: cabecalho_de_func dec_de_var /* comando* */ 'end';
lista_de_param_de_func : TIPO IDENTIFICADOR (',' TIPO IDENTIFICADOR)*;

lista_de_var : IDENTIFICADOR (',' IDENTIFICADOR)*;
lista_de_var_com_atrib : IDENTIFICADOR '=' VALOR (',' IDENTIFICADOR '=' VALOR)*; // TODO: considerar EXPRESSAO(ex: valor = 10 + 20)
dec_de_var_nao_const : lista_de_var ':' TIPO;
dec_de_var_const : 'const' lista_de_var_com_atrib;
dec_de_var: 'var' ':' ((dec_de_var_nao_const | dec_de_var_const) ';')+;

comando: ;
// comando_if
// comando_while
comando_scanf: 'scanf' '(' lista_de_var ')' ';';