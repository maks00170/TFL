# Generated from my_python.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .my_pythonParser import my_pythonParser
else:
    from my_pythonParser import my_pythonParser

# This class defines a complete listener for a parse tree produced by my_pythonParser.
class my_pythonListener(ParseTreeListener):

    # Enter a parse tree produced by my_pythonParser#expression.
    def enterExpression(self, ctx:my_pythonParser.ExpressionContext):
        pass

    # Exit a parse tree produced by my_pythonParser#expression.
    def exitExpression(self, ctx:my_pythonParser.ExpressionContext):
        pass



del my_pythonParser