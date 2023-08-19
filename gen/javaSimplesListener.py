# Generated from C:/Users/Gabriel/PycharmProjects/JavaSimples\javaSimples.g4 by ANTLR 4.12.0
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .javaSimplesParser import javaSimplesParser
else:
    from javaSimplesParser import javaSimplesParser

# This class defines a complete listener for a parse tree produced by javaSimplesParser.
class javaSimplesListener(ParseTreeListener):

    # Enter a parse tree produced by javaSimplesParser#programa.
    def enterPrograma(self, ctx:javaSimplesParser.ProgramaContext):
        pass

    # Exit a parse tree produced by javaSimplesParser#programa.
    def exitPrograma(self, ctx:javaSimplesParser.ProgramaContext):
        pass


    # Enter a parse tree produced by javaSimplesParser#funcao_main.
    def enterFuncao_main(self, ctx:javaSimplesParser.Funcao_mainContext):
        pass

    # Exit a parse tree produced by javaSimplesParser#funcao_main.
    def exitFuncao_main(self, ctx:javaSimplesParser.Funcao_mainContext):
        pass


    # Enter a parse tree produced by javaSimplesParser#dec_de_func.
    def enterDec_de_func(self, ctx:javaSimplesParser.Dec_de_funcContext):
        pass

    # Exit a parse tree produced by javaSimplesParser#dec_de_func.
    def exitDec_de_func(self, ctx:javaSimplesParser.Dec_de_funcContext):
        pass


    # Enter a parse tree produced by javaSimplesParser#cabecalho_de_func.
    def enterCabecalho_de_func(self, ctx:javaSimplesParser.Cabecalho_de_funcContext):
        pass

    # Exit a parse tree produced by javaSimplesParser#cabecalho_de_func.
    def exitCabecalho_de_func(self, ctx:javaSimplesParser.Cabecalho_de_funcContext):
        pass


    # Enter a parse tree produced by javaSimplesParser#lista_de_parametros.
    def enterLista_de_parametros(self, ctx:javaSimplesParser.Lista_de_parametrosContext):
        pass

    # Exit a parse tree produced by javaSimplesParser#lista_de_parametros.
    def exitLista_de_parametros(self, ctx:javaSimplesParser.Lista_de_parametrosContext):
        pass


    # Enter a parse tree produced by javaSimplesParser#parametro.
    def enterParametro(self, ctx:javaSimplesParser.ParametroContext):
        pass

    # Exit a parse tree produced by javaSimplesParser#parametro.
    def exitParametro(self, ctx:javaSimplesParser.ParametroContext):
        pass


    # Enter a parse tree produced by javaSimplesParser#decl_de_variaveis.
    def enterDecl_de_variaveis(self, ctx:javaSimplesParser.Decl_de_variaveisContext):
        pass

    # Exit a parse tree produced by javaSimplesParser#decl_de_variaveis.
    def exitDecl_de_variaveis(self, ctx:javaSimplesParser.Decl_de_variaveisContext):
        pass


    # Enter a parse tree produced by javaSimplesParser#decl_de_var.
    def enterDecl_de_var(self, ctx:javaSimplesParser.Decl_de_varContext):
        pass

    # Exit a parse tree produced by javaSimplesParser#decl_de_var.
    def exitDecl_de_var(self, ctx:javaSimplesParser.Decl_de_varContext):
        pass


    # Enter a parse tree produced by javaSimplesParser#decl_de_var_const.
    def enterDecl_de_var_const(self, ctx:javaSimplesParser.Decl_de_var_constContext):
        pass

    # Exit a parse tree produced by javaSimplesParser#decl_de_var_const.
    def exitDecl_de_var_const(self, ctx:javaSimplesParser.Decl_de_var_constContext):
        pass


    # Enter a parse tree produced by javaSimplesParser#lista_de_var.
    def enterLista_de_var(self, ctx:javaSimplesParser.Lista_de_varContext):
        pass

    # Exit a parse tree produced by javaSimplesParser#lista_de_var.
    def exitLista_de_var(self, ctx:javaSimplesParser.Lista_de_varContext):
        pass


    # Enter a parse tree produced by javaSimplesParser#lista_de_atribuicao.
    def enterLista_de_atribuicao(self, ctx:javaSimplesParser.Lista_de_atribuicaoContext):
        pass

    # Exit a parse tree produced by javaSimplesParser#lista_de_atribuicao.
    def exitLista_de_atribuicao(self, ctx:javaSimplesParser.Lista_de_atribuicaoContext):
        pass


    # Enter a parse tree produced by javaSimplesParser#lista_de_expressoes.
    def enterLista_de_expressoes(self, ctx:javaSimplesParser.Lista_de_expressoesContext):
        pass

    # Exit a parse tree produced by javaSimplesParser#lista_de_expressoes.
    def exitLista_de_expressoes(self, ctx:javaSimplesParser.Lista_de_expressoesContext):
        pass


    # Enter a parse tree produced by javaSimplesParser#expressao.
    def enterExpressao(self, ctx:javaSimplesParser.ExpressaoContext):
        pass

    # Exit a parse tree produced by javaSimplesParser#expressao.
    def exitExpressao(self, ctx:javaSimplesParser.ExpressaoContext):
        pass


    # Enter a parse tree produced by javaSimplesParser#expr_aritimetica.
    def enterExpr_aritimetica(self, ctx:javaSimplesParser.Expr_aritimeticaContext):
        pass

    # Exit a parse tree produced by javaSimplesParser#expr_aritimetica.
    def exitExpr_aritimetica(self, ctx:javaSimplesParser.Expr_aritimeticaContext):
        pass


    # Enter a parse tree produced by javaSimplesParser#termo_aritimetico.
    def enterTermo_aritimetico(self, ctx:javaSimplesParser.Termo_aritimeticoContext):
        pass

    # Exit a parse tree produced by javaSimplesParser#termo_aritimetico.
    def exitTermo_aritimetico(self, ctx:javaSimplesParser.Termo_aritimeticoContext):
        pass


    # Enter a parse tree produced by javaSimplesParser#expr_relacional.
    def enterExpr_relacional(self, ctx:javaSimplesParser.Expr_relacionalContext):
        pass

    # Exit a parse tree produced by javaSimplesParser#expr_relacional.
    def exitExpr_relacional(self, ctx:javaSimplesParser.Expr_relacionalContext):
        pass


    # Enter a parse tree produced by javaSimplesParser#termo_relacional.
    def enterTermo_relacional(self, ctx:javaSimplesParser.Termo_relacionalContext):
        pass

    # Exit a parse tree produced by javaSimplesParser#termo_relacional.
    def exitTermo_relacional(self, ctx:javaSimplesParser.Termo_relacionalContext):
        pass


    # Enter a parse tree produced by javaSimplesParser#comando.
    def enterComando(self, ctx:javaSimplesParser.ComandoContext):
        pass

    # Exit a parse tree produced by javaSimplesParser#comando.
    def exitComando(self, ctx:javaSimplesParser.ComandoContext):
        pass


    # Enter a parse tree produced by javaSimplesParser#comando_if.
    def enterComando_if(self, ctx:javaSimplesParser.Comando_ifContext):
        pass

    # Exit a parse tree produced by javaSimplesParser#comando_if.
    def exitComando_if(self, ctx:javaSimplesParser.Comando_ifContext):
        pass


    # Enter a parse tree produced by javaSimplesParser#comando_while.
    def enterComando_while(self, ctx:javaSimplesParser.Comando_whileContext):
        pass

    # Exit a parse tree produced by javaSimplesParser#comando_while.
    def exitComando_while(self, ctx:javaSimplesParser.Comando_whileContext):
        pass


    # Enter a parse tree produced by javaSimplesParser#comando_scanf.
    def enterComando_scanf(self, ctx:javaSimplesParser.Comando_scanfContext):
        pass

    # Exit a parse tree produced by javaSimplesParser#comando_scanf.
    def exitComando_scanf(self, ctx:javaSimplesParser.Comando_scanfContext):
        pass


    # Enter a parse tree produced by javaSimplesParser#comando_atrib.
    def enterComando_atrib(self, ctx:javaSimplesParser.Comando_atribContext):
        pass

    # Exit a parse tree produced by javaSimplesParser#comando_atrib.
    def exitComando_atrib(self, ctx:javaSimplesParser.Comando_atribContext):
        pass


    # Enter a parse tree produced by javaSimplesParser#comando_print.
    def enterComando_print(self, ctx:javaSimplesParser.Comando_printContext):
        pass

    # Exit a parse tree produced by javaSimplesParser#comando_print.
    def exitComando_print(self, ctx:javaSimplesParser.Comando_printContext):
        pass


    # Enter a parse tree produced by javaSimplesParser#comando_break.
    def enterComando_break(self, ctx:javaSimplesParser.Comando_breakContext):
        pass

    # Exit a parse tree produced by javaSimplesParser#comando_break.
    def exitComando_break(self, ctx:javaSimplesParser.Comando_breakContext):
        pass


    # Enter a parse tree produced by javaSimplesParser#comando_return.
    def enterComando_return(self, ctx:javaSimplesParser.Comando_returnContext):
        pass

    # Exit a parse tree produced by javaSimplesParser#comando_return.
    def exitComando_return(self, ctx:javaSimplesParser.Comando_returnContext):
        pass


    # Enter a parse tree produced by javaSimplesParser#chamada_funcao.
    def enterChamada_funcao(self, ctx:javaSimplesParser.Chamada_funcaoContext):
        pass

    # Exit a parse tree produced by javaSimplesParser#chamada_funcao.
    def exitChamada_funcao(self, ctx:javaSimplesParser.Chamada_funcaoContext):
        pass



del javaSimplesParser