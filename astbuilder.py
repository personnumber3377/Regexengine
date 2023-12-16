from grammar.regexVisitor import regexVisitor
from ast import *

'''
const EPSILON = Symbol("epsilon");
const ASTERISK = Symbol("*");
const PLUS = Symbol("+");
const OPTIONAL = Symbol("?");
const LAZY_ASTERISK = Symbol("*?");
const LAZY_PLUS = Symbol("+?");
const LAZY_OPTIONAL = Symbol("??");
'''

EPSILON = "epsilon"
ASTERISK = "*"
PLUS = "+"
OPTIONAL = "?"
LAZY_ASTERISK = "*?"
LAZY_PLUS = "+?"
LAZY_OPTIONAL = "??"

'''
const SHORTHAND_CHARACTER_CLASSES = {
    "\\d": new ComplexClass([], [new ComplexClassRange("0", "9")], "\d", false),
    "\\D": new ComplexClass([], [new ComplexClassRange("0", "9")], "\D", true),
    "\\w": new ComplexClass(["_"], [new ComplexClassRange("A", "Z"), new ComplexClassRange("a", "z"), new ComplexClassRange("0", "9")], "\w", false),
    "\\W": new ComplexClass(["_"], [new ComplexClassRange("A", "Z"), new ComplexClassRange("a", "z"), new ComplexClassRange("0", "9")], "\W", true),
    "\\s": new ComplexClass( [" ", "\f", "\n", "\r", "\t", "\v", "\u00a0", "\u1680", "\u2028","\u2029","\u202f", "\u205f", "\u3000", "\ufeff"],
       [new ComplexClassRange("\u2000", "\u200a")], "\s", false),
    "\\S": new ComplexClass( [" ", "\f", "\n", "\r", "\t", "\v", "\u00a0", "\u1680", "\u2028","\u2029","\u202f", "\u205f", "\u3000", "\ufeff"],
       [new ComplexClassRange("\u2000", "\u200a")], "\S", true),
};
'''

SHORTHAND_CHARACTER_CLASSES = {"\\d": ComplexClass([], [ComplexClassRange("0", "9")], "\d", False),
	"\\D": ComplexClass([], [ComplexClassRange("0", "9")], "\D", True),
	"\\w": ComplexClass(["_"], [ComplexClassRange("A", "Z"), ComplexClassRange("a", "z"), ComplexClassRange("0", "9")], "\w", False),
	"\\W": ComplexClass(["_"], [ComplexClassRange("A", "Z"), ComplexClassRange("a", "z"), ComplexClassRange("0", "9")], "\W", True),
	"\\s": ComplexClass([" ", "\f", "\n", "\r", "\t", "\v", "\u00a0", "\u1680", "\u2028", "\u2029", "\u202f", "\u205f", "\u3000", "\ufeff"],
		[ComplexClassRange("\u2000", "\u200a")], "\s", False),
	"\\S": ComplexClass([" ", "\f", "\n", "\r", "\t", "\v", "\u00a0", "\u1680", "\u2028", "\u2029", "\u202f", "\u205f", "\u3000", "\ufeff"],
		[ComplexClassRange("\u2000", "\u200a")], "\s", True),

}


ESPECIAL_ESCAPE_CHARACTERS = {"\\n": "\n", "\\b": "\b", "\\t": "\t"}

'''
class AstBuilder extends RegexVisitor {
'''

