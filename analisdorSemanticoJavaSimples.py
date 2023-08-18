from antlr4 import *
from gen.javaSimplesLexer import javaSimplesLexer
from gen.javaSimplesParser import *
from gen.javaSimplesVisitor import javaSimplesVisitor


class MyVisitor(javaSimplesVisitor):
    def __init__(self, output_file):
        self.output_file = output_file
        self.jasmin_code = ""
        self.variablesTable = {}

    def save_jasmin_code(self):
        with open(self.output_file, "w") as file:
            file.write(self.jasmin_code)

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
    # Vendo todas as declarações de variaveis e constantes do codigo
    def visitDecl_de_variaveis(self, ctx: javaSimplesParser.Decl_de_variaveisContext):
        self.jasmin_code += "; Declaracao variaveis\n"

        for decl_de_var in ctx.decl_de_var():
            self.visitDecl_de_var(decl_de_var)
        for decl_de_var_const in ctx.decl_de_var_const():
            self.visitDecl_de_var_const(decl_de_var_const)

        jasmin_instruction = f""

    # Visit a parse tree produced by javaSimplesParser#decl_de_var.
    def visitDecl_de_var(self, ctx: javaSimplesParser.Decl_de_varContext):
        self.jasmin_code += "; Declaracao de variavel\n"
        variable_names = ctx.lista_de_var().IDENTIFICADOR()
        data_type = ctx.TIPO().getText()

        for variable_name in variable_names:
            self.variablesTable[len(self.variablesTable)] = (variable_name, data_type)
        return self.visitChildren(ctx)

    # Visit a parse tree produced by javaSimplesParser#decl_de_var_const.
    def visitDecl_de_var_const(self, ctx: javaSimplesParser.Decl_de_var_constContext):
        self.jasmin_code += "; declaracao de constantes\n"

        for atribuicao in ctx.lista_de_atribuicao():
            self.visitLista_de_atribuicao(atribuicao)

    # Visit a parse tree produced by javaSimplesParser#lista_de_var.
    def visitLista_de_var(self, ctx: javaSimplesParser.Lista_de_varContext):
        self.jasmin_code += "; lista de variaveis\n"
        return self.visitChildren(ctx)

    # Visit a parse tree produced by javaSimplesParser#lista_de_atribuicao.
    def visitLista_de_atribuicao(self, ctx: javaSimplesParser.Lista_de_atribuicaoContext):
        self.jasmin_code += "; lista de atribuicao\n"
        variable_name = ctx.IDENTIFICADOR()
        expressao = self.visitExpressao(ctx.expressao())
        self.variablesTable[variable_name] = expressao

    # Visit a parse tree produced by javaSimplesParser#lista_de_expressoes.
    def visitLista_de_expressoes(self, ctx: javaSimplesParser.Lista_de_expressoesContext):
        self.jasmin_code += "; lista de expressoes\n"
        return self.visitChildren(ctx)

    # Visit a parse tree produced by javaSimplesParser#expressao.
    def visitExpressao(self, ctx: javaSimplesParser.ExpressaoContext):
        self.jasmin_code += "; Expressao\n"
        expressao = None
        if ctx.expr_aritimetica():
            expressao = self.visitExpr_aritimetica(ctx.expr_aritimetica())
        elif ctx.expr_relacional():
            expressao = self.visitExpr_relacional(ctx.expr_relacional())
        elif ctx.VALOR_STR():
            expressao = ctx.VALOR_STR().getText()
        elif ctx.chamada_funcao():
            expressao = self.visitChamada_funcao(ctx.chamada_funcao())
        return expressao

    # Visit a parse tree produced by javaSimplesParser#expr_aritimetica.
    def visitExpr_aritimetica(self, ctx: javaSimplesParser.Expr_aritimeticaContext):
        self.jasmin_code += "; expressao aritimetica\n"
        if ctx.OPERADOR_ARIT_LVL_2() is not None:
            operador = ctx.OPERADOR_ARIT_LVL_2()
            operando_esq = 1
            operando_dir = 0
            if operador == "*":
                return operando_esq * operando_dir
            else:
                return operando_esq / operando_dir
        elif ctx.OPERADOR_ARIT_LVL_1() is not None:
            operador = ctx.OPERADOR_ARIT_LVL_1()
            operando_esq = 1
            operando_dir = 0
            if operador == "+":
                return operando_esq + operando_dir
            else:
                return operando_esq - operando_dir
        else:
            return self.visitTermo_aritimetico(ctx.termo_aritimetico())

    # Visit a parse tree produced by javaSimplesParser#termo_aritimetico.
    def visitTermo_aritimetico(self, ctx: javaSimplesParser.Termo_aritimeticoContext):
        self.jasmin_code += "; termo aritimetico\n"
        return self.visitChildren(ctx)

    # Visit a parse tree produced by javaSimplesParser#expr_relacional.
    def visitExpr_relacional(self, ctx: javaSimplesParser.Expr_relacionalContext):
        self.jasmin_code += "; expressao relacional\n"
        return self.visitChildren(ctx)

    # Visit a parse tree produced by javaSimplesParser#termo_relacional.
    def visitTermo_relacional(self, ctx: javaSimplesParser.Termo_relacionalContext):
        self.jasmin_code += "; termo relacional\n"
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


if __name__ == '__main__':
    # Ler o arquivo de entrada
    input_stream = FileStream('input.txt')

    # Criar o lexer
    lexer = javaSimplesLexer(input_stream)

    # Criar o stream de tokens
    token_stream = CommonTokenStream(lexer)

    # Criar o parser
    parser = javaSimplesParser(token_stream)

    # Obter a árvore de análise sintática
    tree = parser.programa()

    # Criar o visitor
    visitor = MyVisitor("Output.j")

    # Visitar a árvore de análise sintática
    visitor.visit(tree)
