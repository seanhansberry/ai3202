#Sean Hansberry
#CSCI 3202
#Assignment 3

import sys
import Queue
import heapq

def main(argv):
	#Check for heuristic
	heuristic_flag=False
	my_heuristic = argv[2]
	if my_heuristic == 'manhattan' or my_heuristic == 'diagonal':
		heuristic_flag=True
	else:
		while heuristic_flag == False:
			my_heuristic = raw_input("Please enter a heuristic (manhattan or diagonal): ")
			if my_heuristic == 'manhattan' or my_heuristic == 'diagonal':
				heuristic_flag = True
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
	AStarSearch = AStar(my_heuristic)
	AStarSearch.init_grid(myGraph)
	AStarSearch.a_star_search()



	return


class Node():
	def __init__(self, nodeType, x, y):
		self.nodetype = nodeType
		self.x=x
		self.y=y
		self.parent=None
		self.g=0 #explored cost
		self.h=0 #heuristic cost
		self.f=0 #sum cost
		self.diagonal = []

class AStar(object):

	def __init__(self, heuristic_type):
		self.opened = []
		heapq.heapify(self.opened)
		self.closed = set()
		self.nodes = []
		self.grid_height = 8
		self.grid_width = 10
		self.graph = []
		self.heuristic = heuristic_type

	def get_node(self, x, y):
		for z in range(len(self.nodes)):
			if self.nodes[z].x == x and self.nodes[z].y == y:
				#print "Node was Found!:", self.nodes[z].x, self.nodes[z].y
				return self.nodes[z]
		return False

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



	def get_adjacent(self, node):

		adjacent=[]

		if node.x < self.grid_width-1 and node.y < self.grid_height-1:
			#Move diagonal up to right
			node.diagonal.append(self.get_node(node.x+1, node.y+1))
			adjacent.append(self.get_node(node.x+1, node.y+1))

		if node.x < self.grid_width-1:
			#Move right
			adjacent.append(self.get_node(node.x+1,node.y))
			
		if node.y < self.grid_height-1:
			#Move up
			adjacent.append(self.get_node(node.x,node.y+1))

		if node.x < self.grid_width-1 and node.y > 0:
			#Move diagonal down to right
			node.diagonal.append(self.get_node(node.x+1, node.y-1))
			adjacent.append(self.get_node(node.x+1,node.y-1))
				
		if node.x > 0 and node.y < self.grid_height-1:
			#Move diagonal up to left
			node.diagonal.append(self.get_node(node.x-1, node.y+1))
			adjacent.append(self.get_node(node.x-1,node.y+1))

		if node.x > 0:
			#Move left
			adjacent.append(self.get_node(node.x-1,node.y))
			
		if node.y > 0:
			#Move down
			adjacent.append(self.get_node(node.x,node.y-1))

		if node.x > 0 and node.y > 0:
			#Move diagonal down left
			node.diagonal.append(self.get_node(node.x-1, node.y-1))
			adjacent.append(self.get_node(node.x-1,node.y-1))
		
		return adjacent


	def update_node(self, adjacent, node):
		#See if adjacent node is diagonal to node
		diagonal_flag = False
		for x in node.diagonal:
			if x == adjacent:
				diagonal_flag = True
				if adjacent.nodetype == 1:
					adjacent.g = node.g+24
				else:
					adjacent.g = node.g+14
		if diagonal_flag == False:
			if adjacent.nodetype == 1:
				adjacent.g = node.g+20
			else:
				adjacent.g = node.g+10


		if self.heuristic == "manhattan":
			adjacent.h = self.manhattan_dist(adjacent)
		elif self.heuristic == "diagonal":
			adjacent.h = self.diag_dist(adjacent)
		else:
			print "Couldn't find heuristic:",self.heuristic
		adjacent.parent = node
		adjacent.f = adjacent.h + adjacent.g

	def manhattan_dist(self, node):
		return 10 * abs(self.goal.x - node.x) + abs(self.goal.y - node.y)

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

	def show_path(self):
		node = self.goal
		while node.parent is not self.start:
			node = node.parent
			print "Path:", node.x, node.y

	def a_star_search(self):
		#Make the priority queue starting at start
		evaluated_nodes = 0
		heapq.heappush(self.opened, (self.start.f, self.start))
		while len(self.opened):
			# Pop a node from heap queue
			f, node = heapq.heappop(self.opened)
			# Close the node
			self.closed.add(node)
			

			if node == self.goal:
				self.show_path()
				print "Total cost:", node.g
				print "Number of evaluated nodes:", evaluated_nodes
				break
			# Get adjacent nodes
			adjacent_nodes = self.get_adjacent(node)
			for adjacent_node in adjacent_nodes:
				#Ignore walls or nodes in the closed list
				if adjacent_node not in self.closed and adjacent_node.nodetype != "2":
					#If node already on open list, check to see if path is optimal
					if (adjacent_node.f, adjacent_node) in self.opened:
						diagonal_flag=False
						#Check if path is optimal
						for x in node.diagonal:
							if x == adjacent_node:
								diagonal_flag=True
								if adjacent_node.nodetype==1:
									if  adjacent_node.g > node.g + 24:
										self.update_node(adjacent_node,node)

								else:
									if adjacent_node.g > node.g + 14:
										self.update_node(adjacent_node,node)
						
						if diagonal_flag == False:
							
							if adjacent_node.nodetype == 1:
								print adjacent_node.x, adjacent_node.y, adjacent_node.nodetype
							
								if adjacent_node.g > node.g + 20:
									self.update_node(adjacent_node,node)
	
							else:
								if adjacent_node.g > node.g + 10:
									
									self.update_node(adjacent_node,node)

					else:
						self.update_node(adjacent_node, node)
						heapq.heappush(self.opened, (adjacent_node.f, adjacent_node))
						evaluated_nodes = evaluated_nodes+1





# main entry point
if __name__ == "__main__":
	main(sys.argv)