
import antlr4
from grammar.regexLexer import *
from grammar.regexParser import *
from astbuilder import *



'''
This file is basically just this:


const antlr4 = require('antlr4');
const { ErrorListener } = require('antlr4/error');
const { AstBuilder } = require('./astBuilder');
const {regexLexer: RegexLexer} = require('./generated/regexLexer');
const {regexParser: RegexParser} = require('./generated/regexParser');

class CustomErrorListener extends ErrorListener {
    syntaxError(recognizer, offendingSymbol, line, column, msg, e) {
        console.log(msg);
        throw Error(msg);
    }
}
function parseRegex(regex) {
    const chars = new antlr4.InputStream(regex)
    const lexer = new RegexLexer(chars)
    const tokens  = new antlr4.CommonTokenStream(lexer)
    const parser = new RegexParser(tokens)
    parser.buildParseTrees = true;
    parser.addErrorListener(new CustomErrorListener());
    const tree = parser.main();
    return new AstBuilder().visit(tree);
}

module.exports = parseRegex;
'''



'''

const CASES = [
    ["aaaa", "aaa"],
    ["aaaa", "aaaa"],
    ["a+", "aaaa"],
    ["(a|b)+", "abbabasbababababab"],
    ["(a|b)+c*", "abababacccc"],
    ["(a|b)+c*", "abababa"],
    ["a+c?b+", "acb"],
    ["a+c?b+", "accb"],
    ["a(|)b", "ab"],
];
'''
CASES = [
    ["aaaa", "aaa"],
    ["aaaa", "aaaa"],
    ["a+", "aaaa"],
    ["(a|b)+", "abbabasbababababab"],
    ["(a|b)+c*", "abababacccc"],
    ["(a|b)+c*", "abababa"],
    ["a+c?b+", "acb"],
    ["a+c?b+", "accb"],
    ["a(|)b", "ab"],
];


def parseRegex(regex: str):

    chars = antlr4.InputStream(regex)
    #print("chars == "+str(chars))
    #print("Type of chars: "+str(type(chars)))
    lexer = regexLexer(chars)
    #print("Lexer: "+str(lexer))
    # const tokens  = new antlr4.CommonTokenStream(lexer)
    tokens = antlr4.CommonTokenStream(lexer)
    parser = regexParser(tokens)
    #print("parser == "+str(parser))
    # parser.buildParseTrees = true;
    parser.buildParseTrees = True
    # const tree = parser.main();
    tree = parser.main()
    # return new AstBuilder().visit(tree);
    #print(tree.toStringTree(recog=parser))
    #print("AstBuilder() == "+str(AstBuilder()))
    return AstBuilder().visit(tree)

def main() -> int:
    #parseRegex("a+")
    for thing in CASES:
        testcase = thing[0]
        print("Now trying "+str(testcase))
        parseRegex(testcase)
    return 0


if __name__=="__main__":
    exit(main())
