
from matchers import *

class Node:
	def __init__(self, name: str): # This is a node in the regex engine.
		self.transitions = [] # This will be added to later on.
		self.name = name
	def add_transition(self, destnode, matcher) -> None:
		self.transitions.append([matcher, destnode])


class NFAEngine:
	def __init__(self):
		self.states = {} # all possible states. This will be added to later on.
		self.current_states = [] # This is the current node(s) which we are at.
		self.current_nodes = [] # This is a list of names
		self.input_string = "" # This is our input to the state machine.
		self.where_we_are_in_input = 0 # This is the index in the input string where we are.
		self.alphabet = "" # This is the list of valid characters. If the input character is not in this, then automatically go to the dead state.
		self.end_nodes = []
		self.terminated = False
		self.start_state = None
	def update_input(self, string: str) -> None: # Update the input to the state machine.
		self.input_string = string
		self.where_we_are_in_input = 0
	def consume_next_char(self):
		char = self.input_string[self.where_we_are_in_input]
		self.where_we_are_in_input += 1
		return char
	def get_current_nodes(self) -> Node:
		out = []
		for node in self.current_nodes:
			out.append(self.states[node])
		return out # This returns a list of all of the node objects. This will be used in the transition function when we transition all of the nodes forward.
	def add_state(self, name: str) -> None: # This adds a node into our machine.
		new_state = Node(name)
		self.states[name] = new_state # add to the nodes dict
	def add_transition(self, name1: str, name2: str, condition): # defines a transition. The condition is a string of length one aka a character.
		'''
		addTransition(fromState, toState, matcher) {
        	this.states[fromState].addTransition(this.states[toState], matcher);
    	}
		'''
		#assert len(condition) == 1 and isinstance(condition, str)
		assert isinstance(condition, Matcher) or isinstance(condition, CharacterMatcher) or isinstance(condition, EpsilonMatcher)
		# get destination node object
		dest_node = self.states[name2]
		self.states[name1].add_transition(self.states[name2], condition)
		return
	def set_start_node(self, name: str) -> None: # Sets the group of nodes where could be at to a list containing only the start node aka we are now at the very start.
		self.current_nodes = [name]
		self.start_state = name
	def set_end_nodes(self, names: list) -> None:
		self.end_nodes = names
	def get_end_node(self) -> Node:
		return self.states[self.end_node]
	def check_termination(self, new_nodes: list) -> bool:
		if len(new_nodes) > len(self.end_nodes):
			checked_list = self.end_nodes
			other_list = new_nodes
		else:
			checked_list = new_nodes
			other_list = self.end_nodes
		for elem in checked_list:
			if elem in other_list:
				return True
		return False
	def transition_states(self):
		# TODO: First get the input character.
		# Then look at the current node and see which transition(s) to take.
		# Take the transition(s)
		if self.terminated:
			print("Can not advance an already terminated state machine!")
			return

		stack = [[0, self.states[self.start_state]]]


		while len(stack):
			# Pop off the state.
			i, state = stack.pop(-1) # pop from the end of the stack
			if state.name in self.end_nodes:
				print("Match found!")
				return True
			input_char = self.input_string[i]
			for i in range(len(state.transitions)-1,-1,-1): # Go from the last to the first
				matcher, destination_state = state.transitions[i]
				if matcher.matches(input_char, i): # if matches character
					if not matcher.isEpsilon(): # If NOT an epsilon matcher, then advance the string for this path.
						i += 1
					stack.append([i, destination_state])
		print("Match NOT found!")
		return False






