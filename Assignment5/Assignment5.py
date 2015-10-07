#Sean Hansberry
#CSCI 3202
#Assignment 5

import sys
import Queue
import heapq

def main(argv):
	#Check for e 
	if len(sys.argv) < 3:
		e=0
		while e == 0 or e == "":
			e = float(raw_input("Please enter a value for e: "))
	else:
		e=float(argv[2])


	#Read in the data from the world
	with open(argv[1]) as f:
		data = [i.split() for i in f.readlines()]

	#Create the graph of nodes and set locations
	myGraph = []
	y=len(data)-2
	for row in data:
		x=0
		for value in row:
			myGraph.append(Node(value, x, y))
			x=x+1
		y=y-1

	#Begin searching through the graph
	mdp_search = MDP(e)
	mdp_search.init_grid(myGraph)
	mdp_search.markov_decision_process()
	return


class Node():
	def __init__(self, nodeType, x, y):
		self.nodetype = nodeType
		self.x=x
		self.y=y
		self.parent=None
		self.utility = 0
		self.actions = []
		self.visited = False

class MDP(object):

	def __init__(self, allowable_error):
		self.opened = []
		heapq.heapify(self.opened)
		self.closed = set()
		self.nodes = []
		self.grid_height = 8
		self.grid_width = 10
		self.graph = []
		self.error = allowable_error

	def get_node(self, x, y):
		for z in range(len(self.nodes)):
			#print self.nodes[z].x, self.nodes[z].y
			if self.nodes[z].x == x and self.nodes[z].y == y:
				#print "Node was Found!:", self.nodes[z].x, self.nodes[z].y
				return self.nodes[z]
		return None

	def init_grid(self, graph):
		y=8
		self.graph.append(graph)
		for row in self.graph:
			x=0
			for col in row:
				if x%10 == 0:
					y=y-1
				self.nodes.append(Node(col.nodetype, x%10, y))
				x=x+1

		self.start = self.get_node(0,0)
		self.goal = self.get_node(9,7)

	def get_actions(self, node):
		
		if node.x+1 < self.grid_width and self.get_node(node.x+1,node.y).nodetype != '2' and self.get_node(node.x+1,node.y).visited != True:
			node.actions.append(self.get_node(node.x+1,node.y))

		if node.x-1 >= 0 and self.get_node(node.x-1,node.y).nodetype != '2' and self.get_node(node.x-1,node.y).visited != True:
			node.actions.append(self.get_node(node.x-1,node.y))
			
		if node.y+1 < self.grid_height and self.get_node(node.x,node.y+1).nodetype != '2' and self.get_node(node.x,node.y+1).visited != True:
			node.actions.append(self.get_node(node.x,node.y+1))

		if node.y-1 >= 0 and self.get_node(node.x,node.y-1).nodetype != '2' and self.get_node(node.x,node.y-1).visited != True:
			node.actions.append(self.get_node(node.x,node.y-1))


	def value_iteration(self, node):
		f_left_available = False
		f_right_available = False
		f_up_available = False
		f_down_available = False

		#Find reward of node
		if node.nodetype == '1': #mountain
			reward=-1
		elif node.nodetype == '2': #wall
			reward = 0
			return
		elif node.nodetype == '3': #snake
			reward = -2
		elif node.nodetype == '4': #barn
			reward = 1
		elif node.nodetype == '50': #apple
			reward = 50
		else:
			reward = 0

		#Check directions for utility
		if node.x+1 < self.grid_width:
			f_right_available = True

		if node.x-1 >= 0:
			f_left_available = True

		if node.y+1 < self.grid_height:
			f_up_available = True

		if node.y-1 >= 0:
			f_down_available = True
		
		#Find the utility of equivalent nodes
		expected_up_utility = 0
		expected_down_utility = 0
		expected_right_utility = 0
		expected_left_utility = 0

		#Update the right node
		current_node = self.get_node(node.x+1,node.y)
		if f_right_available:
			if f_left_available:
				expected_right_utility = 0.8 * node.utility + 0.1 * self.get_node(node.x-1, node.y).utility + 0.1 * node.utility
			else:
				expected_right_utility = 0.8 * current_node.utility + 0.1 * node.utility + 0.1 * self.get_node(node.x+1, node.y).utility
			

		#Update left node
		current_node = self.get_node(node.x-1,node.y)
		if f_left_available:
			if f_right_available:
				expected_left_utility = 0.8 * current_node.utility + 0.1 * self.get_node(node.x+1, node.y).utility + 0.1 * current_node.utility
			else:
				expected_left_utility = 0.8 * current_node.utility + 0.1 * current_node.utility + 0.1 * node.utility		

		#Update up node
		current_node = self.get_node(node.x,node.y+1)
		if f_up_available:
			if f_right_available and f_left_available:
				expected_up_utility = 0.8 * current_node.utility + 0.1 * self.get_node(node.x-1, node.y).utility + 0.1 * self.get_node(node.x+1, node.y).utility
			elif f_right_available:
				expected_up_utility = 0.8 * current_node.utility + 0.1 * node.utility + 0.1 * self.get_node(node.x+1, node.y).utility
			elif f_left_available:
				expected_up_utility = 0.8 * current_node.utility + 0.1 * self.get_node(node.x-1, node.y).utility + 0.1 * node.utility
			else:
				print "You have failed Update the Up Node" 

		#Update down node
		current_node = self.get_node(node.x,node.y-1)
		if f_down_available:
			if f_right_available and f_left_available:
				expected_down_utility = 0.8 * current_node.utility + 0.1 * self.get_node(node.x-1, node.y).utility + 0.1 * self.get_node(node.x+1, node.y).utility
			elif f_right_available:
				expected_up_utility = 0.8 * current_node.utility + 0.1 * node.utility + 0.1 * self.get_node(node.x+1, node.y).utility
			elif f_left_available:
				expected_up_utility = 0.8 * current_node.utility + 0.1 * self.get_node(node.x-1, node.y).utility + 0.1 * node.utility
			else:
				print "You have failed Update the Down Node" 

		#Find max utility and update node

		max_value = expected_right_utility
		node.utility = reward + (0.9 * expected_right_utility)

		if expected_up_utility > max_value:
			max_value = expected_up_utility
			node.utility = reward + (0.9 * expected_up_utility)
		if expected_down_utility > max_value:
			max_value = expected_down_utility
			node.utility = reward + (0.9 * expected_down_utility)
		if expected_left_utility > max_value:
			max_value = expected_left_utility
			node.utility = reward + (0.9 * expected_left_utility)
		#print "Updated node:",node.x,node.y,"With utility:",node.utility

	def diag_dist(self, node, tiles=0):
		(x1, y1) =(node.x, node.y)
		(x2, y2) = (self.goal.x, self.goal.y)


		if x1 > self.grid_width-1 or y1 > self.grid_height-1:
			print "There was an error x1:",x1,"y1:",y1,"width:",self.grid_width,"height:",self.grid_height
			return False

		if (x1, y1) == (x2, y2):
			return 10*tiles+0

		elif x1 == self.grid_width-1:
			#Move up
			current = self.get_node(x1, y1+1)
			return self.diag_dist(current, tiles+1)
		elif y1 ==  self.grid_height-1:
			#Move right
			current = self.get_node(x1+1,y1)
			return self.diag_dist(current, tiles+1)
		else:
			#Move diagonally
			current = self.get_node(x1+1, y1+1)
			return self.diag_dist(current, tiles+1)

	def iterative_process(self):
		error = self.error
		max_difference = (0.1/0.9)*error

		#Set utlility of all nodes to 0
		for node in self.nodes:
			current_utility = node.utility
			current_difference=0
			while current_difference < max_difference:
				current_difference = 0
				for node in self.nodes:
					#Update utility
					self.value_iteration(node)
					if abs(current_utility - node.utility) > current_difference:
						current_difference = abs(current_utility - node.utility)		


	def show_path(self):
		node = self.goal
		while node.parent is not self.start:
			print "Path location:", node.x, node.y, "with utility of:", node.utility
			node = node.parent

	def markov_decision_process(self):
		self.iterative_process()

		start_node = self.start
		decision_queue = []
		decision_queue.append('null')
		decision_queue.append(start_node)
		while len(decision_queue) > 0:
			next_node = None
			current_node = decision_queue.pop()
			current_node.visited = True
			self.get_actions(current_node)
			actions = current_node.actions
			max_utility = -100

			for node in actions:
				if next_node == None:
					next_node = node
				
				if node.utility - self.diag_dist(node) >= max_utility:
					max_utility = node.utility - self.diag_dist(node) 
					next_node = node

			next_node.parent = current_node

			if next_node == self.goal:
				self.show_path()
				print "Total utility:", self.goal.utility
				decision_queue.pop()

			else:
				decision_queue.append(next_node)


		


# main entry point
if __name__ == "__main__":
	main(sys.argv)