class Matcher:
	def matches(self, char: str, i: int) -> bool:
		return False # Placeholder.
	def isEpsilon(self) -> bool: # This is just to check if this matcher is an epsilon matcher. (Epsilon matches basically anything and does not consume the character.)
		return False # Placeholder
	def getLabel(self) -> str:
		return "not-named" # Placeholder

class CharacterMatcher(Matcher):
	def __init__(self, c: str) -> None:
		# This sets the character for this state
		self.c = c
	def matches(self, char: str, i: int) -> bool:
		if self.c == char:
			return True
		return False
	def getLabel(self) -> str:
		return self.c
	def isEpsilon(self) -> bool:
		return False

class EpsilonMatcher(Matcher):
	def matches(self, char: str, i: int) -> bool:
		#if self.c == char:
		#	return True
		return True
	def getLabel(self) -> str:
		return self.c
	def isEpsilon(self) -> bool:
		return True