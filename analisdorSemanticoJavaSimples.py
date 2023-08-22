from antlr4 import *
from gen.javaSimplesLexer import javaSimplesLexer
from gen.javaSimplesParser import javaSimplesParser
from gen.javaSimplesVisitor import javaSimplesVisitor
import logging


class Erro(Exception):
    def __init__(self, mensagem):
        self.mensagem = mensagem
        super().__init__(self.mensagem)


class MyVisitor(javaSimplesVisitor):
    def __init__(self, path_do_programa):
        self.nome_do_programa = path_do_programa.split('/')[-1]
        self.path_do_programa = path_do_programa
        self.jasmin_code = ""
        self.variablesTable = {}
        self.functionsTable = {}
        self.loopcount = 0
        self.dict_variavel_valor = {}
        logging.basicConfig(level=logging.DEBUG)
        self.stack = [1]
        self.higher_stack_size = 1
        self.palavras_reservadas = javaSimplesLexer.literalNames  # Variáveis não podem usar esses nomes

    def executar(self):
        input_stream = FileStream(self.path_do_programa)
        # Criar o lexer
        lexer = javaSimplesLexer(input_stream)

        # Criar o stream de tokens
        token_stream = CommonTokenStream(lexer)

        # Criar o parser
        parser = javaSimplesParser(token_stream)

        # Obter a árvore de análise sintática
        tree = parser.programa()

        # Visitar a árvore de análise sintática
        self.visit(tree)

    def save_jasmin_code(self):
        with open(self.nome_do_programa.split('.')[0] + ".j", "w") as file:
            file.write(self.jasmin_code)
            return file.name

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
            temp_jasmin_code += f"\taload {identificador}\n"
            self.atualiza_pilha("append")
        else:
            temp_jasmin_code += f"\tiload {identificador}\n"
            self.atualiza_pilha("append")
        return temp_jasmin_code

    def adicionar_funcoes_de_leitura_no_codigo_jasmin(self):
        self.adicionar_funcao_ler_inteiro_no_codigo()
        self.adicionar_funcao_ler_float_no_codigo()
        self.adicionar_funcao_ler_string_no_codigo()
        self.adicionar_funcao_ler_booleano_no_codigo()
        self.jasmin_code += "\n\n"

    def adicionar_funcao_ler_inteiro_no_codigo(self):
        self.jasmin_code += '.method public static lerInteiro()I\n\
        \t.limit stack 3\n\
        \t.limit locals 1\n\
        \tnew java/util/Scanner\n\
        \tdup\n\
        \tgetstatic java/lang/System/in Ljava/io/InputStream;\n\
        \tinvokespecial java/util/Scanner/<init>(Ljava/io/InputStream;)V\n\
        \tinvokevirtual java/util/Scanner/nextInt()I ; usa o nextInt do Scanner\n\
        \tireturn\n\
        .end method\n'

    def adicionar_funcao_ler_float_no_codigo(self):
        self.jasmin_code += ".method public static readFloat()F\n\
    \t.limit stack 3\n\
    \t.limit locals 3\n\
    \tnew java/util/Scanner       ; Cria uma nova instância de Scanner\n\
    \tdup\n\
    \tgetstatic java/lang/System/in Ljava/io/InputStream;\n\
    \tinvokespecial java/util/Scanner/<init>(Ljava/io/InputStream;)V\n\
    \tinvokevirtual java/util/Scanner/nextFloat()F   ; Lê o valor float\n\
    \tfreturn    ; Retorna o valor float lido\n\
.end method\n"

    def adicionar_funcao_ler_string_no_codigo(self):
        self.jasmin_code += ".method public static readString()Ljava/lang/String;\n\
    \t.limit stack 3\n\
    \t.limit locals 4\n\
    \tnew java/util/Scanner        ; Cria uma nova instância de Scanner\n\
    \tdup\n\
    \tgetstatic java/lang/System/in Ljava/io/InputStream;\n\
    \tinvokespecial java/util/Scanner/<init>(Ljava/io/InputStream;)V\n\
    \tinvokevirtual java/util/Scanner/nextLine()Ljava/lang/String;  ; Lê a linha inteira\n\
    \tastore_0    ; Armazena a string lida na variável local 0\n\
    \taload_0     ; Carrega a string na pilha\n\
    \tareturn     ; Retorna a string lida\n\
.end method\n"

    def adicionar_funcao_ler_booleano_no_codigo(self):
        self.jasmin_code += f".method public static readBoolean()I\n\
    \t.limit stack 3\n\
    \t.limit locals 4\n\
    \tnew java/util/Scanner        ; Cria uma nova instância de Scanner\n\
    \tdup\n\
    \tgetstatic java/lang/System/in Ljava/io/InputStream;\n\
    \tinvokespecial java/util/Scanner/<init>(Ljava/io/InputStream;)V\n\
    \tinvokevirtual java/util/Scanner/nextBoolean()Z  ; Lê o valor booleano\n\
    \tifeq false_value   ; Se o valor booleano for falso, vá para o rótulo false_value\n\
    \tldc 1              ; Se for verdadeiro, carrega o valor 1 na pilha\n\
    \tgoto end\n\
false_value:\n\
    \tldc 0              ; Carrega o valor 0 na pilha\n\
end:\n\
    \tireturn            ; Retorna o valor inteiro na pilha\n\
.end method\n"

    #################################################################
    ######                     Ingrid                          ######
    #################################################################
    # Visit a parse tree produced by javaSimplesParser#programa.
    def visitPrograma(self, ctx: javaSimplesParser.ProgramaContext):
        print("Iniciando analise do codigo...")
        self.jasmin_code += f".class public {self.nome_do_programa.split('.')[0]}\n"
        self.jasmin_code += f".super java/lang/Object\n\n"
        return self.visitChildren(ctx)

    # Visit a parse tree produced by javaSimplesParser#funcao_main.
    def visitFuncao_main(self, ctx: javaSimplesParser.Funcao_mainContext):
        print("Criando a Main...")
        n_variaveis = 1
        decl_jasmin_code = ""
        comando_jasmin_code = ""
        self.adicionar_funcoes_de_leitura_no_codigo_jasmin()
        self.jasmin_code += f".method public static main([Ljava/lang/String;)V\n"
        if ctx.declaracoes():
            decl_jasmin_code = self.visitDeclaracoes(ctx.declaracoes())
        if ctx.comando():
            for comando in ctx.comando():
                comando_jasmin_code += self.visitComando(comando)

        n_variaveis = self.conta_variaveis()
        self.jasmin_code += f"\t.limit stack {self.higher_stack_size}\n"
        self.jasmin_code += f"\t.limit locals {n_variaveis}\n"
        self.jasmin_code += decl_jasmin_code
        self.jasmin_code += comando_jasmin_code
        self.jasmin_code += f"\treturn\n"
        self.jasmin_code += f".end method\n"
        self.variablesTable = {}
        self.stack = [1]
        self.higher_stack_size = 1

    # Visit a parse tree produced by javaSimplesParser#dec_de_func.
    def visitDec_de_func(self, ctx: javaSimplesParser.Dec_de_funcContext):
        print("Começando a declaração de função...")
        n_variaveis = 1
        decl_jasmin_code = ""
        comando_jasmin_code = ""
        cabc_da_funcao = self.visitCabecalho_de_func(ctx.cabecalho_de_func())
        if ctx.declaracoes():
            decl_jasmin_code = self.visitDeclaracoes(ctx.declaracoes())
        if ctx.comando():
            for comando in ctx.comando():
                comando_jasmin_code += self.visitComando(comando)

        n_variaveis = self.conta_variaveis()
        self.jasmin_code += cabc_da_funcao
        self.jasmin_code += f"\t.limit stack {self.higher_stack_size}\n"
        self.jasmin_code += f"\t.limit locals {n_variaveis}\n"
        self.jasmin_code += decl_jasmin_code
        self.jasmin_code += comando_jasmin_code
        self.jasmin_code += f".end method\n\n"

        print("Terminando a declaração de função...")
        self.variablesTable = {}
        self.stack = [1]
        self.higher_stack_size = 1

    # Visit a parse tree produced by javaSimplesParser#cabecalho_de_func.
    def visitCabecalho_de_func(self, ctx: javaSimplesParser.Cabecalho_de_funcContext):
        nome_funcao = ctx.IDENTIFICADOR().getText()
        tipos, parametros_da_funcao = self.visitLista_de_parametros(ctx.lista_de_parametros())
        temp_jasmin_code = ""
        tipo_da_funcao = ""

        if ctx.TIPO():
            tipo_da_funcao = ctx.TIPO().getText()
        if tipo_da_funcao == "int":
            temp_jasmin_code += f".method public static {nome_funcao}({parametros_da_funcao})I\n"
        elif tipo_da_funcao == "float":
            temp_jasmin_code += f".method public static {nome_funcao}({parametros_da_funcao})F\n"
        elif tipo_da_funcao == "str":
            temp_jasmin_code += f".method public static {nome_funcao}({parametros_da_funcao})Ljava/lang/String\n"
        elif tipo_da_funcao == "bool":
            temp_jasmin_code += f".method public static {nome_funcao}({parametros_da_funcao})I\n"
        else:
            temp_jasmin_code += f".method public static {nome_funcao}({parametros_da_funcao})V\n"
            tipo_da_funcao = "void"

        self.functionsTable[nome_funcao] = (tipo_da_funcao, tipos)
        return temp_jasmin_code

    # Visit a parse tree produced by javaSimplesParser#lista_de_parametros.
    def visitLista_de_parametros(self, ctx: javaSimplesParser.Lista_de_parametrosContext):
        temp_jasmin_code = ""
        tipos = []
        print("Recebendo Parametros...")
        for parametro in ctx.parametro():
            tipo, param_jasmin_code = self.visitParametro(parametro)
            temp_jasmin_code += param_jasmin_code
            tipos.append(tipo)

        return tipos, temp_jasmin_code

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
        print(f"\tParametro -> {ctx.IDENTIFICADOR().getText()} do tipo {tipo}")
        self.variablesTable[ctx.IDENTIFICADOR().getText()] = (len(self.variablesTable), tipo)
        return tipo, temp_jasmin_code

    #################################################################
    ######                     Daniel                          ######
    #################################################################
    #### Minhas Notas: Rever os returns, descobrir o que é pra retornar pras funções
    # Vendo todas as declarações de variaveis e constantes do codigo
    def visitDeclaracoes(self, ctx: javaSimplesParser.DeclaracoesContext):
        # print("Iniciando Declarações...")
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
        print("Declarando Variaveis...")
        variable_names = ctx.lista_de_var().IDENTIFICADOR()
        data_type = ctx.TIPO().getText()
        temp_jasmin_code = ""

        for variable_name in variable_names:
            if variable_name.getText() in self.variablesTable:
                linha = ctx.start.line
                raise Erro(f"Erro na linha {linha}, variavel já declarada")
            else:
                self.variablesTable[variable_name.getText()] = (len(self.variablesTable), data_type)
                if data_type == "int":
                    temp_jasmin_code += f"\tldc 0\n"
                    temp_jasmin_code += f"\tistore {self.variablesTable[variable_name.getText()][0]}\n"
                elif data_type == "float":
                    temp_jasmin_code += f"\tldc 0.0\n"
                    temp_jasmin_code += f"\tfstore {self.variablesTable[variable_name.getText()][0]}\n"
                elif data_type == "str":
                    temp_jasmin_code += f'\tldc ""\n'
                    temp_jasmin_code += f"\tastore {self.variablesTable[variable_name.getText()][0]}\n"
                else:
                    temp_jasmin_code += f'\tldc 0\n'
                    temp_jasmin_code += f"\tistore {self.variablesTable[variable_name.getText()][0]}\n"
                print(f"\tCriando Variavel-> {variable_name.getText()} do Tipo {data_type}")
        return temp_jasmin_code

    # Visit a parse tree produced by javaSimplesParser#decl_de_var_const.
    def visitDecl_de_const(self, ctx: javaSimplesParser.Decl_de_constContext):
        print("Declarando Constantes...")
        constant_names = ctx.IDENTIFICADOR()
        constants = ctx.VALOR_INT()
        if constants:
            for i in range(0, len(constant_names)):
                self.variablesTable[constant_names[i].getText()] = constants[i].getText()
                print(f"\tCriando Constante-> {constant_names[i]} : {constants[i].getText()}")
        constants = ctx.VALOR_FLOAT()
        if constants:
            for i in range(0, len(constant_names)):
                self.variablesTable[constant_names[i].getText()] = constants[i].getText()
                print(f"\tCriando Constante-> {constant_names[i]} : {constants[i].getText()}")
        constants = ctx.VALOR_STR()
        if constants:
            for i in range(0, len(constant_names)):
                self.variablesTable[constant_names[i].getText()] = constants[i].getText()
                print(f"\tCriando Constante-> {constant_names[i]} : {constants[i].getText()}")
        constants = ctx.VALOR_BOOL()
        if constants:
            for i in range(0, len(constant_names)):
                self.variablesTable[constant_names[i].getText()] = constants[i].getText()
                print(f"\tCriando Constante-> {constant_names[i]} : {constants[i].getText()}")

    # Visit a parse tree produced by javaSimplesParser#expressao.
    def visitExpressao(self, ctx: javaSimplesParser.ExpressaoContext):
        print("realizando expressão...")
        temp_jasmin_code = ""
        tipo_expressao = None
        if ctx.expr_aritimetica():
            tipo_expressao, temp_jasmin_code = self.visitExpr_aritimetica(ctx.expr_aritimetica())
        elif ctx.expr_relacional():
            tipo_expressao, temp_jasmin_code = self.visitExpr_relacional(ctx.expr_relacional())
        elif ctx.VALOR_STR():
            texto = ctx.VALOR_STR().getText()
            temp_jasmin_code += f'\tldc {texto}\n'
            self.atualiza_pilha("append")
            tipo_expressao = "str"
        elif ctx.chamada_funcao():
            temp_jasmin_code = self.visitChamada_funcao(ctx.chamada_funcao())
            tipo_expressao = self.functionsTable[ctx.chamada_funcao().IDENTIFICADOR.getText()][0]
        return tipo_expressao, temp_jasmin_code

    # Visit a parse tree produced by javaSimplesParser#expr_aritimetica.
    def visitExpr_aritimetica(self, ctx: javaSimplesParser.Expr_aritimeticaContext):
        print("realizando expressão aritimetica...")
        temp_jasmin_code = ""
        if ctx.expr_aritimetica() is not None and ctx.OPERADOR_ARIT_LVL_2() is not None:
            operador = ctx.OPERADOR_ARIT_LVL_2().getText()
            tipo_operando_esq, op_esq_jasmin_code = self.visitExpr_aritimetica(ctx.getChild(0))
            tipo_operando_dir, op_dir_jasmin_code = self.visitExpr_aritimetica(ctx.getChild(2))
            if operador == "*":
                if tipo_operando_esq == "float" and tipo_operando_dir == "float":
                    # Adicionando o codigo jasmin do carregamento de operadores para o temp_jasmin_code
                    temp_jasmin_code += op_esq_jasmin_code
                    temp_jasmin_code += op_dir_jasmin_code
                    temp_jasmin_code += "\tfmult\n"
                    self.atualiza_pilha("pop")
                    return "float", temp_jasmin_code
                elif tipo_operando_esq == "float":
                    op_dir_jasmin_code += "\ti2f\n"
                    # Adicionando o codigo jasmin do carregamento de operadores para o temp_jasmin_code
                    temp_jasmin_code += op_esq_jasmin_code
                    temp_jasmin_code += op_dir_jasmin_code
                    temp_jasmin_code += "\tfmult\n"
                    self.atualiza_pilha("pop")
                    return "float", temp_jasmin_code
                elif tipo_operando_dir == "float":
                    op_esq_jasmin_code += "\ti2f\n"
                    # Adicionando o codigo jasmin do carregamento de operadores para o temp_jasmin_code
                    temp_jasmin_code += op_esq_jasmin_code
                    temp_jasmin_code += op_dir_jasmin_code
                    temp_jasmin_code += "\tfmult\n"
                    self.atualiza_pilha("pop")
                    return "float", temp_jasmin_code
                else:
                    # Adicionando o codigo jasmin do carregamento de operadores para o temp_jasmin_code
                    temp_jasmin_code += op_esq_jasmin_code
                    temp_jasmin_code += op_dir_jasmin_code
                    temp_jasmin_code += "\timult\n"
                    self.atualiza_pilha("pop")
                    return "int", temp_jasmin_code
            else:
                if tipo_operando_esq == "float" and tipo_operando_dir == "float":
                    # Adicionando o codigo jasmin do carregamento de operadores para o temp_jasmin_code
                    temp_jasmin_code += op_esq_jasmin_code
                    temp_jasmin_code += op_dir_jasmin_code
                    temp_jasmin_code += "\tfdiv\n"
                    self.atualiza_pilha("pop")
                    return "float", temp_jasmin_code
                elif tipo_operando_esq == "float":
                    op_dir_jasmin_code += "\ti2f\n"
                    # Adicionando o codigo jasmin do carregamento de operadores para o temp_jasmin_code
                    temp_jasmin_code += op_esq_jasmin_code
                    temp_jasmin_code += op_dir_jasmin_code
                    temp_jasmin_code += "\tfdiv\n"
                    self.atualiza_pilha("pop")
                    return "float", temp_jasmin_code
                elif tipo_operando_dir == "float":
                    op_esq_jasmin_code += "\ti2f\n"
                    # Adicionando o codigo jasmin do carregamento de operadores para o temp_jasmin_code
                    temp_jasmin_code += op_esq_jasmin_code
                    temp_jasmin_code += op_dir_jasmin_code
                    temp_jasmin_code += "\tfdiv\n"
                    self.atualiza_pilha("pop")
                    return "float", temp_jasmin_code
                else:
                    # Adicionando o codigo jasmin do carregamento de operadores para o temp_jasmin_code
                    temp_jasmin_code += op_esq_jasmin_code
                    temp_jasmin_code += op_dir_jasmin_code
                    temp_jasmin_code += "\tidiv\n"
                    self.atualiza_pilha("pop")
                    return "int", temp_jasmin_code
        elif ctx.expr_aritimetica() is not None and ctx.OPERADOR_ARIT_LVL_1() is not None:
            operador = ctx.OPERADOR_ARIT_LVL_1().getText()
            tipo_operando_esq, op_esq_jasmin_code = self.visitExpr_aritimetica(ctx.getChild(0))
            tipo_operando_dir, op_dir_jasmin_code = self.visitExpr_aritimetica(ctx.getChild(2))

            if operador == "+":
                if tipo_operando_esq == "float" and tipo_operando_dir == "float":
                    # Adicionando o codigo jasmin do carregamento de operadores para o temp_jasmin_code
                    temp_jasmin_code += op_esq_jasmin_code
                    temp_jasmin_code += op_dir_jasmin_code
                    temp_jasmin_code += "\tfadd\n"
                    self.atualiza_pilha("pop")
                    return "float", temp_jasmin_code
                elif tipo_operando_dir == "float":
                    op_esq_jasmin_code += "\ti2f\n"
                    # Adicionando o codigo jasmin do carregamento de operadores para o temp_jasmin_code
                    temp_jasmin_code += op_esq_jasmin_code
                    temp_jasmin_code += op_dir_jasmin_code
                    temp_jasmin_code += "\tfadd\n"
                    self.atualiza_pilha("pop")
                    return "float", temp_jasmin_code
                elif tipo_operando_esq == "float":
                    op_dir_jasmin_code += "\ti2f\n"
                    # Adicionando o codigo jasmin do carregamento de operadores para o temp_jasmin_code
                    temp_jasmin_code += op_esq_jasmin_code
                    temp_jasmin_code += op_dir_jasmin_code
                    temp_jasmin_code += "\tfadd\n"
                    self.atualiza_pilha("pop")
                    return "float", temp_jasmin_code
                else:
                    # Adicionando o codigo jasmin do carregamento de operadores para o temp_jasmin_code
                    temp_jasmin_code += op_esq_jasmin_code
                    temp_jasmin_code += op_dir_jasmin_code
                    temp_jasmin_code += "\tiadd\n"
                    self.atualiza_pilha("pop")
                    return "int", temp_jasmin_code
            else:
                if tipo_operando_esq == "float" and tipo_operando_dir == "float":
                    # Adicionando o codigo jasmin do carregamento de operadores para o temp_jasmin_code
                    temp_jasmin_code += op_esq_jasmin_code
                    temp_jasmin_code += op_dir_jasmin_code
                    temp_jasmin_code += "\tfsub\n"
                    self.atualiza_pilha("pop")
                    return "float", temp_jasmin_code
                elif tipo_operando_esq == "float":
                    op_dir_jasmin_code += "\ti2f\n"
                    # Adicionando o codigo jasmin do carregamento de operadores para o temp_jasmin_code
                    temp_jasmin_code += op_esq_jasmin_code
                    temp_jasmin_code += op_dir_jasmin_code
                    temp_jasmin_code += "\tfsub\n"
                    self.atualiza_pilha("pop")
                    return "float", temp_jasmin_code
                elif tipo_operando_dir == "float":
                    op_esq_jasmin_code += "\ti2f\n"
                    # Adicionando o codigo jasmin do carregamento de operadores para o temp_jasmin_code
                    temp_jasmin_code += op_esq_jasmin_code
                    temp_jasmin_code += op_dir_jasmin_code
                    temp_jasmin_code += "\tfsub\n"
                    self.atualiza_pilha("pop")
                    return "float", temp_jasmin_code
                else:
                    # Adicionando o codigo jasmin do carregamento de operadores para o temp_jasmin_code
                    temp_jasmin_code += op_esq_jasmin_code
                    temp_jasmin_code += op_dir_jasmin_code
                    temp_jasmin_code += "\tisub\n"
                    self.atualiza_pilha("pop")
                    return "int", temp_jasmin_code
        elif ctx.OPERADOR_ARIT_LVL_1() is not None and ctx.OPERADOR_ARIT_LVL_1().getText() == "-":
            tipo, termo_jasmin_code = self.visitTermo_aritimetico(ctx.termo_aritimetico())
            temp_jasmin_code += termo_jasmin_code
            if tipo == "int":
                temp_jasmin_code += "\tineg\n"
            else:
                temp_jasmin_code += "\tfneg\n"
            return tipo, temp_jasmin_code
        else:
            return self.visitTermo_aritimetico(ctx.termo_aritimetico())

    # Visit a parse tree produced by javaSimplesParser#termo_aritimetico.
    def visitTermo_aritimetico(self, ctx: javaSimplesParser.Termo_aritimeticoContext):
        print("carregando valor...")
        temp_jasmin_code = ""
        if ctx.IDENTIFICADOR() is not None:
            identificador = ctx.IDENTIFICADOR().getText()
            if identificador not in self.variablesTable:
                linha = ctx.start.line
                raise Erro(f"Erro: na linha: {linha}. O identificador \"{identificador}\" não existe")

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
        elif ctx.chamada_funcao() is not None:
            temp_jasmin_code = self.visitChamada_funcao(ctx.chamada_funcao())
            tipo_funcao = self.functionsTable[ctx.chamada_funcao().IDENTIFICADOR().getText()][0]
            return tipo_funcao, temp_jasmin_code
        else:  # Jasmin to do
            expr = self.visitExpr_aritimetica(ctx.expr_aritimetica())
            return expr

    # Visit a parse tree produced by javaSimplesParser#expr_relacional.
    def visitExpr_relacional(self, ctx: javaSimplesParser.Expr_relacionalContext):
        print("realizando expressão relacional...")
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
                temp_jasmin_code += f"\tif_icmpeq "
                self.atualiza_pilha("pop")
            else:
                temp_jasmin_code += f"\tif_icmpne "
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
                temp_jasmin_code += f"\tif_icmplt "
                self.atualiza_pilha("pop")
            elif operador == "<=":
                temp_jasmin_code += f"\tif_icmpgt "
                self.atualiza_pilha("pop")
            elif operador == ">":
                temp_jasmin_code += f"\tif_icmple "
                self.atualiza_pilha("pop")
            else:
                temp_jasmin_code += f"\tif_icmpge "
                self.atualiza_pilha("pop")
            return "bool", temp_jasmin_code
        else:
            return self.visitTermo_relacional(ctx.termo_relacional())

    # Visit a parse tree produced by javaSimplesParser#termo_relacional.
    def visitTermo_relacional(self, ctx: javaSimplesParser.Termo_relacionalContext):
        print("carregando valor booleano...")
        temp_jasmin_code = ""

        if ctx.IDENTIFICADOR() is not None:
            identificador = ctx.IDENTIFICADOR().getText()
            variavel, tipo = self.variablesTable[identificador]
            temp_jasmin_code = self.carregaVariavel(variavel, tipo)
            return "bool", temp_jasmin_code
        elif ctx.VALOR_INT() is not None:
            valor = ctx.VALOR_INT().getText()
            temp_jasmin_code += f"\tldc {valor}\n"
            self.atualiza_pilha("append")
            return "bool", temp_jasmin_code
        elif ctx.VALOR_FLOAT() is not None:
            valor = ctx.VALOR_FLOAT().getText()
            temp_jasmin_code += f"\tldc {valor}\n"
            self.atualiza_pilha("append")
            return "bool", temp_jasmin_code
        elif ctx.VALOR_BOOL() is not None:
            valor = ctx.VALOR_BOOL().getText()
            if valor == "true":
                temp_jasmin_code += f"\tldc 1\n"
                self.atualiza_pilha("append")
            else:
                temp_jasmin_code += f"\tldc 0\n"
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
        if ctx.chamada_funcao():
            return self.visitChamada_funcao(ctx.chamada_funcao())
        else:
            return self.visitChildren(ctx)

    # Visit a parse tree produced by javaSimplesParser#comando_if.
    def visitComando_if(self, ctx: javaSimplesParser.Comando_ifContext):
        temp_jasmin_code = "; Comando if\n"
        tipo, desvio_jasmin_code = self.visitExpr_relacional(ctx.expr_relacional())
        other_stmt = f"loop{self.loopcount}"
        out_if_else = f"loop{self.loopcount + 1}"
        self.loopcount += 2
        desvio_jasmin_code += f"{other_stmt}\n"
        temp_jasmin_code += desvio_jasmin_code
        if ctx.comando():
            for comando in ctx.comando():
                temp_jasmin_code += self.visitComando(comando)
            if ctx.comando_else():
                temp_jasmin_code += f"\tgoto {out_if_else}\n"
        temp_jasmin_code += f"{other_stmt}:\n"
        if ctx.comando_else():
            if ctx.comando_else().comando():
                for comando in ctx.comando_else().comando():
                    temp_jasmin_code += self.visitComando(comando)
            temp_jasmin_code += f"{out_if_else}:\n"

        return temp_jasmin_code

    # Visit a parse tree produced by javaSimplesParser#comando_while.
    def visitComando_while(self, ctx: javaSimplesParser.Comando_whileContext):
        temp_jasmin_code = "; Comando while\n"
        inicio_do_loop = f"loop{self.loopcount}"
        fim_do_loop = f"loop{self.loopcount + 1}"
        self.loopcount += 2
        temp_jasmin_code += f"{inicio_do_loop}:\n"

        tipo, desvio_jasmin_code = self.visitExpr_relacional(ctx.expr_relacional())
        desvio_jasmin_code += f"{fim_do_loop}\n"
        temp_jasmin_code += desvio_jasmin_code

        comandos = ctx.comando()
        for comando in comandos:
            temp_jasmin_code += self.visitComando(comando)
        temp_jasmin_code += f"\tgoto {inicio_do_loop}\n"

        temp_jasmin_code += f"{fim_do_loop}:\n"
        return temp_jasmin_code

    # Visit a parse tree produced by javaSimplesParser#comando_scanf.
    def visitComando_scanf(self, ctx: javaSimplesParser.Comando_scanfContext):
        print("Carregando scanner...")
        temp_jasmin_code = "; Comando scanf\n"
        for identificador in ctx.lista_de_var().IDENTIFICADOR():
            identificador = identificador.getText()
            if identificador not in self.variablesTable:
                raise Erro(f"Erro: variável \"{identificador}\" não existe")

            pos_na_memoria = self.variablesTable[identificador][0]
            tipo_da_variavel = self.variablesTable[identificador][1]
            if tipo_da_variavel == "int":
                temp_jasmin_code += f"\tinvokestatic {self.nome_do_programa.split('.')[0]}/lerInteiro()I\n"
                temp_jasmin_code += f"\tistore {pos_na_memoria}\n"

            elif tipo_da_variavel == "float":
                temp_jasmin_code += f"\tinvokestatic {self.nome_do_programa.split('.')[0]}/readFloat()F\n"
                temp_jasmin_code += f"\tfstore {pos_na_memoria}\n"

            elif tipo_da_variavel == "bool":
                temp_jasmin_code += f"\tinvokestatic {self.nome_do_programa.split('.')[0]}/readBoolean()I\n"
                temp_jasmin_code += f"\tfstore {pos_na_memoria}\n"

            elif tipo_da_variavel == "str":
                temp_jasmin_code += f"\tinvokestatic {self.nome_do_programa.split('.')[0]}/readString()" \
                                    f"Ljava/lang/String;\n "
                temp_jasmin_code += f"\tastore {pos_na_memoria}\n"
        return temp_jasmin_code

    # Visit a parse tree produced by javaSimplesParser#comando_atrib.
    def visitComando_atrib(self, ctx: javaSimplesParser.Comando_atribContext):
        temp_jasmin_code = "\t; Comando atrib\n"
        print("Atribuindo valores...")
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
        elif tipo_da_variavel == "float" and tipo_da_expressao == "int":
            temp_jasmin_code += codigo_da_expr
            temp_jasmin_code += f"\ti2f\n"
            temp_jasmin_code += f"\tfstore {pos_na_memoria}\n"
            self.stack.pop()
        else:
            linha = ctx.start.line
            raise Erro(f"Erro: na linha: {linha}, tipos incompativeis, esperava um {tipo_da_variavel}, recebido {tipo_da_expressao}")
        return temp_jasmin_code

    # Visit a parse tree produced by javaSimplesParser#comando_print.
    def visitComando_print(self, ctx: javaSimplesParser.Comando_printContext):
        # TODO: Verificar o identificador a ser impresso existe
        temp_jasmin_code = "\t; Comando print\n"
        print("Criando print...")

        for expressao in ctx.lista_de_expressoes().expressao():
            tipo_da_expressao, codigo_da_expressao = self.visitExpressao(expressao)
            temp_jasmin_code += "\tgetstatic java/lang/System/out Ljava/io/PrintStream;\n"
            temp_jasmin_code += codigo_da_expressao
            temp_jasmin_code += "\tinvokevirtual java/io/PrintStream/println"
            # print(f"codigo da expressao: {codigo_da_expressao}")
            if tipo_da_expressao == "int":
                temp_jasmin_code += "(I)"  # Print recebe inteiro.

            elif tipo_da_expressao == "float":
                temp_jasmin_code += "(F)"  # Print recebe float

            elif tipo_da_expressao == "bool":
                temp_jasmin_code += "(I)"  # Print recebe booleano como inteiro(0 ou 1)

            elif tipo_da_expressao == "str":
                temp_jasmin_code += "(Ljava/lang/String;)"  # Print recebe string

            temp_jasmin_code += "V\n"  # Print retorna void
            self.atualiza_pilha("pop")
            # pegar o que vai para a pilha

        return temp_jasmin_code

    # Visit a parse tree produced by javaSimplesParser#comando_break.
    def visitComando_break(self, ctx: javaSimplesParser.Comando_breakContext):
        temp_jasmin_code = "; Comando break\n"
        temp_jasmin_code += f"\tgoto loop{self.loopcount - 1}\n"
        return temp_jasmin_code

    # Visit a parse tree produced by javaSimplesParser#comando_return.
    def visitComando_return(self, ctx: javaSimplesParser.Comando_returnContext):
        temp_jasmin_code = "\t; Comando return\n"
        tipo, temp_jasmin_code = self.visitExpressao(ctx.expressao())
        if tipo == "int":
            temp_jasmin_code += "\tireturn\n"
        elif tipo == "float":
            temp_jasmin_code += "\tfreturn\n"
        elif tipo == "str":
            temp_jasmin_code += "\tareturn\n"
        else:
            temp_jasmin_code += "\tireturn\n"
        return temp_jasmin_code

    # Visit a parse tree produced by javaSimplesParser#chamada_funcao.
    def visitChamada_funcao(self, ctx: javaSimplesParser.Chamada_funcaoContext):
        temp_jasmin_code = "; Comando funcao\n"
        print("Preparando chamada de função...")
        parametros = ""
        # carregando os parametros
        if ctx.lista_de_var():
            variable_names = ctx.lista_de_var().IDENTIFICADOR()
            expected_variable_types = self.functionsTable[ctx.IDENTIFICADOR().getText()][1]
            for variable_name, tipo_do_parametro_esperado in zip(variable_names, expected_variable_types):
                if variable_name.getText() in self.variablesTable:
                    variable = self.variablesTable[variable_name.getText()][0]
                    data_type = self.variablesTable[variable_name.getText()][1]
                    if data_type == "int" and data_type == tipo_do_parametro_esperado:
                        temp_jasmin_code += f"\tiload {variable}\n"
                        parametros += "I"
                        self.atualiza_pilha("append")
                    elif data_type == "float" and data_type == tipo_do_parametro_esperado:
                        temp_jasmin_code += f"\tfload {variable}\n"
                        parametros += "F"
                        self.atualiza_pilha("append")
                    elif data_type == "str" and data_type == tipo_do_parametro_esperado:
                        temp_jasmin_code += f'\taload {variable}\n'
                        parametros += "Ljava/lang/String"
                        self.atualiza_pilha("append")
                    elif data_type == "bool" and data_type == tipo_do_parametro_esperado:
                        temp_jasmin_code += f'\tiload {variable}\n'
                        parametros += "I"
                        self.atualiza_pilha("append")
                    else:
                        linha = ctx.start.line
                        raise Erro(
                            f"Erro na linha {linha}: parametro recebido é do tipo {data_type},\
                            era esperado tipo {tipo_do_parametro_esperado}")
                else:
                    linha = ctx.start.line
                    raise Erro(f"Erro na linha {linha}: variavel {variable_name} não declarada")
        elif ctx.lista_de_expressoes():
            expressoes = ctx.lista_de_expressoes().expressao()
            expected_param_types = self.functionsTable[ctx.IDENTIFICADOR().getText()][1]
            for expressao, tipo_do_parametro_esperado in zip(expressoes, expected_param_types):
                tipo, expr_code = self.visitExpressao(expressao)
                print(tipo, tipo_do_parametro_esperado)
                if tipo == tipo_do_parametro_esperado:
                    temp_jasmin_code += expr_code
                if tipo == "int":
                    parametros += "I"
                elif tipo == "float":
                    parametros += "F"
                elif tipo == "str":
                    parametros += "Ljava/lang/String"
                elif tipo == "bool":
                    parametros += "I"
                else:
                    linha = ctx.start.line
                    raise Erro(
                        f"Erro na linha {linha}: parametro recebido é do tipo {tipo},\
                         era esperado tipo {tipo_do_parametro_esperado}")
        # Chamando a função em si
        tipo_de_retorno = self.functionsTable[ctx.IDENTIFICADOR().getText()][0]
        print()
        if tipo_de_retorno == "int":
            temp_jasmin_code += f"\tinvokestatic {self.nome_do_programa.split('.')[0]}/{ctx.IDENTIFICADOR().getText()}({parametros})I\n"
        elif tipo_de_retorno == "float":
            temp_jasmin_code += f"\tinvokestatic {self.nome_do_programa.split('.')[0]}/{ctx.IDENTIFICADOR().getText()}({parametros})F\n"
        elif tipo_de_retorno == "\tstr":
            temp_jasmin_code += f"\tinvokestatic {self.nome_do_programa.split('.')[0]}/{ctx.IDENTIFICADOR().getText()}({parametros})Ljava/lang/String\n"
        else:
            temp_jasmin_code += f"\tinvokestatic {self.nome_do_programa.split('.')[0]}/{ctx.IDENTIFICADOR().getText()}({parametros})I\n"

        return temp_jasmin_code
