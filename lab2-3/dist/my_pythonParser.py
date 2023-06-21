# Generated from my_python.g4 by ANTLR 4.9.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\21")
        buf.write("\33\4\2\t\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3")
        buf.write("\2\3\2\5\2\21\n\2\3\2\3\2\3\2\7\2\26\n\2\f\2\16\2\31\13")
        buf.write("\2\3\2\2\3\2\3\2\2\2\2!\2\20\3\2\2\2\4\5\b\2\1\2\5\6\7")
        buf.write("\3\2\2\6\7\5\2\2\2\7\b\7\4\2\2\b\21\3\2\2\2\t\21\7\5\2")
        buf.write("\2\n\21\7\6\2\2\13\21\7\t\2\2\f\21\7\n\2\2\r\21\7\7\2")
        buf.write("\2\16\21\7\f\2\2\17\21\7\20\2\2\20\4\3\2\2\2\20\t\3\2")
        buf.write("\2\2\20\n\3\2\2\2\20\13\3\2\2\2\20\f\3\2\2\2\20\r\3\2")
        buf.write("\2\2\20\16\3\2\2\2\20\17\3\2\2\2\21\27\3\2\2\2\22\23\f")
        buf.write("\n\2\2\23\24\7\b\2\2\24\26\5\2\2\13\25\22\3\2\2\2\26\31")
        buf.write("\3\2\2\2\27\25\3\2\2\2\27\30\3\2\2\2\30\3\3\2\2\2\31\27")
        buf.write("\3\2\2\2\4\20\27")
        return buf.getvalue()


class my_pythonParser ( Parser ):

    grammarFileName = "my_python.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'('", "')'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "INT", "REAL", 
                      "STRING", "SIGN", "BOOL", "NEGATIVE", "INDEX", "DICT", 
                      "NOT_LAST_PAIR", "LAST_PAIR", "LIST_ELEMENT", "LIST", 
                      "SPACES" ]

    RULE_expression = 0

    ruleNames =  [ "expression" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    INT=3
    REAL=4
    STRING=5
    SIGN=6
    BOOL=7
    NEGATIVE=8
    INDEX=9
    DICT=10
    NOT_LAST_PAIR=11
    LAST_PAIR=12
    LIST_ELEMENT=13
    LIST=14
    SPACES=15

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(my_pythonParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(my_pythonParser.ExpressionContext,i)


        def INT(self):
            return self.getToken(my_pythonParser.INT, 0)

        def REAL(self):
            return self.getToken(my_pythonParser.REAL, 0)

        def BOOL(self):
            return self.getToken(my_pythonParser.BOOL, 0)

        def NEGATIVE(self):
            return self.getToken(my_pythonParser.NEGATIVE, 0)

        def STRING(self):
            return self.getToken(my_pythonParser.STRING, 0)

        def DICT(self):
            return self.getToken(my_pythonParser.DICT, 0)

        def LIST(self):
            return self.getToken(my_pythonParser.LIST, 0)

        def SIGN(self):
            return self.getToken(my_pythonParser.SIGN, 0)

        def getRuleIndex(self):
            return my_pythonParser.RULE_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression" ):
                listener.enterExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression" ):
                listener.exitExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression" ):
                return visitor.visitExpression(self)
            else:
                return visitor.visitChildren(self)



    def expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = my_pythonParser.ExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 0
        self.enterRecursionRule(localctx, 0, self.RULE_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 14
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [my_pythonParser.T__0]:
                self.state = 3
                self.match(my_pythonParser.T__0)
                self.state = 4
                self.expression(0)
                self.state = 5
                self.match(my_pythonParser.T__1)
                pass
            elif token in [my_pythonParser.INT]:
                self.state = 7
                self.match(my_pythonParser.INT)
                pass
            elif token in [my_pythonParser.REAL]:
                self.state = 8
                self.match(my_pythonParser.REAL)
                pass
            elif token in [my_pythonParser.BOOL]:
                self.state = 9
                self.match(my_pythonParser.BOOL)
                pass
            elif token in [my_pythonParser.NEGATIVE]:
                self.state = 10
                self.match(my_pythonParser.NEGATIVE)
                pass
            elif token in [my_pythonParser.STRING]:
                self.state = 11
                self.match(my_pythonParser.STRING)
                pass
            elif token in [my_pythonParser.DICT]:
                self.state = 12
                self.match(my_pythonParser.DICT)
                pass
            elif token in [my_pythonParser.LIST]:
                self.state = 13
                self.match(my_pythonParser.LIST)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 21
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,1,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = my_pythonParser.ExpressionContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                    self.state = 16
                    if not self.precpred(self._ctx, 8):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                    self.state = 17
                    self.match(my_pythonParser.SIGN)
                    self.state = 18
                    self.expression(9) 
                self.state = 23
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,1,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[0] = self.expression_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expression_sempred(self, localctx:ExpressionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 8)
         




