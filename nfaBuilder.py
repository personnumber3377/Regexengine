
# This file is actually the program, which constructs the NFA from an AST generated by antlr4 from the regex string.

from ast import *
from astBuilder import *
from NFA import *

class NFABuilder:
	def __init__(self):
		self.stateNumber = 0


