# Generated from C:/Users/Windows_PC/Desktop/Arquivos/Estudos/1 - UFPI/6º Periodo/Compiladores/Projeto_Final_Compiladores/JavaSimples\javaSimples.g4 by ANTLR 4.12.0
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,34,296,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,1,0,5,0,52,8,0,10,0,
        12,0,55,9,0,1,0,1,0,1,1,1,1,1,1,3,1,62,8,1,1,1,5,1,65,8,1,10,1,12,
        1,68,9,1,1,1,1,1,1,2,1,2,3,2,74,8,2,1,2,5,2,77,8,2,10,2,12,2,80,
        9,2,1,2,1,2,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,4,1,4,1,4,5,4,94,8,4,10,
        4,12,4,97,9,4,3,4,99,8,4,1,5,1,5,1,5,1,6,1,6,1,6,1,6,3,6,108,8,6,
        1,6,1,6,4,6,112,8,6,11,6,12,6,113,1,7,1,7,1,7,1,7,1,8,1,8,1,8,1,
        8,1,8,1,8,1,8,1,8,5,8,128,8,8,10,8,12,8,131,9,8,1,9,1,9,1,9,5,9,
        136,8,9,10,9,12,9,139,9,9,1,10,1,10,1,10,5,10,144,8,10,10,10,12,
        10,147,9,10,1,11,1,11,1,11,1,11,3,11,153,8,11,1,12,1,12,3,12,157,
        8,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,5,12,167,8,12,10,12,
        12,12,170,9,12,1,13,1,13,1,13,1,13,1,13,1,13,3,13,178,8,13,1,14,
        3,14,181,8,14,1,14,1,14,1,14,3,14,186,8,14,1,14,1,14,1,14,3,14,191,
        8,14,1,14,1,14,1,14,3,14,196,8,14,1,14,1,14,1,14,3,14,201,8,14,1,
        14,3,14,204,8,14,1,15,1,15,1,15,3,15,209,8,15,1,15,1,15,1,15,1,15,
        3,15,215,8,15,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,
        3,16,227,8,16,1,17,1,17,1,17,1,17,1,17,1,17,5,17,235,8,17,10,17,
        12,17,238,9,17,1,17,1,17,1,17,5,17,243,8,17,10,17,12,17,246,9,17,
        3,17,248,8,17,1,17,1,17,1,18,1,18,1,18,1,18,1,18,1,18,4,18,258,8,
        18,11,18,12,18,259,1,18,1,18,1,19,1,19,1,19,1,19,1,19,1,19,1,20,
        1,20,1,20,1,20,1,20,1,21,1,21,1,21,1,21,1,21,1,21,1,22,1,22,1,22,
        1,23,1,23,1,23,1,23,1,24,1,24,1,24,1,24,3,24,292,8,24,1,24,1,24,
        1,24,0,1,24,25,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,
        36,38,40,42,44,46,48,0,4,2,0,6,6,30,30,1,0,19,22,1,0,19,20,2,0,19,
        20,22,22,313,0,53,1,0,0,0,2,58,1,0,0,0,4,71,1,0,0,0,6,83,1,0,0,0,
        8,98,1,0,0,0,10,100,1,0,0,0,12,103,1,0,0,0,14,115,1,0,0,0,16,119,
        1,0,0,0,18,132,1,0,0,0,20,140,1,0,0,0,22,152,1,0,0,0,24,154,1,0,
        0,0,26,177,1,0,0,0,28,203,1,0,0,0,30,214,1,0,0,0,32,226,1,0,0,0,
        34,228,1,0,0,0,36,251,1,0,0,0,38,263,1,0,0,0,40,269,1,0,0,0,42,274,
        1,0,0,0,44,280,1,0,0,0,46,283,1,0,0,0,48,287,1,0,0,0,50,52,3,4,2,
        0,51,50,1,0,0,0,52,55,1,0,0,0,53,51,1,0,0,0,53,54,1,0,0,0,54,56,
        1,0,0,0,55,53,1,0,0,0,56,57,3,2,1,0,57,1,1,0,0,0,58,59,5,1,0,0,59,
        61,5,2,0,0,60,62,3,12,6,0,61,60,1,0,0,0,61,62,1,0,0,0,62,66,1,0,
        0,0,63,65,3,32,16,0,64,63,1,0,0,0,65,68,1,0,0,0,66,64,1,0,0,0,66,
        67,1,0,0,0,67,69,1,0,0,0,68,66,1,0,0,0,69,70,5,3,0,0,70,3,1,0,0,
        0,71,73,3,6,3,0,72,74,3,12,6,0,73,72,1,0,0,0,73,74,1,0,0,0,74,78,
        1,0,0,0,75,77,3,32,16,0,76,75,1,0,0,0,77,80,1,0,0,0,78,76,1,0,0,
        0,78,79,1,0,0,0,79,81,1,0,0,0,80,78,1,0,0,0,81,82,5,3,0,0,82,5,1,
        0,0,0,83,84,5,31,0,0,84,85,5,4,0,0,85,86,3,8,4,0,86,87,5,5,0,0,87,
        88,5,2,0,0,88,89,7,0,0,0,89,7,1,0,0,0,90,95,3,10,5,0,91,92,5,7,0,
        0,92,94,3,10,5,0,93,91,1,0,0,0,94,97,1,0,0,0,95,93,1,0,0,0,95,96,
        1,0,0,0,96,99,1,0,0,0,97,95,1,0,0,0,98,90,1,0,0,0,98,99,1,0,0,0,
        99,9,1,0,0,0,100,101,5,30,0,0,101,102,5,31,0,0,102,11,1,0,0,0,103,
        104,5,8,0,0,104,111,5,2,0,0,105,108,3,14,7,0,106,108,3,16,8,0,107,
        105,1,0,0,0,107,106,1,0,0,0,108,109,1,0,0,0,109,110,5,9,0,0,110,
        112,1,0,0,0,111,107,1,0,0,0,112,113,1,0,0,0,113,111,1,0,0,0,113,
        114,1,0,0,0,114,13,1,0,0,0,115,116,3,18,9,0,116,117,5,2,0,0,117,
        118,5,30,0,0,118,15,1,0,0,0,119,120,5,10,0,0,120,121,5,31,0,0,121,
        122,5,11,0,0,122,129,7,1,0,0,123,124,5,7,0,0,124,125,5,31,0,0,125,
        126,5,11,0,0,126,128,7,1,0,0,127,123,1,0,0,0,128,131,1,0,0,0,129,
        127,1,0,0,0,129,130,1,0,0,0,130,17,1,0,0,0,131,129,1,0,0,0,132,137,
        5,31,0,0,133,134,5,7,0,0,134,136,5,31,0,0,135,133,1,0,0,0,136,139,
        1,0,0,0,137,135,1,0,0,0,137,138,1,0,0,0,138,19,1,0,0,0,139,137,1,
        0,0,0,140,145,3,22,11,0,141,142,5,7,0,0,142,144,3,22,11,0,143,141,
        1,0,0,0,144,147,1,0,0,0,145,143,1,0,0,0,145,146,1,0,0,0,146,21,1,
        0,0,0,147,145,1,0,0,0,148,153,3,24,12,0,149,153,3,28,14,0,150,153,
        5,21,0,0,151,153,3,48,24,0,152,148,1,0,0,0,152,149,1,0,0,0,152,150,
        1,0,0,0,152,151,1,0,0,0,153,23,1,0,0,0,154,156,6,12,-1,0,155,157,
        5,23,0,0,156,155,1,0,0,0,156,157,1,0,0,0,157,158,1,0,0,0,158,159,
        3,26,13,0,159,168,1,0,0,0,160,161,10,3,0,0,161,162,5,26,0,0,162,
        167,3,24,12,4,163,164,10,2,0,0,164,165,5,25,0,0,165,167,3,24,12,
        3,166,160,1,0,0,0,166,163,1,0,0,0,167,170,1,0,0,0,168,166,1,0,0,
        0,168,169,1,0,0,0,169,25,1,0,0,0,170,168,1,0,0,0,171,178,5,31,0,
        0,172,178,7,2,0,0,173,174,5,4,0,0,174,175,3,24,12,0,175,176,5,5,
        0,0,176,178,1,0,0,0,177,171,1,0,0,0,177,172,1,0,0,0,177,173,1,0,
        0,0,178,27,1,0,0,0,179,181,5,24,0,0,180,179,1,0,0,0,180,181,1,0,
        0,0,181,182,1,0,0,0,182,183,3,30,15,0,183,185,5,27,0,0,184,186,5,
        24,0,0,185,184,1,0,0,0,185,186,1,0,0,0,186,187,1,0,0,0,187,188,3,
        30,15,0,188,204,1,0,0,0,189,191,5,24,0,0,190,189,1,0,0,0,190,191,
        1,0,0,0,191,192,1,0,0,0,192,193,3,30,15,0,193,195,5,28,0,0,194,196,
        5,24,0,0,195,194,1,0,0,0,195,196,1,0,0,0,196,197,1,0,0,0,197,198,
        3,30,15,0,198,204,1,0,0,0,199,201,5,24,0,0,200,199,1,0,0,0,200,201,
        1,0,0,0,201,202,1,0,0,0,202,204,3,30,15,0,203,180,1,0,0,0,203,190,
        1,0,0,0,203,200,1,0,0,0,204,29,1,0,0,0,205,215,5,31,0,0,206,215,
        7,3,0,0,207,209,5,24,0,0,208,207,1,0,0,0,208,209,1,0,0,0,209,210,
        1,0,0,0,210,211,5,4,0,0,211,212,3,28,14,0,212,213,5,5,0,0,213,215,
        1,0,0,0,214,205,1,0,0,0,214,206,1,0,0,0,214,208,1,0,0,0,215,31,1,
        0,0,0,216,227,3,34,17,0,217,227,3,36,18,0,218,227,3,38,19,0,219,
        227,3,42,21,0,220,227,3,40,20,0,221,227,3,46,23,0,222,227,3,44,22,
        0,223,224,3,48,24,0,224,225,5,9,0,0,225,227,1,0,0,0,226,216,1,0,
        0,0,226,217,1,0,0,0,226,218,1,0,0,0,226,219,1,0,0,0,226,220,1,0,
        0,0,226,221,1,0,0,0,226,222,1,0,0,0,226,223,1,0,0,0,227,33,1,0,0,
        0,228,229,5,12,0,0,229,230,5,4,0,0,230,231,3,28,14,0,231,232,5,5,
        0,0,232,236,5,2,0,0,233,235,3,32,16,0,234,233,1,0,0,0,235,238,1,
        0,0,0,236,234,1,0,0,0,236,237,1,0,0,0,237,247,1,0,0,0,238,236,1,
        0,0,0,239,240,5,13,0,0,240,244,5,2,0,0,241,243,3,32,16,0,242,241,
        1,0,0,0,243,246,1,0,0,0,244,242,1,0,0,0,244,245,1,0,0,0,245,248,
        1,0,0,0,246,244,1,0,0,0,247,239,1,0,0,0,247,248,1,0,0,0,248,249,
        1,0,0,0,249,250,5,3,0,0,250,35,1,0,0,0,251,252,5,14,0,0,252,253,
        5,4,0,0,253,254,3,28,14,0,254,255,5,5,0,0,255,257,5,2,0,0,256,258,
        3,32,16,0,257,256,1,0,0,0,258,259,1,0,0,0,259,257,1,0,0,0,259,260,
        1,0,0,0,260,261,1,0,0,0,261,262,5,3,0,0,262,37,1,0,0,0,263,264,5,
        15,0,0,264,265,5,4,0,0,265,266,3,18,9,0,266,267,5,5,0,0,267,268,
        5,9,0,0,268,39,1,0,0,0,269,270,5,31,0,0,270,271,5,11,0,0,271,272,
        3,22,11,0,272,273,5,9,0,0,273,41,1,0,0,0,274,275,5,16,0,0,275,276,
        5,4,0,0,276,277,3,20,10,0,277,278,5,5,0,0,278,279,5,9,0,0,279,43,
        1,0,0,0,280,281,5,17,0,0,281,282,5,9,0,0,282,45,1,0,0,0,283,284,
        5,18,0,0,284,285,3,22,11,0,285,286,5,9,0,0,286,47,1,0,0,0,287,288,
        5,31,0,0,288,291,5,4,0,0,289,292,3,18,9,0,290,292,3,20,10,0,291,
        289,1,0,0,0,291,290,1,0,0,0,291,292,1,0,0,0,292,293,1,0,0,0,293,
        294,5,5,0,0,294,49,1,0,0,0,31,53,61,66,73,78,95,98,107,113,129,137,
        145,152,156,166,168,177,180,185,190,195,200,203,208,214,226,236,
        244,247,259,291
    ]

