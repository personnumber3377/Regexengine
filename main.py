
from NFA import *

def main() -> int:
	# Basically synonomous with this:
	'''
	const nfa = new EngineNFA();
	nfa.declareStates("q0", "q1");
	nfa.setInitialState("q0");
	nfa.setEndingStates(["q1"]);
	nfa.addTransition("q0", "q1", new CharacterMatcher("a"));
	console.log(nfa.compute("a"));
	'''

	engine = NFAEngine()
	engine.update_input("b")
	engine.add_node("q0")
	engine.add_node("q1")
	engine.set_start_node("q0")
	engine.set_end_nodes(["q1"])
	# add_transition(self, name1: str, name2: str, condition: str)
	engine.add_transition("q0", "q1", "a")
	engine.transition_states() # Run one step!
	return 0

if __name__=="__main__":
	exit(main())
