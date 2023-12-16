# Generated from regex.g4 by ANTLR 4.7.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .regexParser import regexParser
else:
    from regexParser import regexParser

# This class defines a complete generic visitor for a parse tree produced by regexParser.

class regexVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by regexParser#main.
    def visitMain(self, ctx:regexParser.MainContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by regexParser#regex.
    def visitRegex(self, ctx:regexParser.RegexContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by regexParser#alternative.
    def visitAlternative(self, ctx:regexParser.AlternativeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by regexParser#expr.
    def visitExpr(self, ctx:regexParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by regexParser#groupPattern.
    def visitGroupPattern(self, ctx:regexParser.GroupPatternContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by regexParser#atomicPattern.
    def visitAtomicPattern(self, ctx:regexParser.AtomicPatternContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by regexParser#escapedReservedAtomicPattern.
    def visitEscapedReservedAtomicPattern(self, ctx:regexParser.EscapedReservedAtomicPatternContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by regexParser#characterClass.
    def visitCharacterClass(self, ctx:regexParser.CharacterClassContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by regexParser#ComplexClass.
    def visitComplexClass(self, ctx:regexParser.ComplexClassContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by regexParser#backreference.
    def visitBackreference(self, ctx:regexParser.BackreferenceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by regexParser#dollarAnchor.
    def visitDollarAnchor(self, ctx:regexParser.DollarAnchorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by regexParser#caretAnchor.
    def visitCaretAnchor(self, ctx:regexParser.CaretAnchorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by regexParser#dotPattern.
    def visitDotPattern(self, ctx:regexParser.DotPatternContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by regexParser#regexGroup.
    def visitRegexGroup(self, ctx:regexParser.RegexGroupContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by regexParser#complexCharacterClass.
    def visitComplexCharacterClass(self, ctx:regexParser.ComplexCharacterClassContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by regexParser#ccPiece_Respone.
    def visitCcPiece_Respone(self, ctx:regexParser.CcPiece_ResponeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by regexParser#ccPiece_Escape.
    def visitCcPiece_Escape(self, ctx:regexParser.CcPiece_EscapeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by regexParser#allowedCharInCharacterClass.
    def visitAllowedCharInCharacterClass(self, ctx:regexParser.AllowedCharInCharacterClassContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by regexParser#atomicChar.
    def visitAtomicChar(self, ctx:regexParser.AtomicCharContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by regexParser#asteriskQuantifier.
    def visitAsteriskQuantifier(self, ctx:regexParser.AsteriskQuantifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by regexParser#plusQuantifier.
    def visitPlusQuantifier(self, ctx:regexParser.PlusQuantifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by regexParser#questionQuantifier.
    def visitQuestionQuantifier(self, ctx:regexParser.QuestionQuantifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by regexParser#lazyAsteriskQuantifier.
    def visitLazyAsteriskQuantifier(self, ctx:regexParser.LazyAsteriskQuantifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by regexParser#lazyPlusQuantifier.
    def visitLazyPlusQuantifier(self, ctx:regexParser.LazyPlusQuantifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by regexParser#lazyQuestionQuantifier.
    def visitLazyQuestionQuantifier(self, ctx:regexParser.LazyQuestionQuantifierContext):
        return self.visitChildren(ctx)



del regexParser