from antlr4 import *
from gen.javaSimplesLexer import javaSimplesLexer
from gen.javaSimplesParser import javaSimplesParser
from gen.javaSimplesVisitor import javaSimplesVisitor
import logging
import sys

class MyVisitor(javaSimplesVisitor):
    def __init__(self, nome_do_programa):
        self.nome_do_programa = nome_do_programa
        self.jasmin_code = ""
        self.variablesTable = {}
        self.dict_variavel_valor = {}
        logging.basicConfig(level=logging.DEBUG)
        self.stack = [1]
        self.higher_stack_size = 1
        self.palavras_reservadas = javaSimplesLexer.literalNames  # Variáveis não podem usar esses nomes

    def save_jasmin_code(self):
        with open(self.nome_do_programa, "w") as file:
            file.write(self.jasmin_code)

    def atualiza_pilha(self, operacao):
        if operacao == "pop":
            self.stack.pop()
        else:
            self.stack.append(1)
            if len(self.stack) > self.higher_stack_size:
                self.higher_stack_size = len(self.stack)

    def conta_variaveis(self):
        count = 0
        for key in self.variablesTable:
            if isinstance(self.variablesTable[key], tuple):
                count += 1
        return count

    def carregaVariavel(self, identificador, tipo):
        temp_jasmin_code = ""
        if tipo == "int":
            temp_jasmin_code += f"\tiload {identificador}\n"
            self.atualiza_pilha("append")
        elif tipo == "float":
            temp_jasmin_code += f"\tfload {identificador}\n"
            self.atualiza_pilha("append")
        elif tipo == "str":
            temp_jasmin_code += f"\taload {identificador}"
            self.atualiza_pilha("append")
        else:
            temp_jasmin_code += f"\tiload {identificador}"
            self.atualiza_pilha("append")
        return temp_jasmin_code

    def adicionar_funcoes_de_leitura_no_codigo_jasmin(self):
        self.adicionar_funcao_ler_inteiro_no_codigo()
        self.jasmin_code += "\n\n"

    def adicionar_funcao_ler_inteiro_no_codigo(self):
        self.jasmin_code += '''.method public static lerInteiro()I
   .limit stack 3
   .limit locals 1

   new java/util/Scanner
   dup
   getstatic java/lang/System/in Ljava/io/InputStream;
   invokespecial java/util/Scanner/<init>(Ljava/io/InputStream;)V
   invokevirtual java/util/Scanner/nextInt()I ; usa o nextInt do Scanner
   ireturn
.end method'''

    #################################################################
    ######                     Ingrid                          ######
    #################################################################
    # Visit a parse tree produced by javaSimplesParser#programa.
    def visitPrograma(self, ctx: javaSimplesParser.ProgramaContext):
        logging.debug("Iniciando analise do codigo...")
        self.jasmin_code += f".class public {self.nome_do_programa}\n"
        self.jasmin_code += f".super java/lang/Object\n\n"
        return self.visitChildren(ctx)

    # Visit a parse tree produced by javaSimplesParser#funcao_main.
    def visitFuncao_main(self, ctx: javaSimplesParser.Funcao_mainContext):
        logging.debug("Criando a Main...")
        n_variaveis = 1
        decl_jasmin_code = ""
        comando_jasmin_code = ""
        self.adicionar_funcoes_de_leitura_no_codigo_jasmin()
        self.jasmin_code += f".method public static main([Ljava/lang/String;)V\n"
        if ctx.declaracoes():
            decl_jasmin_code = self.visitDeclaracoes(ctx.declaracoes())
            n_variaveis = self.conta_variaveis()
        if ctx.comando():
            for comando in ctx.comando():
                comando_jasmin_code += self.visitComando(comando)
        self.jasmin_code += f"\t.limit stack {self.higher_stack_size}\n"
        self.jasmin_code += f"\t.limit locals {n_variaveis}\n"
        self.jasmin_code += decl_jasmin_code
        self.jasmin_code += comando_jasmin_code
        self.jasmin_code += f".end method"
        self.variablesTable = {}
        self.stack = [1]
        self.higher_stack_size = 1

    # Visit a parse tree produced by javaSimplesParser#dec_de_func.
    def visitDec_de_func(self, ctx: javaSimplesParser.Dec_de_funcContext):
        logging.debug("Começando a declaração de função...")
        n_variaveis = 1
        decl_jasmin_code = ""
        comando_jasmin_code = ""
        cabc_da_funcao = self.visitCabecalho_de_func(ctx.cabecalho_de_func())
        if ctx.declaracoes():
            decl_jasmin_code = self.visitDeclaracoes(ctx.declaracoes())
            n_variaveis = self.conta_variaveis()
        if ctx.comando():
            # comando_jasmin_code = self.visitComando(ctx.comando())
            for comando in ctx.comando():
                self.visitComando(comando)

        self.jasmin_code += cabc_da_funcao
        self.jasmin_code += f"\t.limit stack {self.higher_stack_size}\n"
        self.jasmin_code += f"\t.limit locals {n_variaveis}\n"
        self.jasmin_code += decl_jasmin_code
        self.jasmin_code += comando_jasmin_code
        self.jasmin_code += f".end method\n"

        logging.debug("Terminando a declaração de função...")
        self.variablesTable = {}
        self.stack = [1]
        self.higher_stack_size = 1

    # Visit a parse tree produced by javaSimplesParser#cabecalho_de_func.
    def visitCabecalho_de_func(self, ctx: javaSimplesParser.Cabecalho_de_funcContext):
        nome_funcao = ctx.IDENTIFICADOR().getText()
        parametros_da_funcao = self.visitLista_de_parametros(ctx.lista_de_parametros())
        temp_jasmin_code = ""

        if ctx.TIPO().getText() == "int":
            temp_jasmin_code += f".method public static {nome_funcao}({parametros_da_funcao})I\n"
        elif ctx.TIPO().getText() == "float":
            temp_jasmin_code += f".method public static {nome_funcao}({parametros_da_funcao})F\n"
        elif ctx.TIPO().getText() == "str":
            temp_jasmin_code += f".method public static {nome_funcao}({parametros_da_funcao})Ljava/lang/String\n"
        elif ctx.TIPO().getText() == "bool":
            temp_jasmin_code += f".method public static {nome_funcao}({parametros_da_funcao})I\n"
        else:
            temp_jasmin_code += f".method public static {nome_funcao}({parametros_da_funcao})V\n"

        return temp_jasmin_code

    # Visit a parse tree produced by javaSimplesParser#lista_de_parametros.
    def visitLista_de_parametros(self, ctx: javaSimplesParser.Lista_de_parametrosContext):
        temp_jasmin_code = ""
        logging.debug("Recebendo Parametros...")
        for parametro in ctx.parametro():
            temp_jasmin_code += self.visitParametro(parametro)

        return temp_jasmin_code

    # Visit a parse tree produced by javaSimplesParser#parametro.
    def visitParametro(self, ctx: javaSimplesParser.ParametroContext):
        temp_jasmin_code = ""
        tipo = ctx.TIPO().getText()
        if tipo == "int":
            temp_jasmin_code += f"I"
        elif tipo == "float":
            temp_jasmin_code += f"F"
        elif tipo == "str":
            temp_jasmin_code += f"Ljava/lang/String"
        elif tipo == "bool":
            temp_jasmin_code += f"I"
        logging.debug(f"\tParametro -> {ctx.IDENTIFICADOR().getText()} do tipo {tipo}")
        self.variablesTable[ctx.IDENTIFICADOR().getText()] = (len(self.variablesTable), tipo)

        return temp_jasmin_code

    #################################################################
    ######                     Daniel                          ######
    #################################################################
    #### Minhas Notas: Rever os returns, descobrir o que é pra retornar pras funções
    # Vendo todas as declarações de variaveis e constantes do codigo
    def visitDeclaracoes(self, ctx: javaSimplesParser.DeclaracoesContext):
        # logging.debug("Iniciando Declarações...")
        temp_jasmin_code = ""
        temp_jasmin_code += f"\t; inicio das declaracoes\n"
        for declaracao in ctx.decl_de_var():
            temp_jasmin_code += self.visitDecl_de_var(declaracao)
        for declaracao in ctx.decl_de_const():
            self.visitDecl_de_const(declaracao)

        temp_jasmin_code += f"\t; fim das declaracoes\n"
        return temp_jasmin_code

    # Visit a parse tree produced by javaSimplesParser#decl_de_var.
    def visitDecl_de_var(self, ctx: javaSimplesParser.Decl_de_varContext):
        logging.debug("Declarando Variaveis...")
        variable_names = ctx.lista_de_var().IDENTIFICADOR()
        data_type = ctx.TIPO().getText()
        temp_jasmin_code = ""

        for variable_name in variable_names:
            if variable_name.getText() in self.variablesTable:
                linha = ctx.start.line
                logging.debug(f"Erro na linha {linha}, variavel já declarada")
                exit(1)
            else:
                self.variablesTable[variable_name.getText()] = (len(self.variablesTable), data_type)
                if data_type == "int":
                    temp_jasmin_code += f"\tldc 0\n"
                    temp_jasmin_code += f"\tistore {self.variablesTable[variable_name.getText()][0]}\n"
                elif data_type == "float":
                    temp_jasmin_code += f"\tldc 0\n"
                    temp_jasmin_code += f"\tfstore {self.variablesTable[variable_name.getText()][0]}\n"
                elif data_type == "str":
                    temp_jasmin_code += f'\tldc ""\n'
                    temp_jasmin_code += f"\tastore {self.variablesTable[variable_name.getText()][0]}\n"
                else:
                    temp_jasmin_code += f'\tldc 0\n'
                    temp_jasmin_code += f"\tistore {self.variablesTable[variable_name.getText()][0]}\n"
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
            temp_jasmin_code += f'\tldc "{texto}"\n'
            self.atualiza_pilha("append")
            tipo_expressao = "str"
        elif ctx.chamada_funcao():
            tipo_expressao, temp_jasmin_code = self.visitChamada_funcao(ctx.chamada_funcao())
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
                    temp_jasmin_code += "\tfmult\n"
                    self.atualiza_pilha("pop")
                    return "float", temp_jasmin_code
                else:
                    temp_jasmin_code += "\timult\n"
                    self.atualiza_pilha("pop")
                    return "int", temp_jasmin_code
            else:
                if tipo_operando_esq == "float" or tipo_operando_dir == "float":
                    temp_jasmin_code += "\tfdiv\n"
                    self.atualiza_pilha("pop")
                    return "float", temp_jasmin_code
                else:
                    temp_jasmin_code += "\tidiv\n"
                    self.atualiza_pilha("pop")
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
                    temp_jasmin_code += "\tfadd\n"
                    self.atualiza_pilha("pop")
                    return "float", temp_jasmin_code
                else:
                    temp_jasmin_code += "\tiadd\n"
                    self.atualiza_pilha("pop")
                    return "int", temp_jasmin_code
            else:
                if tipo_operando_esq == "float" or tipo_operando_dir == "float":
                    temp_jasmin_code += "\tfsub\n"
                    self.atualiza_pilha("pop")
                    return "float", temp_jasmin_code
                else:
                    temp_jasmin_code += "\tisub\n"
                    self.atualiza_pilha("pop")
                    return "int", temp_jasmin_code
        else:
            return self.visitTermo_aritimetico(ctx.termo_aritimetico())

    # Visit a parse tree produced by javaSimplesParser#termo_aritimetico.
    def visitTermo_aritimetico(self, ctx: javaSimplesParser.Termo_aritimeticoContext):
        logging.debug("carregando valor...")
        temp_jasmin_code = ""
        if ctx.IDENTIFICADOR() is not None:
            identificador = ctx.IDENTIFICADOR().getText()

            if identificador not in self.variablesTable:
                linha = ctx.start.line
                logging.debug(f"Erro: na linha: {linha}. O identificador \"{identificador}\" não existe")
                exit(1)

            variavel, tipo = self.variablesTable[identificador]
            temp_jasmin_code = self.carregaVariavel(variavel, tipo)
            return tipo, temp_jasmin_code
        elif ctx.VALOR_INT() is not None:
            valor = ctx.VALOR_INT().getText()
            temp_jasmin_code += f"\tldc {valor}\n"
            self.atualiza_pilha("append")
            return "int", temp_jasmin_code
        elif ctx.VALOR_FLOAT() is not None:
            valor = ctx.VALOR_FLOAT().getText()
            temp_jasmin_code += f"\tldc {valor}\n"
            self.atualiza_pilha("append")
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
                self.atualiza_pilha("pop")
            else:
                temp_jasmin_code += f"if_icmpne ;implementar labels\n"
                self.atualiza_pilha("pop")
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
                self.atualiza_pilha("pop")
            elif operador == "<=":
                temp_jasmin_code += f"if_icmple ;implementar labels\n"
                self.atualiza_pilha("pop")
            elif operador == ">":
                temp_jasmin_code += f"if_icmpgt ;implementar labels\n"
                self.atualiza_pilha("pop")
            else:
                temp_jasmin_code += f"if_icmplt ;implementar labels\n"
                self.atualiza_pilha("pop")
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
            self.atualiza_pilha("append")
            return "bool", temp_jasmin_code
        elif ctx.VALOR_FLOAT() is not None:
            valor = ctx.VALOR_FLOAT().getText()
            temp_jasmin_code += f"ldc {valor}\n"
            self.atualiza_pilha("append")
            return "bool", temp_jasmin_code
        elif ctx.VALOR_BOOL() is not None:
            valor = ctx.VALOR_BOOL().getText()
            if valor == "true":
                temp_jasmin_code += f"ldc 1\n"
                self.atualiza_pilha("append")
            else:
                temp_jasmin_code += f"ldc 0\n"
                self.atualiza_pilha("append")
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
        temp_jasmin_code = "; Comando scanf\n"

        for identificador in ctx.lista_de_var().IDENTIFICADOR():
            identificador = identificador.getText()
            if identificador not in self.variablesTable:
                logging.debug(f"Erro: variável \"{identificador}\" não existe")
                exit(1)

            pos_na_memoria = self.variablesTable[identificador][0]
            tipo_da_variavel = self.variablesTable[identificador][1]

            if tipo_da_variavel == "int":
                temp_jasmin_code += f"\tinvokestatic {self.nome_do_programa}/lerInteiro()I\n"
                temp_jasmin_code += f"\tistore {pos_na_memoria}\n"

            elif tipo_da_variavel == "float":
                pass

            elif tipo_da_variavel == "bool":
                pass

            elif tipo_da_variavel == "str":
                pass

        return temp_jasmin_code

    # Visit a parse tree produced by javaSimplesParser#comando_atrib.
    def visitComando_atrib(self, ctx: javaSimplesParser.Comando_atribContext):
        temp_jasmin_code = "\t; Comando atrib\n"
        identificador = ctx.IDENTIFICADOR()
        pos_na_memoria = self.variablesTable[identificador.getText()][0]
        tipo_da_variavel = self.variablesTable[identificador.getText()][1]
        tipo_da_expressao, codigo_da_expr = self.visitExpressao(ctx.expressao())
        if tipo_da_expressao == tipo_da_variavel:
            temp_jasmin_code += codigo_da_expr
            if tipo_da_variavel == "int":
                temp_jasmin_code += f"\tistore {pos_na_memoria}\n"
                self.stack.pop()

            elif tipo_da_variavel == "str":
                temp_jasmin_code += f"\tastore {pos_na_memoria}\n"
                self.stack.pop()

            elif tipo_da_variavel == "float":
                temp_jasmin_code += f"\tfstore {pos_na_memoria}\n"
                self.stack.pop()

            elif tipo_da_variavel == "bool":
                temp_jasmin_code += f"\tistore {pos_na_memoria}\n"
                self.stack.pop()
        else:
            linha = ctx.start.line
            logging.debug(f"Erro: na linha: {linha}, tipos incompativeis")
            exit(1)
        return temp_jasmin_code

    # Visit a parse tree produced by javaSimplesParser#comando_print.
    def visitComando_print(self, ctx: javaSimplesParser.Comando_printContext):
        # TODO: Verificar o identificador a ser impresso existe
        temp_jasmin_code = "\t; Comando print\n"

        for expressao in ctx.lista_de_expressoes().expressao():
            tipo_da_expressao, codigo_da_expressao = self.visitExpressao(expressao)
            temp_jasmin_code += "\tgetstatic java/lang/System/out Ljava/io/PrintStream;\n"
            temp_jasmin_code += codigo_da_expressao
            temp_jasmin_code += "\tinvokevirtual java/io/PrintStream/print"
            #print(f"codigo da expressao: {codigo_da_expressao}")
            if tipo_da_expressao == "int":
                temp_jasmin_code += "(I)" # Print recebe inteiro.

            elif tipo_da_expressao == "float":
                temp_jasmin_code += "(F)" # Print recebe float

            elif tipo_da_expressao == "bool":
                temp_jasmin_code += "(I)" # Print recebe booleano como inteiro(0 ou 1)

            elif tipo_da_expressao == "str":
                temp_jasmin_code += "(Ljava/lang/String;)" # Print recebe string

            temp_jasmin_code += "V\n" # Print retorna void

            # pegar o que vai para a pilha

        return temp_jasmin_code

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
    input_stream = FileStream('./testes_entrada/funcao_testes_do_gabriel.txt')
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
