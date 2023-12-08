
from matchers import *

def main() -> int:
	char_matcher = CharacterMatcher("a")
	assert char_matcher.matches("a", 0)
	return 0

if __name__=="__main__":
	exit(main())
