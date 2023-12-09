
from NFA import *


def test_simple() -> None:
	engine = NFAEngine()
	engine.update_input("a")
	engine.add_state("q0")
	engine.add_state("q1")
	engine.set_start_node("q0")
	engine.set_end_nodes(["q1"])
	# add_transition(self, name1: str, name2: str, condition: str)
	engine.add_transition("q0", "q1", CharacterMatcher("a"))
	assert engine.transition_states() # Run one step!
	return 0

def test_epsilon_loop() -> None:
	'''
	const nfa = new EngineNFA();
	nfa.declareStates("q0", "q1", "q2");
	nfa.setInitialState("q0");
	nfa.setEndingStates(["q2"]);
	nfa.addTransition("q0", "q1", new CharacterMatcher("a"));
	nfa.addTransition("q1", "q1", new EpsilonMatcher());
	nfa.addTransition("q1", "q2", new CharacterMatcher("b"));
	console.log(nfa.compute("ab")); // Stuck forever :(
	'''
	engine = NFAEngine()
	engine.add_state("q0")
	engine.add_state("q1")
	engine.add_state("q2")
	engine.set_start_node("q0")
	engine.set_end_nodes(["q2"])
	engine.add_transition("q0", "q1", CharacterMatcher("a"))
	engine.add_transition("q1", "q1", EpsilonMatcher())
	engine.add_transition("q1", "q2", CharacterMatcher("b"))
	engine.update_input("ab")
	engine.transition_states()
	return 

def main() -> int:
	test_simple()
	print("Now testing the epsilon loop...")
	test_epsilon_loop()
	print("Passed!")
	return 0

if __name__=="__main__":
	exit(main())
