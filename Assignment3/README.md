# Sean Hansberry
# CSCI 3202
# AI 3202

For Manhattan heuristic:
	Usage: python Assignment3.py [filename] manhattan
	
For Diagonal heuristic:
	Usage: python Assignment3.py [filename] diagonal
	
'''
My heuristic equation for this assignment is very simple.
It counts the number of tiles that are diagonally in between the start and 
the goal. If the starting tile is on the top of the graph then the heuristic
returns the number of horizontal tiles to the goal or if the starting
tile is on the outer edge then the heurisitc returns the number of vertical 
tiles to the goal. This heuristic is admissible in A* search because it
will never overestimate the distance to the goal since it is taking the most 
direct path to the goal regardless of obstacles and diagonal movement cost.
This is more efficient than the Manhattan distance heuristic since the Manhattan
distance is calculated by taking the number of horizontal tiles plus the number
of vertical tiles to the goal. Therefore, by Pythagorean's theorem the diagonal
distance will always be shorter than the sum of the two sides so this heuristic
will give a better estimate and therefore give a more efficient search.

Example:
Using Manhattan distance on World1.txt:
	Total Cost: 136
	Evaluated Nodes: 70
Using Diagonal distance on World1.txt:
	Total Cost: 130
	Evaluated Nodes: 53		

This example shows that my heuristic found a path of shorter cost 
and evaluated less nodes in the process proving that my diagonal 
distance heuristic function is more efficient in A star search algorithms
than the Manhattan distance heuristic function 
'''