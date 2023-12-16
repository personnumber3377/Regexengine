# Generated from regex.g4 by ANTLR 4.7.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .regexParser import regexParser
else:
    from regexParser import regexParser

# This class defines a complete listener for a parse tree produced by regexParser.
class regexListener(ParseTreeListener):

    # Enter a parse tree produced by regexParser#main.
    def enterMain(self, ctx:regexParser.MainContext):
        pass

    # Exit a parse tree produced by regexParser#main.
    def exitMain(self, ctx:regexParser.MainContext):
        pass


    # Enter a parse tree produced by regexParser#regex.
    def enterRegex(self, ctx:regexParser.RegexContext):
        pass

    # Exit a parse tree produced by regexParser#regex.
    def exitRegex(self, ctx:regexParser.RegexContext):
        pass


    # Enter a parse tree produced by regexParser#alternative.
    def enterAlternative(self, ctx:regexParser.AlternativeContext):
        pass

    # Exit a parse tree produced by regexParser#alternative.
    def exitAlternative(self, ctx:regexParser.AlternativeContext):
        pass


    # Enter a parse tree produced by regexParser#expr.
    def enterExpr(self, ctx:regexParser.ExprContext):
        pass

    # Exit a parse tree produced by regexParser#expr.
    def exitExpr(self, ctx:regexParser.ExprContext):
        pass


    # Enter a parse tree produced by regexParser#groupPattern.
    def enterGroupPattern(self, ctx:regexParser.GroupPatternContext):
        pass

    # Exit a parse tree produced by regexParser#groupPattern.
    def exitGroupPattern(self, ctx:regexParser.GroupPatternContext):
        pass


    # Enter a parse tree produced by regexParser#atomicPattern.
    def enterAtomicPattern(self, ctx:regexParser.AtomicPatternContext):
        pass

    # Exit a parse tree produced by regexParser#atomicPattern.
    def exitAtomicPattern(self, ctx:regexParser.AtomicPatternContext):
        pass


    # Enter a parse tree produced by regexParser#escapedReservedAtomicPattern.
    def enterEscapedReservedAtomicPattern(self, ctx:regexParser.EscapedReservedAtomicPatternContext):
        pass

    # Exit a parse tree produced by regexParser#escapedReservedAtomicPattern.
    def exitEscapedReservedAtomicPattern(self, ctx:regexParser.EscapedReservedAtomicPatternContext):
        pass


    # Enter a parse tree produced by regexParser#characterClass.
    def enterCharacterClass(self, ctx:regexParser.CharacterClassContext):
        pass

    # Exit a parse tree produced by regexParser#characterClass.
    def exitCharacterClass(self, ctx:regexParser.CharacterClassContext):
        pass


    # Enter a parse tree produced by regexParser#ComplexClass.
    def enterComplexClass(self, ctx:regexParser.ComplexClassContext):
        pass

    # Exit a parse tree produced by regexParser#ComplexClass.
    def exitComplexClass(self, ctx:regexParser.ComplexClassContext):
        pass


    # Enter a parse tree produced by regexParser#backreference.
    def enterBackreference(self, ctx:regexParser.BackreferenceContext):
        pass

    # Exit a parse tree produced by regexParser#backreference.
    def exitBackreference(self, ctx:regexParser.BackreferenceContext):
        pass


    # Enter a parse tree produced by regexParser#dollarAnchor.
    def enterDollarAnchor(self, ctx:regexParser.DollarAnchorContext):
        pass

    # Exit a parse tree produced by regexParser#dollarAnchor.
    def exitDollarAnchor(self, ctx:regexParser.DollarAnchorContext):
        pass


    # Enter a parse tree produced by regexParser#caretAnchor.
    def enterCaretAnchor(self, ctx:regexParser.CaretAnchorContext):
        pass

    # Exit a parse tree produced by regexParser#caretAnchor.
    def exitCaretAnchor(self, ctx:regexParser.CaretAnchorContext):
        pass


    # Enter a parse tree produced by regexParser#dotPattern.
    def enterDotPattern(self, ctx:regexParser.DotPatternContext):
        pass

    # Exit a parse tree produced by regexParser#dotPattern.
    def exitDotPattern(self, ctx:regexParser.DotPatternContext):
        pass


    # Enter a parse tree produced by regexParser#regexGroup.
    def enterRegexGroup(self, ctx:regexParser.RegexGroupContext):
        pass

    # Exit a parse tree produced by regexParser#regexGroup.
    def exitRegexGroup(self, ctx:regexParser.RegexGroupContext):
        pass


    # Enter a parse tree produced by regexParser#complexCharacterClass.
    def enterComplexCharacterClass(self, ctx:regexParser.ComplexCharacterClassContext):
        pass

    # Exit a parse tree produced by regexParser#complexCharacterClass.
    def exitComplexCharacterClass(self, ctx:regexParser.ComplexCharacterClassContext):
        pass


    # Enter a parse tree produced by regexParser#ccPiece_Respone.
    def enterCcPiece_Respone(self, ctx:regexParser.CcPiece_ResponeContext):
        pass

    # Exit a parse tree produced by regexParser#ccPiece_Respone.
    def exitCcPiece_Respone(self, ctx:regexParser.CcPiece_ResponeContext):
        pass


    # Enter a parse tree produced by regexParser#ccPiece_Escape.
    def enterCcPiece_Escape(self, ctx:regexParser.CcPiece_EscapeContext):
        pass

    # Exit a parse tree produced by regexParser#ccPiece_Escape.
    def exitCcPiece_Escape(self, ctx:regexParser.CcPiece_EscapeContext):
        pass


    # Enter a parse tree produced by regexParser#allowedCharInCharacterClass.
    def enterAllowedCharInCharacterClass(self, ctx:regexParser.AllowedCharInCharacterClassContext):
        pass

    # Exit a parse tree produced by regexParser#allowedCharInCharacterClass.
    def exitAllowedCharInCharacterClass(self, ctx:regexParser.AllowedCharInCharacterClassContext):
        pass


    # Enter a parse tree produced by regexParser#atomicChar.
    def enterAtomicChar(self, ctx:regexParser.AtomicCharContext):
        pass

    # Exit a parse tree produced by regexParser#atomicChar.
    def exitAtomicChar(self, ctx:regexParser.AtomicCharContext):
        pass


    # Enter a parse tree produced by regexParser#asteriskQuantifier.
    def enterAsteriskQuantifier(self, ctx:regexParser.AsteriskQuantifierContext):
        pass

    # Exit a parse tree produced by regexParser#asteriskQuantifier.
    def exitAsteriskQuantifier(self, ctx:regexParser.AsteriskQuantifierContext):
        pass


    # Enter a parse tree produced by regexParser#plusQuantifier.
    def enterPlusQuantifier(self, ctx:regexParser.PlusQuantifierContext):
        pass

    # Exit a parse tree produced by regexParser#plusQuantifier.
    def exitPlusQuantifier(self, ctx:regexParser.PlusQuantifierContext):
        pass


    # Enter a parse tree produced by regexParser#questionQuantifier.
    def enterQuestionQuantifier(self, ctx:regexParser.QuestionQuantifierContext):
        pass

    # Exit a parse tree produced by regexParser#questionQuantifier.
    def exitQuestionQuantifier(self, ctx:regexParser.QuestionQuantifierContext):
        pass


    # Enter a parse tree produced by regexParser#lazyAsteriskQuantifier.
    def enterLazyAsteriskQuantifier(self, ctx:regexParser.LazyAsteriskQuantifierContext):
        pass

    # Exit a parse tree produced by regexParser#lazyAsteriskQuantifier.
    def exitLazyAsteriskQuantifier(self, ctx:regexParser.LazyAsteriskQuantifierContext):
        pass


    # Enter a parse tree produced by regexParser#lazyPlusQuantifier.
    def enterLazyPlusQuantifier(self, ctx:regexParser.LazyPlusQuantifierContext):
        pass

    # Exit a parse tree produced by regexParser#lazyPlusQuantifier.
    def exitLazyPlusQuantifier(self, ctx:regexParser.LazyPlusQuantifierContext):
        pass


    # Enter a parse tree produced by regexParser#lazyQuestionQuantifier.
    def enterLazyQuestionQuantifier(self, ctx:regexParser.LazyQuestionQuantifierContext):
        pass

    # Exit a parse tree produced by regexParser#lazyQuestionQuantifier.
    def exitLazyQuestionQuantifier(self, ctx:regexParser.LazyQuestionQuantifierContext):
        pass


