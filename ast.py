


'''
class Regex {
    constructor(subpatterns) {
        this.subpatterns = subpatterns;
        this.groupName = null;
        this._capturing = true;
        this._atomic = false;
       }

    isCapturingGroup() {
        return this._capturing;
    }

    nonCapturing() {
        this._capturing = false;
        return this;
    }

    isAtomic() {
        return this._atomic;
    }

    atomic() {
        this._atomic = true;
        this._capturing = false;
        return this;
    }
}

class Expression {

    constructor(quantifier, child) {
        this.quantifier = quantifier;
        this.child = child;
    }
}

class RegexAlternative {
    /**
     * 
     * @param {*} groupName Null if it's not a named group.
     * @param  {...any} alternatives 
     */
    constructor(...alternatives) {
        this.groupName = null;
        this._capturing = true;
        this.alternatives = alternatives;
        this._atomic = false;
    }

    isCapturingGroup() {
        return this._capturing;
    }

    nonCapturing() {
        this._capturing = false;
        return this;
    }

    isAtomic() {
        return this._atomic;
    }
    
    atomic() {
        this._atomic = true;
        this._capturing = false;
        return this;
    }
}

class AtomicPattern {
    constructor(char) {
        this.char = char;
    }
}

class DotPattern {
}


class ComplexClassRange {
    constructor(start, end) {
        this.start = start;
        this.end = end;
    }

    matches(c) {
        return c >= this.start && this.end >= c;
    }
}

class ComplexClass {
    constructor(individialChars, ranges, name, negated) {
        this.chars = individialChars;
        this.ranges = ranges;
        this.name = name;
        this.negated = negated;
    }

    matches(c) {
        const base = this.chars.includes(c) || this.ranges.some(x => x.matches(c));
        return this.negated ? !base : base;
    }
}


class DollarAnchor {

}

class CaretAnchor {
    
}

class Backreference {
    constructor(group) {
        this.group = group;
    }
}
'''


'''
class Regex {
    constructor(subpatterns) {
        this.subpatterns = subpatterns;
        this.groupName = null;
        this._capturing = true;
        this._atomic = false;
       }

    isCapturingGroup() {
        return this._capturing;
    }

    nonCapturing() {
        this._capturing = false;
        return this;
    }

    isAtomic() {
        return this._atomic;
    }

    atomic() {
        this._atomic = true;
        this._capturing = false;
        return this;
    }
}
'''

class Regex:
	def __init__(self, subpatterns) -> None:
		self.subpatterns = subpatterns
		self.groupName = None
		self._capturing = True
		self._atomic = False
	def isCapturingGroup(self) -> bool:
		return self._capturing
	def nonCapturing(self):
		self._capturing = False
		return self
	def isAtomic(self) -> bool:
		return self._atomic
	def atomic(self):
		self._atomic = True
		self._capturing = False
		return self

'''

class Expression {

    constructor(quantifier, child) {
        this.quantifier = quantifier;
        this.child = child;
    }
}

'''

class Expression:
	def __init__(self, quantifier, child) -> None:
		self.quantifier = quantifier
		self.child = child

'''

class RegexAlternative {
    /**
     * 
     * @param {*} groupName Null if it's not a named group.
     * @param  {...any} alternatives 
     */
    constructor(...alternatives) {
        this.groupName = null;
        this._capturing = true;
        this.alternatives = alternatives;
        this._atomic = false;
    }

    isCapturingGroup() {
        return this._capturing;
    }

    nonCapturing() {
        this._capturing = false;
        return this;
    }

    isAtomic() {
        return this._atomic;
    }
    
    atomic() {
        this._atomic = true;
        this._capturing = false;
        return this;
    }
}
'''

class RegexAlternative:
	def __init__(self, alternatives) -> None:
		self.groupName = None
		self._capturing = True
		self.alternatives = alternatives
		self._atomic = False
	def isCapturingGroup(self) -> bool:
		return self._capturing
	def nonCapturing(self):
		self._capturing = False
		return self
	def isAtomic(self):
		return self._atomic
	def atomic(self):
		self._atomic = True
		self._capturing = False
		return self

'''
class AtomicPattern {
    constructor(char) {
        this.char = char;
    }
}

class DotPattern {
}
'''

class AtomicPattern:
	def __init__(self, char):
		self.char = char

class DotPattern:
	def __init(self):
		self = self # Dummy


'''
class ComplexClassRange {
    constructor(start, end) {
        this.start = start;
        this.end = end;
    }

    matches(c) {
        return c >= this.start && this.end >= c;
    }
}

class ComplexClass {
    constructor(individialChars, ranges, name, negated) {
        this.chars = individialChars;
        this.ranges = ranges;
        this.name = name;
        this.negated = negated;
    }

    matches(c) {
        const base = this.chars.includes(c) || this.ranges.some(x => x.matches(c));
        return this.negated ? !base : base;
    }
}
'''

class ComplexClassRange:
	def __init__(self, start, end) -> None:
		self.start = start
		self.end = end
	def matches(self, c) -> bool:
		#return c >= self.start && self.end >= c
		return c >= self.start and self.end >= c

class ComplexClass:
	def __init__(self, individualChars, ranges, name, negated) -> None:
		self.chars = individualChars
		self.ranges = ranges
		self.name = name
		self.negated = negated

	def matches(c) -> bool:
		base = c in self.chars
		if self.negated:
			return not base
		else:
			return base

'''
class DollarAnchor {

}

class CaretAnchor {
    
}

'''


class DollarAnchor:
	def __init(self):
		self = self # Dummy


class CaretAnchor:
	def __init(self):
		self = self # Dummy

'''
class Backreference {
    constructor(group) {
        this.group = group;
    }
}
'''
class Backreference:
	def __init__(self, group) -> None:
		self.group = group