class AstBuilder(regexVisitor):
	'''
	visitMain(ctx) {
        return this.visit(ctx.regex());
    }
	'''
	def visitMain(self, ctx):
		thing = ctx.regex()
		#print("thing == "+str(thing))
		return self.visit(thing) # I have absolutely no idea what this does

	'''
	visitRegex(ctx) {
        if (ctx.alternative().length === 0)
            return new Regex(this.visit(ctx.expr()));
        else {
            const main = ctx.expr().length === 0 ? this._epsilonAlternative() : new Regex(this.visit(ctx.expr()));
            const alternatives = this.visit(ctx.alternative());
            main.nonCapturing();
            alternatives.forEach(x => x.nonCapturing());
            return new RegexAlternative(main,  ...alternatives);
        }
    }
	'''

	def visitRegex(self, ctx):
		#print("ctx.alternative() == "+str(ctx.alternative()))
		if len(ctx.alternative()) == 0:
			#return Regex(self.visit(ctx.expr()))
			oof = ctx.expr()
			#print("oof == "+str(oof))
			#print("type(oof) == "+str(type(oof)))
			#oof = oof[0]
			poopoo = self.visit(oof)
			return Regex(poopoo)
		else:
			if len(ctx.expr()) == 0:
				main = self._epsilonAlternative()
			else:
				main = Regex(self.visit(ctx.expr()))
			alternatives = self.visit(ctx.alternative())
			main.nonCapturing()
			for x in alternatives:
				x.nonCapturing()
			return RegexAlternative([main, alternatives]) # I think this is right

	'''
	visitAlternative(ctx) {
        if (ctx.expr().length !== 0)
            return new Regex(this.visit(ctx.expr()));
        else 
            return this._epsilonAlternative();
    }
	'''

	def visitAlternative(self, ctx):
		if len(ctx.expr()) != 0:
			return Regex(self.visit(ctx.expr()))
		else:
			return self._epsilonAlternative()

	'''
	_epsilonAlternative() {
        return new Regex([new Expression(null,new AtomicPattern(EPSILON))]);
    }
	'''

	def _epsilonAlternative(self):
		return Regex([Expression(None, AtomicPattern(EPSILON))])

	'''
	visitExpr(ctx) {
        return new Expression(ctx.quantifier() ? this.visit(ctx.quantifier()) : null, this.visit(ctx.subexpr()));
    }
	'''

	def visitExpr(self, ctx):
		if ctx.quantifier():
			return Expression(self.visit(ctx.quantifier()), self.visit(ctx.subexpr()))
		else:
			return Expression(None, self.visit(ctx.subexpr()))

	'''
	visitAtomicPattern(ctx) {
        return new AtomicPattern(ctx.getText());
    }
	'''

	def visitAtomicPattern(self, ctx):
		return AtomicPattern(ctx.getText())

	'''
	visitEscapedReservedAtomicPattern(ctx) {
        const char = ctx.getText();
        const pattern = char in ESPECIAL_ESCAPE_CHARACTERS ? ESPECIAL_ESCAPE_CHARACTERS[char] : char.substring(1); 
        return new AtomicPattern(pattern);
    }
	'''

	def visitEscapedReservedAtomicPattern(self, ctx):
		char = ctx.getText()
		if char in ESPECIAL_ESCAPE_CHARACTERS:
			pattern = ESPECIAL_ESCAPE_CHARACTERS[char]
		else:
			# Thanks to https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/substr
			pattern = char[1:]
		return AtomicPattern(pattern)

	'''
    visitCharacterClass(ctx) {
        const txt = ctx.getText();
        return SHORTHAND_CHARACTER_CLASSES[txt];
    }
	'''

	def visitCharacterClass(self, ctx) -> None:
		txt = ctx.getText()
		assert txt in SHORTHAND_CHARACTER_CLASSES
		return SHORTHAND_CHARACTER_CLASSES[txt]

	'''
	visitComplexCharacterClass(ctx) {
        const negated = Boolean(ctx.negated);
        const children = this.visit(ctx.complexCCPiece());
        const single = [];
        const ranges = [];
        for (const c of children) {
           single.push(...c.singles);
           ranges.push(...c.ranges);
        }
        return new ComplexClass(single, ranges, ctx.getText(), negated);
    }
	'''

	def visitComplexCharacterClass(self, ctx):
		negated = bool(ctx.negated)
		children = self.visit(ctx.complexCCPiece())
		single = []
		ranges = []
		for c in children:
			for x in c.singles:
				single.append(x)
			for x in c.ranges:
				ranges.append(x)

		return ComplexClass(single, ranges, ctx.getText(), negated)

	'''
	visitCcPiece_Respone(ctx) {
        const piece = this.visit(ctx.allowedCharInCharacterClass());
        const base =  {singles: [], ranges: []};
        if (piece.length === 1)
            base.singles.push(piece[0]);
        else 
            base.ranges.push(new ComplexClassRange(piece[0], piece[1]));
        return base;   
    }
	'''

	def visitCcPiece_Respone(self, ctx):
		piece = sefl.visit(ctx.allowedCharInCharacterClass())
		base = [[], []]
		if len(piece) == 1:
			base[0].append(piece[0])
		else:
			base[1],append(ComplexClassRange(piece[0], piece[1]))
		return base

	'''
	visitCcPiece_Escape(ctx) {
        const txt = ctx.getText();
        const base = {singles: [], ranges: []};
        base.ranges.push(SHORTHAND_CHARACTER_CLASSES[txt]);
        return base;
    }
	'''

	def visitCcPiece_Escape(self, ctx):
		txt = ctx.getText()
		base = [[],[]]
		base[1].append(SHORTHAND_CHARACTER_CLASSES[txt])
		return base

	'''
	visitDotPattern() {
        return new ComplexClass(["\n", "\r"], [], true, ".");
    }

    visitDollarAnchor() {
        return new DollarAnchor();
    }

    visitCaretAnchor() {
        return new CaretAnchor();
    }
  
    visitComplexClass(ctx) {
       return this.visit(ctx.complexCharacterClass());
    }
	'''

	def visitDotPattern(self):
		return ComplexClass(["\n", "\r"], [], True, ".")
	def visitDollarAnchor(self):
		return DollarAnchor()
	def visitCaretAnchor(self):
		return CaretAnchor()
	def visitComplexClass(self, ctx):
		return self.visit(ctx.complexCharacterClass())

	'''
	visitBackreference(ctx) {
        const [_, group] = /\\([0-9]+)/.exec(ctx.getText());
        return new Backreference(Number(group));
    }

    visitAllowedCharInCharacterClass(ctx) {
        const txt = ctx.getText();
        return txt[0] === "\\" ? txt.substring(1) : txt;
    }
	'''

	def visitBackreference(self, ctx):
		regex_string = r"\\([0-9]+)"
		matcher = re.compile(regex_string)
		group = matcher.match(ctx.getText()).group()
		if group[0] == "\\":
			group = group[1:]
		return int(group)

	def visitAllowedCharInCharacterClass(self, ctx):
		txt = ctx.getText()
		if txt[0] == "\\":
			return txt[1:]
		else:
			return txt

	'''
	visitAsteriskQuantifier() {
        return ASTERISK;
    }

    visitQuestionQuantifier() {
        return OPTIONAL;
    }

    visitLazyAsteriskQuantifier() {
        return LAZY_ASTERISK;
    }

    visitLazyPlusQuantifier() {
        return LAZY_PLUS;
    }

    visitLazyQuestionQuantifier() {
        return LAZY_OPTIONAL;
    }
    
    visitGroupPattern(ctx) {
        return this.visit(ctx.regexGroup());
    }
	'''
	
	def visitAsteriskQuantifier(self):
		return ASTERISK
	def visitQuestionQuantifier(self):
		return OPTIONAL
	def visitLazyAsteriskQuantifier(self):
		return LAZY_ASTERISK
	def visitLazyPlusQuantifier(self):
		return LAZY_PLUS
	def visitLazyQuestionQuantifier(self):

		return LAZY_OPTIONAL
	def visitGroupPattern(self, ctx):
		return self.visit(ctx.regexGroup())

	'''
	visitRegexGroup(ctx) {
        const alternative = this.visit(ctx.regex());
        alternative.groupName = ctx.name.map(x => x.text).join("");
        if (ctx.nonCapture) alternative.nonCapturing();
        if (ctx.atomic) alternative.atomic();
        return alternative;
    }

    visitPlusQuantifier() {
        return PLUS;
    }
	'''

	def visitRegexGroup(self, ctx):
		alternative = self.visit(ctx.regex())
		#print("alternative == "+str(alternative))
		final_name = ""
		for thing in ctx.name:
			final_name += thing.text
		alternative.groupName = final_name
		if ctx.nonCapture:
			alternative.nonCapturing()
		if ctx.atomic:
			alternative.atomic()
		return alternative
	def visitPlusQuantifier(self):
		return PLUS
