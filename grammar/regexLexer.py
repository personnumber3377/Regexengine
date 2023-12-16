# Generated from regex.g4 by ANTLR 4.7.2
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\26")
        buf.write("g\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\3\2\3\2\3\3\3\3\3\4\3\4\3\4\3\4\3")
        buf.write("\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\5\4?\n\4\3")
        buf.write("\5\3\5\6\5C\n\5\r\5\16\5D\3\6\3\6\3\6\3\7\3\7\3\b\3\b")
        buf.write("\3\t\3\t\3\n\3\n\3\13\3\13\3\f\3\f\3\r\3\r\3\16\3\16\3")
        buf.write("\17\3\17\3\20\3\20\3\21\3\21\3\22\3\22\3\23\3\23\3\24")
        buf.write("\3\24\3\25\3\25\2\2\26\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21")
        buf.write("\n\23\13\25\f\27\r\31\16\33\17\35\20\37\21!\22#\23%\24")
        buf.write("\'\25)\26\3\2\5\6\2ddppttvv\3\2\62;\b\2FFUUYYffuuyy\2")
        buf.write("t\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13")
        buf.write("\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3")
        buf.write("\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2")
        buf.write("\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2")
        buf.write("%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\3+\3\2\2\2\5-\3\2\2\2")
        buf.write("\7/\3\2\2\2\t@\3\2\2\2\13F\3\2\2\2\rI\3\2\2\2\17K\3\2")
        buf.write("\2\2\21M\3\2\2\2\23O\3\2\2\2\25Q\3\2\2\2\27S\3\2\2\2\31")
        buf.write("U\3\2\2\2\33W\3\2\2\2\35Y\3\2\2\2\37[\3\2\2\2!]\3\2\2")
        buf.write("\2#_\3\2\2\2%a\3\2\2\2\'c\3\2\2\2)e\3\2\2\2+,\7~\2\2,")
        buf.write("\4\3\2\2\2-.\7^\2\2.\6\3\2\2\2/>\5\5\3\2\60?\5\5\3\2\61")
        buf.write("?\5\r\7\2\62?\5\17\b\2\63?\5\21\t\2\64?\5\23\n\2\65?\5")
        buf.write("\25\13\2\66?\5\31\r\2\67?\5\33\16\28?\5\37\20\29?\5!\21")
        buf.write("\2:?\5#\22\2;?\5%\23\2<?\5\'\24\2=?\t\2\2\2>\60\3\2\2")
        buf.write("\2>\61\3\2\2\2>\62\3\2\2\2>\63\3\2\2\2>\64\3\2\2\2>\65")
        buf.write("\3\2\2\2>\66\3\2\2\2>\67\3\2\2\2>8\3\2\2\2>9\3\2\2\2>")
        buf.write(":\3\2\2\2>;\3\2\2\2><\3\2\2\2>=\3\2\2\2?\b\3\2\2\2@B\5")
        buf.write("\5\3\2AC\t\3\2\2BA\3\2\2\2CD\3\2\2\2DB\3\2\2\2DE\3\2\2")
        buf.write("\2E\n\3\2\2\2FG\5\5\3\2GH\t\4\2\2H\f\3\2\2\2IJ\7*\2\2")
        buf.write("J\16\3\2\2\2KL\7+\2\2L\20\3\2\2\2MN\7,\2\2N\22\3\2\2\2")
        buf.write("OP\7-\2\2P\24\3\2\2\2QR\7\60\2\2R\26\3\2\2\2ST\7A\2\2")
        buf.write("T\30\3\2\2\2UV\7]\2\2V\32\3\2\2\2WX\7_\2\2X\34\3\2\2\2")
        buf.write("YZ\7/\2\2Z\36\3\2\2\2[\\\7@\2\2\\ \3\2\2\2]^\7>\2\2^\"")
        buf.write("\3\2\2\2_`\7<\2\2`$\3\2\2\2ab\7`\2\2b&\3\2\2\2cd\7&\2")
        buf.write("\2d(\3\2\2\2ef\13\2\2\2f*\3\2\2\2\5\2>D\2")
        return buf.getvalue()


class regexLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    BACKSLASH = 2
    ESCAPED_RESERVED_CHAR = 3
    BACKREFERENCE = 4
    CHARACTER_CLASS = 5
    OPEN_PAR = 6
    CLOSE_PAR = 7
    ASTERISK = 8
    PLUS = 9
    DOT = 10
    QUESTION_MARK = 11
    OPEN_BRACKET = 12
    CLOSE_BRACKET = 13
    DASH = 14
    GREATER_THAN = 15
    LOWER_THAN = 16
    COLON = 17
    CARET = 18
    DOLLAR = 19
    CHAR = 20

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'|'", "'\\'", "'('", "')'", "'*'", "'+'", "'.'", "'?'", "'['", 
            "']'", "'-'", "'>'", "'<'", "':'", "'^'", "'$'" ]

    symbolicNames = [ "<INVALID>",
            "BACKSLASH", "ESCAPED_RESERVED_CHAR", "BACKREFERENCE", "CHARACTER_CLASS", 
            "OPEN_PAR", "CLOSE_PAR", "ASTERISK", "PLUS", "DOT", "QUESTION_MARK", 
            "OPEN_BRACKET", "CLOSE_BRACKET", "DASH", "GREATER_THAN", "LOWER_THAN", 
            "COLON", "CARET", "DOLLAR", "CHAR" ]

    ruleNames = [ "T__0", "BACKSLASH", "ESCAPED_RESERVED_CHAR", "BACKREFERENCE", 
                  "CHARACTER_CLASS", "OPEN_PAR", "CLOSE_PAR", "ASTERISK", 
                  "PLUS", "DOT", "QUESTION_MARK", "OPEN_BRACKET", "CLOSE_BRACKET", 
                  "DASH", "GREATER_THAN", "LOWER_THAN", "COLON", "CARET", 
                  "DOLLAR", "CHAR" ]

    grammarFileName = "regex.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


