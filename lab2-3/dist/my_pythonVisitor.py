# Generated from my_python.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .my_pythonParser import my_pythonParser
else:
    from my_pythonParser import my_pythonParser

# This class defines a complete generic visitor for a parse tree produced by my_pythonParser.

class my_pythonVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by my_pythonParser#expression.
    def visitExpression(self, ctx:my_pythonParser.ExpressionContext):
        return self.visitChildren(ctx)



del my_pythonParser