class javaSimplesParser ( Parser ):

    grammarFileName = "javaSimples.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'main'", "':'", "'end'", "'('", "')'", 
                     "'void'", "','", "'var'", "';'", "'const'", "'='", 
                     "'if'", "'else'", "'while'", "'scanf'", "'print'", 
                     "'break'", "'return'", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "'-'", "'!'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "VALOR_INT", 
                      "VALOR_FLOAT", "VALOR_STR", "VALOR_BOOL", "OPERADOR_UNARIO_ARIT", 
                      "OPERADOR_UNARIO_RELACIONAL", "OPERADOR_ARIT_LVL_1", 
                      "OPERADOR_ARIT_LVL_2", "OPERADOR_RELACIONAL_LVL_2", 
                      "OPERADOR_RELACIONAL_LVL_1", "OPERADOR_LOGICO", "TIPO", 
                      "IDENTIFICADOR", "COMENTARIO_BLOCO", "COMENTARIO_LINHA", 
                      "WS" ]

    RULE_programa = 0
    RULE_funcao_main = 1
    RULE_dec_de_func = 2
    RULE_cabecalho_de_func = 3
    RULE_lista_de_parametros = 4
    RULE_parametro = 5
    RULE_declaracoes = 6
    RULE_decl_de_var = 7
    RULE_decl_de_const = 8
    RULE_lista_de_var = 9
    RULE_lista_de_expressoes = 10
    RULE_expressao = 11
    RULE_expr_aritimetica = 12
    RULE_termo_aritimetico = 13
    RULE_expr_relacional = 14
    RULE_termo_relacional = 15
    RULE_comando = 16
    RULE_comando_if = 17
    RULE_comando_while = 18
    RULE_comando_scanf = 19
    RULE_comando_atrib = 20
    RULE_comando_print = 21
    RULE_comando_break = 22
    RULE_comando_return = 23
    RULE_chamada_funcao = 24

    ruleNames =  [ "programa", "funcao_main", "dec_de_func", "cabecalho_de_func", 
                   "lista_de_parametros", "parametro", "declaracoes", "decl_de_var", 
                   "decl_de_const", "lista_de_var", "lista_de_expressoes", 
                   "expressao", "expr_aritimetica", "termo_aritimetico", 
                   "expr_relacional", "termo_relacional", "comando", "comando_if", 
                   "comando_while", "comando_scanf", "comando_atrib", "comando_print", 
                   "comando_break", "comando_return", "chamada_funcao" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    T__16=17
    T__17=18
    VALOR_INT=19
    VALOR_FLOAT=20
    VALOR_STR=21
    VALOR_BOOL=22
    OPERADOR_UNARIO_ARIT=23
    OPERADOR_UNARIO_RELACIONAL=24
    OPERADOR_ARIT_LVL_1=25
    OPERADOR_ARIT_LVL_2=26
    OPERADOR_RELACIONAL_LVL_2=27
    OPERADOR_RELACIONAL_LVL_1=28
    OPERADOR_LOGICO=29
    TIPO=30
    IDENTIFICADOR=31
    COMENTARIO_BLOCO=32
    COMENTARIO_LINHA=33
    WS=34

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.12.0")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def funcao_main(self):
            return self.getTypedRuleContext(javaSimplesParser.Funcao_mainContext,0)


        def dec_de_func(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(javaSimplesParser.Dec_de_funcContext)
            else:
                return self.getTypedRuleContext(javaSimplesParser.Dec_de_funcContext,i)


        def getRuleIndex(self):
            return javaSimplesParser.RULE_programa

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrograma" ):
                listener.enterPrograma(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrograma" ):
                listener.exitPrograma(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrograma" ):
                return visitor.visitPrograma(self)
            else:
                return visitor.visitChildren(self)




    def programa(self):

        localctx = javaSimplesParser.ProgramaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_programa)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 53
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==31:
                self.state = 50
                self.dec_de_func()
                self.state = 55
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 56
            self.funcao_main()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Funcao_mainContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declaracoes(self):
            return self.getTypedRuleContext(javaSimplesParser.DeclaracoesContext,0)


        def comando(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(javaSimplesParser.ComandoContext)
            else:
                return self.getTypedRuleContext(javaSimplesParser.ComandoContext,i)


        def getRuleIndex(self):
            return javaSimplesParser.RULE_funcao_main

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFuncao_main" ):
                listener.enterFuncao_main(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFuncao_main" ):
                listener.exitFuncao_main(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncao_main" ):
                return visitor.visitFuncao_main(self)
            else:
                return visitor.visitChildren(self)




    def funcao_main(self):

        localctx = javaSimplesParser.Funcao_mainContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_funcao_main)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 58
            self.match(javaSimplesParser.T__0)
            self.state = 59
            self.match(javaSimplesParser.T__1)
            self.state = 61
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==8:
                self.state = 60
                self.declaracoes()


            self.state = 66
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 2147995648) != 0):
                self.state = 63
                self.comando()
                self.state = 68
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 69
            self.match(javaSimplesParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Dec_de_funcContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def cabecalho_de_func(self):
            return self.getTypedRuleContext(javaSimplesParser.Cabecalho_de_funcContext,0)


        def declaracoes(self):
            return self.getTypedRuleContext(javaSimplesParser.DeclaracoesContext,0)


        def comando(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(javaSimplesParser.ComandoContext)
            else:
                return self.getTypedRuleContext(javaSimplesParser.ComandoContext,i)


        def getRuleIndex(self):
            return javaSimplesParser.RULE_dec_de_func

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDec_de_func" ):
                listener.enterDec_de_func(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDec_de_func" ):
                listener.exitDec_de_func(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDec_de_func" ):
                return visitor.visitDec_de_func(self)
            else:
                return visitor.visitChildren(self)




    def dec_de_func(self):

        localctx = javaSimplesParser.Dec_de_funcContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_dec_de_func)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 71
            self.cabecalho_de_func()
            self.state = 73
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==8:
                self.state = 72
                self.declaracoes()


            self.state = 78
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 2147995648) != 0):
                self.state = 75
                self.comando()
                self.state = 80
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 81
            self.match(javaSimplesParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Cabecalho_de_funcContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFICADOR(self):
            return self.getToken(javaSimplesParser.IDENTIFICADOR, 0)

        def lista_de_parametros(self):
            return self.getTypedRuleContext(javaSimplesParser.Lista_de_parametrosContext,0)


        def TIPO(self):
            return self.getToken(javaSimplesParser.TIPO, 0)

        def getRuleIndex(self):
            return javaSimplesParser.RULE_cabecalho_de_func

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCabecalho_de_func" ):
                listener.enterCabecalho_de_func(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCabecalho_de_func" ):
                listener.exitCabecalho_de_func(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCabecalho_de_func" ):
                return visitor.visitCabecalho_de_func(self)
            else:
                return visitor.visitChildren(self)




    def cabecalho_de_func(self):

        localctx = javaSimplesParser.Cabecalho_de_funcContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_cabecalho_de_func)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 83
            self.match(javaSimplesParser.IDENTIFICADOR)
            self.state = 84
            self.match(javaSimplesParser.T__3)
            self.state = 85
            self.lista_de_parametros()
            self.state = 86
            self.match(javaSimplesParser.T__4)
            self.state = 87
            self.match(javaSimplesParser.T__1)
            self.state = 88
            _la = self._input.LA(1)
            if not(_la==6 or _la==30):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Lista_de_parametrosContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def parametro(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(javaSimplesParser.ParametroContext)
            else:
                return self.getTypedRuleContext(javaSimplesParser.ParametroContext,i)


        def getRuleIndex(self):
            return javaSimplesParser.RULE_lista_de_parametros

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLista_de_parametros" ):
                listener.enterLista_de_parametros(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLista_de_parametros" ):
                listener.exitLista_de_parametros(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLista_de_parametros" ):
                return visitor.visitLista_de_parametros(self)
            else:
                return visitor.visitChildren(self)




    def lista_de_parametros(self):

        localctx = javaSimplesParser.Lista_de_parametrosContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_lista_de_parametros)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 98
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==30:
                self.state = 90
                self.parametro()
                self.state = 95
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==7:
                    self.state = 91
                    self.match(javaSimplesParser.T__6)
                    self.state = 92
                    self.parametro()
                    self.state = 97
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParametroContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TIPO(self):
            return self.getToken(javaSimplesParser.TIPO, 0)

        def IDENTIFICADOR(self):
            return self.getToken(javaSimplesParser.IDENTIFICADOR, 0)

        def getRuleIndex(self):
            return javaSimplesParser.RULE_parametro

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParametro" ):
                listener.enterParametro(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParametro" ):
                listener.exitParametro(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParametro" ):
                return visitor.visitParametro(self)
            else:
                return visitor.visitChildren(self)




    def parametro(self):

        localctx = javaSimplesParser.ParametroContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_parametro)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 100
            self.match(javaSimplesParser.TIPO)
            self.state = 101
            self.match(javaSimplesParser.IDENTIFICADOR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclaracoesContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def decl_de_var(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(javaSimplesParser.Decl_de_varContext)
            else:
                return self.getTypedRuleContext(javaSimplesParser.Decl_de_varContext,i)


        def decl_de_const(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(javaSimplesParser.Decl_de_constContext)
            else:
                return self.getTypedRuleContext(javaSimplesParser.Decl_de_constContext,i)


        def getRuleIndex(self):
            return javaSimplesParser.RULE_declaracoes

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclaracoes" ):
                listener.enterDeclaracoes(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclaracoes" ):
                listener.exitDeclaracoes(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclaracoes" ):
                return visitor.visitDeclaracoes(self)
            else:
                return visitor.visitChildren(self)




    def declaracoes(self):

        localctx = javaSimplesParser.DeclaracoesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_declaracoes)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 103
            self.match(javaSimplesParser.T__7)
            self.state = 104
            self.match(javaSimplesParser.T__1)
            self.state = 111 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 107
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [31]:
                        self.state = 105
                        self.decl_de_var()
                        pass
                    elif token in [10]:
                        self.state = 106
                        self.decl_de_const()
                        pass
                    else:
                        raise NoViableAltException(self)

                    self.state = 109
                    self.match(javaSimplesParser.T__8)

                else:
                    raise NoViableAltException(self)
                self.state = 113 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,8,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Decl_de_varContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def lista_de_var(self):
            return self.getTypedRuleContext(javaSimplesParser.Lista_de_varContext,0)


        def TIPO(self):
            return self.getToken(javaSimplesParser.TIPO, 0)

        def getRuleIndex(self):
            return javaSimplesParser.RULE_decl_de_var

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDecl_de_var" ):
                listener.enterDecl_de_var(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDecl_de_var" ):
                listener.exitDecl_de_var(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDecl_de_var" ):
                return visitor.visitDecl_de_var(self)
            else:
                return visitor.visitChildren(self)




    def decl_de_var(self):

        localctx = javaSimplesParser.Decl_de_varContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_decl_de_var)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 115
            self.lista_de_var()
            self.state = 116
            self.match(javaSimplesParser.T__1)
            self.state = 117
            self.match(javaSimplesParser.TIPO)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Decl_de_constContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFICADOR(self, i:int=None):
            if i is None:
                return self.getTokens(javaSimplesParser.IDENTIFICADOR)
            else:
                return self.getToken(javaSimplesParser.IDENTIFICADOR, i)

        def VALOR_INT(self, i:int=None):
            if i is None:
                return self.getTokens(javaSimplesParser.VALOR_INT)
            else:
                return self.getToken(javaSimplesParser.VALOR_INT, i)

        def VALOR_FLOAT(self, i:int=None):
            if i is None:
                return self.getTokens(javaSimplesParser.VALOR_FLOAT)
            else:
                return self.getToken(javaSimplesParser.VALOR_FLOAT, i)

        def VALOR_STR(self, i:int=None):
            if i is None:
                return self.getTokens(javaSimplesParser.VALOR_STR)
            else:
                return self.getToken(javaSimplesParser.VALOR_STR, i)

        def VALOR_BOOL(self, i:int=None):
            if i is None:
                return self.getTokens(javaSimplesParser.VALOR_BOOL)
            else:
                return self.getToken(javaSimplesParser.VALOR_BOOL, i)

        def getRuleIndex(self):
            return javaSimplesParser.RULE_decl_de_const

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDecl_de_const" ):
                listener.enterDecl_de_const(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDecl_de_const" ):
                listener.exitDecl_de_const(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDecl_de_const" ):
                return visitor.visitDecl_de_const(self)
            else:
                return visitor.visitChildren(self)




    def decl_de_const(self):

        localctx = javaSimplesParser.Decl_de_constContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_decl_de_const)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 119
            self.match(javaSimplesParser.T__9)
            self.state = 120
            self.match(javaSimplesParser.IDENTIFICADOR)
            self.state = 121
            self.match(javaSimplesParser.T__10)
            self.state = 122
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 7864320) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 129
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==7:
                self.state = 123
                self.match(javaSimplesParser.T__6)
                self.state = 124
                self.match(javaSimplesParser.IDENTIFICADOR)
                self.state = 125
                self.match(javaSimplesParser.T__10)
                self.state = 126
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 7864320) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 131
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Lista_de_varContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFICADOR(self, i:int=None):
            if i is None:
                return self.getTokens(javaSimplesParser.IDENTIFICADOR)
            else:
                return self.getToken(javaSimplesParser.IDENTIFICADOR, i)

        def getRuleIndex(self):
            return javaSimplesParser.RULE_lista_de_var

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLista_de_var" ):
                listener.enterLista_de_var(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLista_de_var" ):
                listener.exitLista_de_var(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLista_de_var" ):
                return visitor.visitLista_de_var(self)
            else:
                return visitor.visitChildren(self)




    def lista_de_var(self):

        localctx = javaSimplesParser.Lista_de_varContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_lista_de_var)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 132
            self.match(javaSimplesParser.IDENTIFICADOR)
            self.state = 137
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==7:
                self.state = 133
                self.match(javaSimplesParser.T__6)
                self.state = 134
                self.match(javaSimplesParser.IDENTIFICADOR)
                self.state = 139
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Lista_de_expressoesContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expressao(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(javaSimplesParser.ExpressaoContext)
            else:
                return self.getTypedRuleContext(javaSimplesParser.ExpressaoContext,i)


        def getRuleIndex(self):
            return javaSimplesParser.RULE_lista_de_expressoes

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLista_de_expressoes" ):
                listener.enterLista_de_expressoes(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLista_de_expressoes" ):
                listener.exitLista_de_expressoes(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLista_de_expressoes" ):
                return visitor.visitLista_de_expressoes(self)
            else:
                return visitor.visitChildren(self)




    def lista_de_expressoes(self):

        localctx = javaSimplesParser.Lista_de_expressoesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_lista_de_expressoes)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 140
            self.expressao()
            self.state = 145
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==7:
                self.state = 141
                self.match(javaSimplesParser.T__6)
                self.state = 142
                self.expressao()
                self.state = 147
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressaoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr_aritimetica(self):
            return self.getTypedRuleContext(javaSimplesParser.Expr_aritimeticaContext,0)


        def expr_relacional(self):
            return self.getTypedRuleContext(javaSimplesParser.Expr_relacionalContext,0)


        def VALOR_STR(self):
            return self.getToken(javaSimplesParser.VALOR_STR, 0)

        def chamada_funcao(self):
            return self.getTypedRuleContext(javaSimplesParser.Chamada_funcaoContext,0)


        def getRuleIndex(self):
            return javaSimplesParser.RULE_expressao

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpressao" ):
                listener.enterExpressao(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpressao" ):
                listener.exitExpressao(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpressao" ):
                return visitor.visitExpressao(self)
            else:
                return visitor.visitChildren(self)




    def expressao(self):

        localctx = javaSimplesParser.ExpressaoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_expressao)
        try:
            self.state = 152
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 148
                self.expr_aritimetica(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 149
                self.expr_relacional()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 150
                self.match(javaSimplesParser.VALOR_STR)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 151
                self.chamada_funcao()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr_aritimeticaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def termo_aritimetico(self):
            return self.getTypedRuleContext(javaSimplesParser.Termo_aritimeticoContext,0)


        def OPERADOR_UNARIO_ARIT(self):
            return self.getToken(javaSimplesParser.OPERADOR_UNARIO_ARIT, 0)

        def expr_aritimetica(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(javaSimplesParser.Expr_aritimeticaContext)
            else:
                return self.getTypedRuleContext(javaSimplesParser.Expr_aritimeticaContext,i)


        def OPERADOR_ARIT_LVL_2(self):
            return self.getToken(javaSimplesParser.OPERADOR_ARIT_LVL_2, 0)

        def OPERADOR_ARIT_LVL_1(self):
            return self.getToken(javaSimplesParser.OPERADOR_ARIT_LVL_1, 0)

        def getRuleIndex(self):
            return javaSimplesParser.RULE_expr_aritimetica

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr_aritimetica" ):
                listener.enterExpr_aritimetica(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr_aritimetica" ):
                listener.exitExpr_aritimetica(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr_aritimetica" ):
                return visitor.visitExpr_aritimetica(self)
            else:
                return visitor.visitChildren(self)



    def expr_aritimetica(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = javaSimplesParser.Expr_aritimeticaContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 24
        self.enterRecursionRule(localctx, 24, self.RULE_expr_aritimetica, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 156
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==23:
                self.state = 155
                self.match(javaSimplesParser.OPERADOR_UNARIO_ARIT)


            self.state = 158
            self.termo_aritimetico()
            self._ctx.stop = self._input.LT(-1)
            self.state = 168
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,15,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 166
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
                    if la_ == 1:
                        localctx = javaSimplesParser.Expr_aritimeticaContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr_aritimetica)
                        self.state = 160
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 161
                        self.match(javaSimplesParser.OPERADOR_ARIT_LVL_2)
                        self.state = 162
                        self.expr_aritimetica(4)
                        pass

                    elif la_ == 2:
                        localctx = javaSimplesParser.Expr_aritimeticaContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr_aritimetica)
                        self.state = 163
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 164
                        self.match(javaSimplesParser.OPERADOR_ARIT_LVL_1)
                        self.state = 165
                        self.expr_aritimetica(3)
                        pass

             
                self.state = 170
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,15,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Termo_aritimeticoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFICADOR(self):
            return self.getToken(javaSimplesParser.IDENTIFICADOR, 0)

        def VALOR_INT(self):
            return self.getToken(javaSimplesParser.VALOR_INT, 0)

        def VALOR_FLOAT(self):
            return self.getToken(javaSimplesParser.VALOR_FLOAT, 0)

        def expr_aritimetica(self):
            return self.getTypedRuleContext(javaSimplesParser.Expr_aritimeticaContext,0)


        def getRuleIndex(self):
            return javaSimplesParser.RULE_termo_aritimetico

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTermo_aritimetico" ):
                listener.enterTermo_aritimetico(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTermo_aritimetico" ):
                listener.exitTermo_aritimetico(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTermo_aritimetico" ):
                return visitor.visitTermo_aritimetico(self)
            else:
                return visitor.visitChildren(self)




    def termo_aritimetico(self):

        localctx = javaSimplesParser.Termo_aritimeticoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_termo_aritimetico)
        self._la = 0 # Token type
        try:
            self.state = 177
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [31]:
                self.enterOuterAlt(localctx, 1)
                self.state = 171
                self.match(javaSimplesParser.IDENTIFICADOR)
                pass
            elif token in [19, 20]:
                self.enterOuterAlt(localctx, 2)
                self.state = 172
                _la = self._input.LA(1)
                if not(_la==19 or _la==20):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                pass
            elif token in [4]:
                self.enterOuterAlt(localctx, 3)
                self.state = 173
                self.match(javaSimplesParser.T__3)
                self.state = 174
                self.expr_aritimetica(0)
                self.state = 175
                self.match(javaSimplesParser.T__4)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr_relacionalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def termo_relacional(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(javaSimplesParser.Termo_relacionalContext)
            else:
                return self.getTypedRuleContext(javaSimplesParser.Termo_relacionalContext,i)


        def OPERADOR_RELACIONAL_LVL_2(self):
            return self.getToken(javaSimplesParser.OPERADOR_RELACIONAL_LVL_2, 0)

        def OPERADOR_UNARIO_RELACIONAL(self, i:int=None):
            if i is None:
                return self.getTokens(javaSimplesParser.OPERADOR_UNARIO_RELACIONAL)
            else:
                return self.getToken(javaSimplesParser.OPERADOR_UNARIO_RELACIONAL, i)

        def OPERADOR_RELACIONAL_LVL_1(self):
            return self.getToken(javaSimplesParser.OPERADOR_RELACIONAL_LVL_1, 0)

        def getRuleIndex(self):
            return javaSimplesParser.RULE_expr_relacional

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr_relacional" ):
                listener.enterExpr_relacional(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr_relacional" ):
                listener.exitExpr_relacional(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr_relacional" ):
                return visitor.visitExpr_relacional(self)
            else:
                return visitor.visitChildren(self)




    def expr_relacional(self):

        localctx = javaSimplesParser.Expr_relacionalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_expr_relacional)
        try:
            self.state = 203
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 180
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
                if la_ == 1:
                    self.state = 179
                    self.match(javaSimplesParser.OPERADOR_UNARIO_RELACIONAL)


                self.state = 182
                self.termo_relacional()
                self.state = 183
                self.match(javaSimplesParser.OPERADOR_RELACIONAL_LVL_2)
                self.state = 185
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
                if la_ == 1:
                    self.state = 184
                    self.match(javaSimplesParser.OPERADOR_UNARIO_RELACIONAL)


                self.state = 187
                self.termo_relacional()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 190
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
                if la_ == 1:
                    self.state = 189
                    self.match(javaSimplesParser.OPERADOR_UNARIO_RELACIONAL)


                self.state = 192
                self.termo_relacional()
                self.state = 193
                self.match(javaSimplesParser.OPERADOR_RELACIONAL_LVL_1)
                self.state = 195
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
                if la_ == 1:
                    self.state = 194
                    self.match(javaSimplesParser.OPERADOR_UNARIO_RELACIONAL)


                self.state = 197
                self.termo_relacional()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 200
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
                if la_ == 1:
                    self.state = 199
                    self.match(javaSimplesParser.OPERADOR_UNARIO_RELACIONAL)


                self.state = 202
                self.termo_relacional()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Termo_relacionalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFICADOR(self):
            return self.getToken(javaSimplesParser.IDENTIFICADOR, 0)

        def VALOR_INT(self):
            return self.getToken(javaSimplesParser.VALOR_INT, 0)

        def VALOR_FLOAT(self):
            return self.getToken(javaSimplesParser.VALOR_FLOAT, 0)

        def VALOR_BOOL(self):
            return self.getToken(javaSimplesParser.VALOR_BOOL, 0)

        def expr_relacional(self):
            return self.getTypedRuleContext(javaSimplesParser.Expr_relacionalContext,0)


        def OPERADOR_UNARIO_RELACIONAL(self):
            return self.getToken(javaSimplesParser.OPERADOR_UNARIO_RELACIONAL, 0)

        def getRuleIndex(self):
            return javaSimplesParser.RULE_termo_relacional

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTermo_relacional" ):
                listener.enterTermo_relacional(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTermo_relacional" ):
                listener.exitTermo_relacional(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTermo_relacional" ):
                return visitor.visitTermo_relacional(self)
            else:
                return visitor.visitChildren(self)




    def termo_relacional(self):

        localctx = javaSimplesParser.Termo_relacionalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_termo_relacional)
        self._la = 0 # Token type
        try:
            self.state = 214
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [31]:
                self.enterOuterAlt(localctx, 1)
                self.state = 205
                self.match(javaSimplesParser.IDENTIFICADOR)
                pass
            elif token in [19, 20, 22]:
                self.enterOuterAlt(localctx, 2)
                self.state = 206
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 5767168) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                pass
            elif token in [4, 24]:
                self.enterOuterAlt(localctx, 3)
                self.state = 208
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==24:
                    self.state = 207
                    self.match(javaSimplesParser.OPERADOR_UNARIO_RELACIONAL)


                self.state = 210
                self.match(javaSimplesParser.T__3)
                self.state = 211
                self.expr_relacional()
                self.state = 212
                self.match(javaSimplesParser.T__4)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ComandoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def comando_if(self):
            return self.getTypedRuleContext(javaSimplesParser.Comando_ifContext,0)


        def comando_while(self):
            return self.getTypedRuleContext(javaSimplesParser.Comando_whileContext,0)


        def comando_scanf(self):
            return self.getTypedRuleContext(javaSimplesParser.Comando_scanfContext,0)


        def comando_print(self):
            return self.getTypedRuleContext(javaSimplesParser.Comando_printContext,0)


        def comando_atrib(self):
            return self.getTypedRuleContext(javaSimplesParser.Comando_atribContext,0)


        def comando_return(self):
            return self.getTypedRuleContext(javaSimplesParser.Comando_returnContext,0)


        def comando_break(self):
            return self.getTypedRuleContext(javaSimplesParser.Comando_breakContext,0)


        def chamada_funcao(self):
            return self.getTypedRuleContext(javaSimplesParser.Chamada_funcaoContext,0)


        def getRuleIndex(self):
            return javaSimplesParser.RULE_comando

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComando" ):
                listener.enterComando(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComando" ):
                listener.exitComando(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComando" ):
                return visitor.visitComando(self)
            else:
                return visitor.visitChildren(self)




    def comando(self):

        localctx = javaSimplesParser.ComandoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_comando)
        try:
            self.state = 226
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 216
                self.comando_if()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 217
                self.comando_while()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 218
                self.comando_scanf()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 219
                self.comando_print()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 220
                self.comando_atrib()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 221
                self.comando_return()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 222
                self.comando_break()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 223
                self.chamada_funcao()
                self.state = 224
                self.match(javaSimplesParser.T__8)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Comando_ifContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr_relacional(self):
            return self.getTypedRuleContext(javaSimplesParser.Expr_relacionalContext,0)


        def comando(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(javaSimplesParser.ComandoContext)
            else:
                return self.getTypedRuleContext(javaSimplesParser.ComandoContext,i)


        def getRuleIndex(self):
            return javaSimplesParser.RULE_comando_if

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComando_if" ):
                listener.enterComando_if(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComando_if" ):
                listener.exitComando_if(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComando_if" ):
                return visitor.visitComando_if(self)
            else:
                return visitor.visitChildren(self)




    def comando_if(self):

        localctx = javaSimplesParser.Comando_ifContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_comando_if)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 228
            self.match(javaSimplesParser.T__11)
            self.state = 229
            self.match(javaSimplesParser.T__3)
            self.state = 230
            self.expr_relacional()
            self.state = 231
            self.match(javaSimplesParser.T__4)
            self.state = 232
            self.match(javaSimplesParser.T__1)
            self.state = 236
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 2147995648) != 0):
                self.state = 233
                self.comando()
                self.state = 238
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 247
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==13:
                self.state = 239
                self.match(javaSimplesParser.T__12)
                self.state = 240
                self.match(javaSimplesParser.T__1)
                self.state = 244
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 2147995648) != 0):
                    self.state = 241
                    self.comando()
                    self.state = 246
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 249
            self.match(javaSimplesParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Comando_whileContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr_relacional(self):
            return self.getTypedRuleContext(javaSimplesParser.Expr_relacionalContext,0)


        def comando(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(javaSimplesParser.ComandoContext)
            else:
                return self.getTypedRuleContext(javaSimplesParser.ComandoContext,i)


        def getRuleIndex(self):
            return javaSimplesParser.RULE_comando_while

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComando_while" ):
                listener.enterComando_while(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComando_while" ):
                listener.exitComando_while(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComando_while" ):
                return visitor.visitComando_while(self)
            else:
                return visitor.visitChildren(self)




    def comando_while(self):

        localctx = javaSimplesParser.Comando_whileContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_comando_while)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 251
            self.match(javaSimplesParser.T__13)
            self.state = 252
            self.match(javaSimplesParser.T__3)
            self.state = 253
            self.expr_relacional()
            self.state = 254
            self.match(javaSimplesParser.T__4)
            self.state = 255
            self.match(javaSimplesParser.T__1)
            self.state = 257 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 256
                self.comando()
                self.state = 259 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 2147995648) != 0)):
                    break

            self.state = 261
            self.match(javaSimplesParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Comando_scanfContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def lista_de_var(self):
            return self.getTypedRuleContext(javaSimplesParser.Lista_de_varContext,0)


        def getRuleIndex(self):
            return javaSimplesParser.RULE_comando_scanf

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComando_scanf" ):
                listener.enterComando_scanf(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComando_scanf" ):
                listener.exitComando_scanf(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComando_scanf" ):
                return visitor.visitComando_scanf(self)
            else:
                return visitor.visitChildren(self)




    def comando_scanf(self):

        localctx = javaSimplesParser.Comando_scanfContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_comando_scanf)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 263
            self.match(javaSimplesParser.T__14)
            self.state = 264
            self.match(javaSimplesParser.T__3)
            self.state = 265
            self.lista_de_var()
            self.state = 266
            self.match(javaSimplesParser.T__4)
            self.state = 267
            self.match(javaSimplesParser.T__8)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Comando_atribContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFICADOR(self):
            return self.getToken(javaSimplesParser.IDENTIFICADOR, 0)

        def expressao(self):
            return self.getTypedRuleContext(javaSimplesParser.ExpressaoContext,0)


        def getRuleIndex(self):
            return javaSimplesParser.RULE_comando_atrib

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComando_atrib" ):
                listener.enterComando_atrib(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComando_atrib" ):
                listener.exitComando_atrib(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComando_atrib" ):
                return visitor.visitComando_atrib(self)
            else:
                return visitor.visitChildren(self)




    def comando_atrib(self):

        localctx = javaSimplesParser.Comando_atribContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_comando_atrib)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 269
            self.match(javaSimplesParser.IDENTIFICADOR)
            self.state = 270
            self.match(javaSimplesParser.T__10)
            self.state = 271
            self.expressao()
            self.state = 272
            self.match(javaSimplesParser.T__8)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Comando_printContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def lista_de_expressoes(self):
            return self.getTypedRuleContext(javaSimplesParser.Lista_de_expressoesContext,0)


        def getRuleIndex(self):
            return javaSimplesParser.RULE_comando_print

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComando_print" ):
                listener.enterComando_print(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComando_print" ):
                listener.exitComando_print(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComando_print" ):
                return visitor.visitComando_print(self)
            else:
                return visitor.visitChildren(self)




    def comando_print(self):

        localctx = javaSimplesParser.Comando_printContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_comando_print)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 274
            self.match(javaSimplesParser.T__15)
            self.state = 275
            self.match(javaSimplesParser.T__3)
            self.state = 276
            self.lista_de_expressoes()
            self.state = 277
            self.match(javaSimplesParser.T__4)
            self.state = 278
            self.match(javaSimplesParser.T__8)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Comando_breakContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return javaSimplesParser.RULE_comando_break

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComando_break" ):
                listener.enterComando_break(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComando_break" ):
                listener.exitComando_break(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComando_break" ):
                return visitor.visitComando_break(self)
            else:
                return visitor.visitChildren(self)




    def comando_break(self):

        localctx = javaSimplesParser.Comando_breakContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_comando_break)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 280
            self.match(javaSimplesParser.T__16)
            self.state = 281
            self.match(javaSimplesParser.T__8)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Comando_returnContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expressao(self):
            return self.getTypedRuleContext(javaSimplesParser.ExpressaoContext,0)


        def getRuleIndex(self):
            return javaSimplesParser.RULE_comando_return

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComando_return" ):
                listener.enterComando_return(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComando_return" ):
                listener.exitComando_return(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComando_return" ):
                return visitor.visitComando_return(self)
            else:
                return visitor.visitChildren(self)




    def comando_return(self):

        localctx = javaSimplesParser.Comando_returnContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_comando_return)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 283
            self.match(javaSimplesParser.T__17)
            self.state = 284
            self.expressao()
            self.state = 285
            self.match(javaSimplesParser.T__8)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Chamada_funcaoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFICADOR(self):
            return self.getToken(javaSimplesParser.IDENTIFICADOR, 0)

        def lista_de_var(self):
            return self.getTypedRuleContext(javaSimplesParser.Lista_de_varContext,0)


        def lista_de_expressoes(self):
            return self.getTypedRuleContext(javaSimplesParser.Lista_de_expressoesContext,0)


        def getRuleIndex(self):
            return javaSimplesParser.RULE_chamada_funcao

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterChamada_funcao" ):
                listener.enterChamada_funcao(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitChamada_funcao" ):
                listener.exitChamada_funcao(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitChamada_funcao" ):
                return visitor.visitChamada_funcao(self)
            else:
                return visitor.visitChildren(self)




    def chamada_funcao(self):

        localctx = javaSimplesParser.Chamada_funcaoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_chamada_funcao)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 287
            self.match(javaSimplesParser.IDENTIFICADOR)
            self.state = 288
            self.match(javaSimplesParser.T__3)
            self.state = 291
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,30,self._ctx)
            if la_ == 1:
                self.state = 289
                self.lista_de_var()

            elif la_ == 2:
                self.state = 290
                self.lista_de_expressoes()


            self.state = 293
            self.match(javaSimplesParser.T__4)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[12] = self.expr_aritimetica_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_aritimetica_sempred(self, localctx:Expr_aritimeticaContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         




