grammar javaSimples;
import lexerJavaSimples;

/*
Estrutura básica:
programa: dec_de_func* main;
main: 'main' ':' dec_de_var comando* 'end';
etc
*/

programa: comando; //

cabecalho_de_func: IDENTIFICADOR '(' lista_de_param_de_func ')' ':' TIPO;
dec_de_func: cabecalho_de_func dec_de_var /* comando* */ 'end';
lista_de_param_de_func : TIPO IDENTIFICADOR (',' TIPO IDENTIFICADOR)*;

lista_de_var_nao_const : IDENTIFICADOR (',' IDENTIFICADOR)*;
lista_de_var_const : IDENTIFICADOR '=' VALOR (',' IDENTIFICADOR '=' VALOR)*;
dec_de_var_nao_const : lista_de_var_nao_const ':' TIPO;
dec_de_var_const : 'const' lista_de_var_const;
dec_de_var: 'var' ':' (dec_de_var_nao_const | dec_de_var_const)+ ';';

comando: ;
// comando_if
// comando_while