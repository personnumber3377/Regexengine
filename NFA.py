
class Node:
	def __init__(self, name: str): # This is a node in the regex engine.
		self.transitions = {} # This will be added to later on.
		self.name = name


class NFAEngine:
	def __init__(self):
		self.states = [] # all possible states. This will be added to later on.
		self.nodes = {} # This is a dictionary with the name of the node as key and the reference to the node as a value
		self.current_states = [] # This is the current node(s) which we are at.
		self.current_nodes = [] # This is a list of names
		self.input_string = "" # This is our input to the state machine.
		self.where_we_are_in_input = 0 # This is the index in the input string where we are.
		self.alphabet = "" # This is the list of valid characters. If the input character is not in this, then automatically go to the dead state.
		self.end_nodes = []
		self.terminated = False
		
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
			out.append(self.nodes[node])
		return out # This returns a list of all of the node objects. This will be used in the transition function when we transition all of the nodes forward.
	def add_node(self, name: str) -> None: # This adds a node into our machine.
		new_node = Node(name)
		self.nodes[name] = new_node # add to the nodes dict
	def add_transition(self, name1: str, name2: str, condition: str): # defines a transition. The condition is a string of length one aka a character.
		assert len(condition) == 1 and isinstance(condition, str)
		# get destination node object
		dest_node = self.nodes[name2]
		# get source node
		source_node = self.nodes[name1]
		if condition in source_node.transitions: # If there is another possible transition for this character, then add another one to it.
			source_node.transitions[condition].append(dest_node)
		else:
			source_node.transitions[condition] = [dest_node] # There isn't a transition already defined for this character so initialize the list.
	def set_start_node(self, name: str) -> None: # Sets the group of nodes where could be at to a list containing only the start node aka we are now at the very start.
		self.current_nodes = [name]
	def set_end_nodes(self, names: list) -> None:
		self.end_nodes = names
	def get_end_node(self) -> Node:
		return self.nodes[self.end_node]
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
		char = self.consume_next_char()
		# Go over each possible current node.
		new_nodes = [] # These are the new nodes when we are done.
		for node in self.current_nodes:
			node_obj = self.nodes[node] # The actual node object
			if char in node_obj.transitions: # Check if the character is in the possible transitions. If it isn't then go to the dead state. Going to the dead state is synonomous with just removing this path alltogether, since it is not possible to transition from the dead state to any other state.
				nodes_we_transitioned_into = node_obj.transitions[char]
				for n in nodes_we_transitioned_into:

					new_nodes.append(n.name) # add the name to the new nodes. We will set our current nodes to these nodes later on.
		# Check if we have reached the end node
		if self.check_termination(new_nodes):
			print("We have reached the end node!")
			self.terminated = True
			return
		if new_nodes == []: # No path goes to the end node.
			self.terminated = True
			print("We did NOT reach the end node")
			return
		# Set the all possible current states to the new states.
		self.current_nodes = new_nodes
		return
