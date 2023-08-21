from antlr4 import *
from gen.javaSimplesLexer import javaSimplesLexer
from gen.javaSimplesParser import javaSimplesParser
from gen.javaSimplesVisitor import javaSimplesVisitor
import logging

class MyVisitor(javaSimplesVisitor):
    def __init__(self, output_file):
        self.output_file = output_file
        self.jasmin_code = ""
        self.variablesTable = {}
        self.dict_variavel_valor = {}
        self.stack = []
        logging.basicConfig(level = logging.INFO)


    def save_jasmin_code(self):
        with open(self.output_file, "w") as file:
            file.write(self.jasmin_code)

    def carregaVariavel(self, identificador, tipo):
        temp_jasmin_code = ""
        if tipo == "int":
            temp_jasmin_code += f"iload {identificador}\n"
            self.stack.append(len(self.stack))
        elif tipo == "float":
            temp_jasmin_code += f"fload {identificador}\n"
            self.stack.append(len(self.stack))
        elif tipo == "str":
            temp_jasmin_code += f"aload {identificador}"
            self.stack.append(len(self.stack))
        else:
            temp_jasmin_code += f"iload {identificador}"
            self.stack.append(len(self.stack))
        return temp_jasmin_code

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
    #### Minhas Notas: Rever os returns, descobrir o que é pra retornar pras funções
    # Vendo todas as declarações de variaveis e constantes do codigo
    def visitDeclaracoes(self, ctx: javaSimplesParser.DeclaracoesContext):
        logging.debug("Iniciando Declarações...")
        temp_jasmin_code = ""
        temp_jasmin_code += f"; inicio das declaracoes\n"
        for declaracao in ctx.decl_de_var():
            temp_jasmin_code += self.visitDecl_de_var(declaracao)
        for declaracao in ctx.decl_de_const():
            self.visitDecl_de_const(declaracao)

        temp_jasmin_code += f"; fim das declaracoes\n"
        ############################ Debug
        self.jasmin_code = temp_jasmin_code
        return len(self.variablesTable), temp_jasmin_code

    # Visit a parse tree produced by javaSimplesParser#decl_de_var.
    def visitDecl_de_var(self, ctx: javaSimplesParser.Decl_de_varContext):
        logging.debug("Declarando Variaveis...")
        variable_names = ctx.lista_de_var().IDENTIFICADOR()
        data_type = ctx.TIPO().getText()
        temp_jasmin_code = ""

        for variable_name in variable_names:
            self.variablesTable[variable_name.getText()] = (len(self.variablesTable), data_type)
            if data_type == "int":
                temp_jasmin_code += f"ldc 0\n"
                
                temp_jasmin_code += f"istore {self.variablesTable[variable_name.getText()][0]}\n"
            elif data_type == "float":
                temp_jasmin_code += f"ldc 0\n"
                temp_jasmin_code += f"fstore {self.variablesTable[variable_name.getText()][0]}\n"
            elif data_type == "str":
                temp_jasmin_code += f'ldc ""\n'
                temp_jasmin_code += f"astore {self.variablesTable[variable_name.getText()][0]}\n"
            else:
                temp_jasmin_code += f'ldc 0\n'
                temp_jasmin_code += f"istore {self.variablesTable[variable_name.getText()][0]}\n"
            logging.debug(f"\tCriando Variavel-> {variable_name.getText()} do Tipo {data_type}")
        return temp_jasmin_code

    # Visit a parse tree produced by javaSimplesParser#decl_de_var_const.
    def visitDecl_de_const(self, ctx: javaSimplesParser.Decl_de_constContext):
        logging.debug("Declarando Constantes...")
        constant_names = ctx.IDENTIFICADOR()
        constants = ctx.VALOR_INT()
        if constants:
            for i in range(0, len(constant_names)):
                self.variablesTable[constant_names[i].getText()] = constants[i].getText()
                logging.debug(f"\tCriando Constante-> {constant_names[i]} : {constants[i].getText()}")
        constants = ctx.VALOR_FLOAT()
        if constants:
            for i in range(0, len(constant_names)):
                self.variablesTable[constant_names[i].getText()] = constants[i].getText()
                logging.debug(f"\tCriando Constante-> {constant_names[i]} : {constants[i].getText()}")
        constants = ctx.VALOR_STR()
        if constants:
            for i in range(0, len(constant_names)):
                self.variablesTable[constant_names[i].getText()] = constants[i].getText()
                logging.debug(f"\tCriando Constante-> {constant_names[i]} : {constants[i].getText()}")
        constants = ctx.VALOR_BOOL()
        if constants:
            for i in range(0, len(constant_names)):
                self.variablesTable[constant_names[i].getText()] = constants[i].getText()
                logging.debug(f"\tCriando Constante-> {constant_names[i]} : {constants[i].getText()}")

    # Visit a parse tree produced by javaSimplesParser#expressao.
    def visitExpressao(self, ctx: javaSimplesParser.ExpressaoContext):
        logging.debug("realizando expressão...")
        temp_jasmin_code = ""
        tipo_expressao = None
        if ctx.expr_aritimetica():
            tipo_expressao, temp_jasmin_code = self.visitExpr_aritimetica(ctx.expr_aritimetica())
        elif ctx.expr_relacional():
            tipo_expressao, temp_jasmin_code = self.visitExpr_relacional(ctx.expr_relacional())
        elif ctx.VALOR_STR():
            texto = ctx.VALOR_STR().getText()
            temp_jasmin_code += f'ldc "{texto}"\n'
            tipo_expressao = "str"
        elif ctx.chamada_funcao():
            tipo_expressao, temp_jasmin_code = self.visitChamada_funcao(ctx.chamada_funcao())
        self.jasmin_code += temp_jasmin_code
        return tipo_expressao, temp_jasmin_code

    # Visit a parse tree produced by javaSimplesParser#expr_aritimetica.
    def visitExpr_aritimetica(self, ctx: javaSimplesParser.Expr_aritimeticaContext):
        logging.debug("realizando expressão aritimetica...")
        temp_jasmin_code = ""
        if ctx.OPERADOR_ARIT_LVL_2() is not None:
            operador = ctx.OPERADOR_ARIT_LVL_2().getText()
            tipo_operando_esq = self.visitExpr_aritimetica(ctx.getChild(0))
            tipo_operando_dir = self.visitExpr_aritimetica(ctx.getChild(2))
            if operador == "*":
                if tipo_operando_esq == "float" or tipo_operando_dir == "float":
                    temp_jasmin_code += "fmult\n"
                    return "float", temp_jasmin_code
                else:
                    temp_jasmin_code += "imult\n"
                    return "int", temp_jasmin_code
            else:
                if tipo_operando_esq == "float" or tipo_operando_dir == "float":
                    temp_jasmin_code += "fdiv\n"
                    return "float", temp_jasmin_code
                else:
                    temp_jasmin_code += "idiv\n"
                    return "int", temp_jasmin_code
        elif ctx.OPERADOR_ARIT_LVL_1() is not None:
            operador = ctx.OPERADOR_ARIT_LVL_1().getText()
            tipo_operando_esq, op_esq_jasmin_code = self.visitExpr_aritimetica(ctx.getChild(0))
            tipo_operando_dir, op_dir_jasmin_code = self.visitExpr_aritimetica(ctx.getChild(2))

            # Adicionando o codigo jasmin do carregamento de operadores para o temp_jasmin_code
            temp_jasmin_code += op_esq_jasmin_code
            temp_jasmin_code += op_dir_jasmin_code

            if operador == "+":
                if tipo_operando_esq == "float" or tipo_operando_dir == "float":
                    temp_jasmin_code += "fadd\n"
                    return "float", temp_jasmin_code
                else:
                    temp_jasmin_code += "iadd\n"
                    return "int", temp_jasmin_code
            else:
                if tipo_operando_esq == "float" or tipo_operando_dir == "float":
                    temp_jasmin_code += "fsub\n"
                    return "float", temp_jasmin_code
                else:
                    temp_jasmin_code += "isub\n"
                    return "int", temp_jasmin_code
        else:
            return self.visitTermo_aritimetico(ctx.termo_aritimetico())

    # Visit a parse tree produced by javaSimplesParser#termo_aritimetico.
    def visitTermo_aritimetico(self, ctx: javaSimplesParser.Termo_aritimeticoContext):
        logging.debug("carregando valor...")
        temp_jasmin_code = ""
        if ctx.IDENTIFICADOR() is not None:
            identificador = ctx.IDENTIFICADOR().getText()
            variavel, tipo = self.variablesTable[identificador]
            temp_jasmin_code = self.carregaVariavel(variavel, tipo)
            return tipo, temp_jasmin_code
        elif ctx.VALOR_INT() is not None:
            valor = ctx.VALOR_INT().getText()
            temp_jasmin_code += f"ldc {valor}\n"
            return "int", temp_jasmin_code
        elif ctx.VALOR_FLOAT() is not None:
            valor = ctx.VALOR_FLOAT().getText()
            temp_jasmin_code += f"ldc {valor}\n"
            return "float", temp_jasmin_code
        else:  # Jasmin to do
            expr = self.visitExpr_aritimetica(ctx.expr_aritimetica())
            return expr

    # Visit a parse tree produced by javaSimplesParser#expr_relacional.
    def visitExpr_relacional(self, ctx: javaSimplesParser.Expr_relacionalContext):
        logging.debug("realizando expressão relacional...")
        temp_jasmin_code = ""
        if ctx.OPERADOR_RELACIONAL_LVL_2() is not None:
            operador = ctx.OPERADOR_RELACIONAL_LVL_2().getText()
            if ctx.getChild(0).getText() == "!":
                tipo, op_esq_jasmin_code = self.visitTermo_relacional(ctx.getChild(1))
                if ctx.getChild(3).getText() == "!":
                    tipo, op_dir_jasmin_code = self.visitTermo_relacional(ctx.getChild(4))
                else:
                    tipo, op_dir_jasmin_code = self.visitTermo_relacional(ctx.getChild(3))
            else:
                tipo, op_esq_jasmin_code = self.visitTermo_relacional(ctx.getChild(0))
                if ctx.getChild(2).getText() == "!":
                    tipo, op_dir_jasmin_code = self.visitTermo_relacional(ctx.getChild(3))
                else:
                    tipo, op_dir_jasmin_code = self.visitTermo_relacional(ctx.getChild(2))

            temp_jasmin_code += op_esq_jasmin_code
            temp_jasmin_code += op_dir_jasmin_code

            if operador == "==":
                temp_jasmin_code += f"if_icmpeq ;implementar labels\n"
            else:
                temp_jasmin_code += f"if_icmpne ;implementar labels\n"
            return "bool", temp_jasmin_code
        elif ctx.OPERADOR_RELACIONAL_LVL_1() is not None:
            operador = ctx.OPERADOR_RELACIONAL_LVL_1().getText()
            if ctx.getChild(0).getText() == "!":
                tipo, op_esq_jasmin_code = self.visitTermo_relacional(ctx.getChild(1))
                if ctx.getChild(3).getText() == "!":
                    tipo, op_dir_jasmin_code = self.visitTermo_relacional(ctx.getChild(4))
                else:
                    tipo, op_dir_jasmin_code = self.visitTermo_relacional(ctx.getChild(3))
            else:
                tipo, op_esq_jasmin_code = self.visitTermo_relacional(ctx.getChild(0))
                if ctx.getChild(2).getText() == "!":
                    tipo, op_dir_jasmin_code = self.visitTermo_relacional(ctx.getChild(3))
                else:
                    tipo, op_dir_jasmin_code = self.visitTermo_relacional(ctx.getChild(2))

            temp_jasmin_code += op_esq_jasmin_code
            temp_jasmin_code += op_dir_jasmin_code

            if operador == ">=":
                temp_jasmin_code += f"if_icmpge ;implementar labels\n"
            elif operador == "<=":
                temp_jasmin_code += f"if_icmple ;implementar labels\n"
            elif operador == ">":
                temp_jasmin_code += f"if_icmpgt ;implementar labels\n"
            else:
                temp_jasmin_code += f"if_icmplt ;implementar labels\n"
            return "bool", temp_jasmin_code
        else:
            return self.visitTermo_relacional(ctx.termo_relacional())

    # Visit a parse tree produced by javaSimplesParser#termo_relacional.
    def visitTermo_relacional(self, ctx: javaSimplesParser.Termo_relacionalContext):
        logging.debug("carregando valor booleano...")
        temp_jasmin_code = ""

        if ctx.IDENTIFICADOR() is not None:
            identificador = ctx.IDENTIFICADOR().getText()
            variavel, tipo = self.variablesTable[identificador]
            temp_jasmin_code = self.carregaVariavel(variavel, tipo)
            return "bool", temp_jasmin_code
        elif ctx.VALOR_INT() is not None:
            valor = ctx.VALOR_INT().getText()
            temp_jasmin_code += f"ldc {valor}\n"
            return "bool", temp_jasmin_code
        elif ctx.VALOR_FLOAT() is not None:
            valor = ctx.VALOR_FLOAT().getText()
            temp_jasmin_code += f"ldc {valor}\n"
            return "bool", temp_jasmin_code
        elif ctx.VALOR_BOOL() is not None:
            valor = ctx.VALOR_BOOL().getText()
            if valor == "true":
                temp_jasmin_code += f"ldc 1\n"
            else:
                temp_jasmin_code += f"ldc 0\n"
            return "bool", temp_jasmin_code
        else:  # Jasmin to do
            expr = self.visitExpr_relacional(ctx.expr_relacional())
            return expr

    #################################################################
    ######                     gabriel                         ######
    #################################################################
    # Visit a parse tree produced by javaSimplesParser#comando.
    def visitComando(self, ctx: javaSimplesParser.ComandoContext):

        return self.visitChildren(ctx)

    # Visit a parse tree produced by javaSimplesParser#comando_if.
    def visitComando_if(self, ctx: javaSimplesParser.Comando_ifContext):
        self.jasmin_code += "; Comando if\n"
        return self.visitChildren(ctx)

    # Visit a parse tree produced by javaSimplesParser#comando_while.
    def visitComando_while(self, ctx: javaSimplesParser.Comando_whileContext):
        self.jasmin_code += "; Comando while\n"
        return self.visitChildren(ctx)

    # Visit a parse tree produced by javaSimplesParser#comando_scanf.
    def visitComando_scanf(self, ctx: javaSimplesParser.Comando_scanfContext):
        self.jasmin_code += "; Comando scanf\n"
        return self.visitChildren(ctx)

    # Visit a parse tree produced by javaSimplesParser#comando_atrib.
    def visitComando_atrib(self, ctx: javaSimplesParser.Comando_atribContext):
        self.jasmin_code += "; Comando atrib\n"
        identificador = ctx.IDENTIFICADOR()
        pos_na_memoria = self.variablesTable[identificador.getText()][0]
        tipo = self.variablesTable[identificador.getText()][1]
        valor = self.resolver_expressao(ctx.expressao())
        print(valor)
        #print(self.teste)
        # self.jasmin_code += f"ldc {valor}"
        '''
        if tipo == "int":
            self.jasmin_code += f"istore {pos_na_memoria}"

        elif tipo == "str":
            self.jasmin_code += f"astore {pos_na_memoria}"

        elif tipo == "float":
            self.jasmin_code += f"fstore {pos_na_memoria}"

        elif tipo == "bool":
            self.jasmin_code += f"istore {pos_na_memoria}"
            '''
        return self.visitChildren(ctx)

    def resolver_expressao(self, ctx):
        logging.debug("realizando expressão...")
        print(ctx.getText())
        if ctx.expr_aritimetica():
            print(ctx.expr_aritimetica().getText())
            resultado = eval(ctx.expr_aritimetica().getText())
        elif ctx.expr_relacional():
            resultado = eval(ctx.expr_relacional().getText())
        elif ctx.VALOR_STR():
            resultado = ctx.VALOR_STR().getText()
        elif ctx.chamada_funcao():
            #resultado = self.visitChamada_funcao(ctx.chamada_funcao())
            pass

        return resultado

    def substituir_valores(self, expressao):
        expressao = expressao.split()
        for i in range(len(expressao)):
            token = expressao[i]

            if token in self.variablesTable:
                expressao[i] = self.variablesTable[token]


    # Visit a parse tree produced by javaSimplesParser#comando_print.
    def visitComando_print(self, ctx: javaSimplesParser.Comando_printContext):
        # TODO: Verificar o identificador a ser impresso existe
        self.jasmin_code += "; Comando print\n"
        print(ctx.getText())
        # teste = self.visit(ctx.lista_de_expressoes())
        # print(teste)
        return self.visitChildren(ctx)

    # Visit a parse tree produced by javaSimplesParser#comando_break.
    def visitComando_break(self, ctx: javaSimplesParser.Comando_breakContext):
        self.jasmin_code += "; Comando break\n"
        return self.visitChildren(ctx)

    # Visit a parse tree produced by javaSimplesParser#comando_return.
    def visitComando_return(self, ctx: javaSimplesParser.Comando_returnContext):
        self.jasmin_code += "; Comando return\n"
        return self.visitChildren(ctx)

    # Visit a parse tree produced by javaSimplesParser#chamada_funcao.
    def visitChamada_funcao(self, ctx: javaSimplesParser.Chamada_funcaoContext):
        self.jasmin_code += "; Comando funcao\n"
        return self.visitChildren(ctx)


if __name__ == '__main__':
    # Ler o arquivo de entrada
    input_stream = FileStream('./testes_entrada/funcao_testes_do_daniel.txt')
    # print(input_stream)
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
    visitor.save_jasmin_code()
