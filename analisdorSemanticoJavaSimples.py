from antlr4 import *
from gen.javaSimplesLexer import javaSimplesLexer
from gen.javaSimplesParser import *


class JavaSimplesVisitor(ParseTreeVisitor):
    #################################################################
    ######                     Ingrid                          ######
    #################################################################
    # Visit a parse tree produced by javaSimplesParser#programa.
    def visitPrograma(self, ctx: javaSimplesParser.ProgramaContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by javaSimplesParser#funcao_main.
    def visitFuncao_main(self, ctx: javaSimplesParser.Funcao_mainContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by javaSimplesParser#dec_de_func.
    def visitDec_de_func(self, ctx: javaSimplesParser.Dec_de_funcContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by javaSimplesParser#cabecalho_de_func.
    def visitCabecalho_de_func(self, ctx: javaSimplesParser.Cabecalho_de_funcContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by javaSimplesParser#lista_de_parametros.
    def visitLista_de_parametros(self, ctx: javaSimplesParser.Lista_de_parametrosContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by javaSimplesParser#parametro.
    def visitParametro(self, ctx: javaSimplesParser.ParametroContext):
        return self.visitChildren(ctx)

    #################################################################
    ######                     Daniel                          ######
    #################################################################
    # Visit a parse tree produced by javaSimplesParser#decl_de_variaveis.
    def visitDecl_de_variaveis(self, ctx: javaSimplesParser.Decl_de_variaveisContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by javaSimplesParser#decl_de_var.
    def visitDecl_de_var(self, ctx: javaSimplesParser.Decl_de_varContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by javaSimplesParser#decl_de_var_const.
    def visitDecl_de_var_const(self, ctx: javaSimplesParser.Decl_de_var_constContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by javaSimplesParser#lista_de_var.
    def visitLista_de_var(self, ctx: javaSimplesParser.Lista_de_varContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by javaSimplesParser#lista_de_atribuicao.
    def visitLista_de_atribuicao(self, ctx: javaSimplesParser.Lista_de_atribuicaoContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by javaSimplesParser#lista_de_expressoes.
    def visitLista_de_expressoes(self, ctx: javaSimplesParser.Lista_de_expressoesContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by javaSimplesParser#expressao.
    def visitExpressao(self, ctx: javaSimplesParser.ExpressaoContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by javaSimplesParser#expr_aritimetica.
    def visitExpr_aritimetica(self, ctx: javaSimplesParser.Expr_aritimeticaContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by javaSimplesParser#termo_aritimetico.
    def visitTermo_aritimetico(self, ctx: javaSimplesParser.Termo_aritimeticoContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by javaSimplesParser#expr_relacional.
    def visitExpr_relacional(self, ctx: javaSimplesParser.Expr_relacionalContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by javaSimplesParser#termo_relacional.
    def visitTermo_relacional(self, ctx: javaSimplesParser.Termo_relacionalContext):
        return self.visitChildren(ctx)

    #################################################################
    ######                     gabriel                         ######
    #################################################################
    # Visit a parse tree produced by javaSimplesParser#comando.
    def visitComando(self, ctx: javaSimplesParser.ComandoContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by javaSimplesParser#comando_if.
    def visitComando_if(self, ctx: javaSimplesParser.Comando_ifContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by javaSimplesParser#comando_while.
    def visitComando_while(self, ctx: javaSimplesParser.Comando_whileContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by javaSimplesParser#comando_scanf.
    def visitComando_scanf(self, ctx: javaSimplesParser.Comando_scanfContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by javaSimplesParser#comando_atrib.
    def visitComando_atrib(self, ctx: javaSimplesParser.Comando_atribContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by javaSimplesParser#comando_print.
    def visitComando_print(self, ctx: javaSimplesParser.Comando_printContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by javaSimplesParser#comando_break.
    def visitComando_break(self, ctx: javaSimplesParser.Comando_breakContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by javaSimplesParser#comando_return.
    def visitComando_return(self, ctx: javaSimplesParser.Comando_returnContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by javaSimplesParser#chamada_funcao.
    def visitChamada_funcao(self, ctx: javaSimplesParser.Chamada_funcaoContext):
        return self.visitChildren(ctx)


def main():
    input_stream = InputStream("3 + 4 - 2")

    # lexer vai receber o comando
    # lexer = javaSimplesLexer(input_stream)
    # separa em tokens
    # tokens = CommonTokenStream(lexer)
    # cria um parser com os tokens
    # parser = javaSimplesParser(tokens)

    # cria uma arvore
    # tree = parser.start()
    visitor = JavaSimplesVisitor()
    # analisa o codigo
    # jasmin_code = visitor.visit(tree)

    # print(jasmin_code)


if __name__ == '__main__':
    main()
