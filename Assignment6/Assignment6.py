#Sean Hansberry
#CSCI 3202
#Assignment 6


import getopt, sys


def main():
    try:
        opts, args = getopt.getopt(sys.argv[1:], "m:g:j:p:")
    except getopt.GetoptError as err:
        # print help information and exit:
        print str(err) # will print something like "option -a not recognized"
        sys.exit(2)

   
    #Create the Bayes Net
    bayes=BayesNet()
    bayes.initialize()

    #Third Test Update the Priors if -p
    for o, a in opts:
		
		if o in ("-p"):
			print "flag o:", o
			print "args a:", a
			print "opts:", opts
			print "args:", args

			#print "Unit Test 1: Set prior for pollution OR smoker"
			#print "..."
			#print
			
			i=0
			
			for number in args:
				if i==1:
					break
				del args[i]
				value=float(number)
				i=i+1
			
			if a == "P":
				#Set Pollution Prior
				pollution = bayes.find('pollution')
				pollution.info[True][True] = value
				pollution.info[False][False] = 1-value
				print "Pollution Prior Set!:", float(value)

			elif a == "S":
				#Set Smoking Prior
				smoker=bayes.find('smoker')
				smoker.info[True][True] = value
				smoker.info[False][False] = 1-value
				print "Smoker Prior Set!:", value

			#setting the prior here works if the Bayes net is already built
			#setPrior(a[0], float(a[1:])
		elif o in ("-m"):
			print "flag", o
			print "args", a

			#print "Passed!"

			#Should calculate marginal density for dyspnoea
			#Find marginal for args[counter]
			print a
			false=False
			if a == "P":
				current_node=bayes.find('pollution')

			elif a == "S":
				current_node=bayes.find('smoker')

			elif a == "C":
				current_node=bayes.find('cancer')

			elif a == "X":
				current_node=bayes.find('xray')

			elif a == "D":
				current_node = bayes.find('dyspnoea')

			elif a == "~p":
				current_node=bayes.find('pollution')
				false = True
			elif a == "~s":
				current_node=bayes.find('smoker')
				false=True

			elif a == "~c":
				current_node=bayes.find('cancer')
				false=True

			elif a == "~x":
				current_node=bayes.find('xray')
				false=True

			elif a == "~d":
				current_node = bayes.find('dyspnoea')
				false=True

			else:
				print "unhandled option:", a


		
			#print "Calculating marginal for",current_node.name
			
			if false:
				current_node.option = False
			else:
				current_node.option = True

			marginal = bayes.calc_marginal(current_node)
			print "Marginal probability for", current_node.name,"being",current_node.option,"is",marginal








		elif o in ("-g"):
			print "flag", o
			print "args", a

			'''you may want to parse a here and pass the left of |
			and right of | as arguments to calcConditional
			'''
			#print "Unit test 4! Calculate and return conditional probabilities"
			#print "...."
			#print


			i=0
			conditions = []
			flag = True
			my_list = list(a)
			for argument in my_list:
				if i==0:

					if argument == '~':

						option = '~' + my_list[i+1]
						del my_list[i+1]
						flag=False

					else:
						option = argument

				else:
					conditions.append(argument)

				i=i+1

			
			i=0
			given = []
			for item in conditions:

				if item == '~':
					
					if conditions[i+1] == 'p':
						bayes.find('pollution').option=False
						given.append(bayes.find('pollution'))

					elif conditions[i+1] == 's':
						bayes.find('smoker').option=False
						given.append(bayes.find('smoker'))

					elif conditions[i+1] == 'c':
						bayes.find('cancer').option=False
						given.append(bayes.find('cancer'))

					elif conditions[i+1] == 'd':
						bayes.find('dyspnoea').option=False
						given.append(bayes.find('dyspnoea'))

					elif conditions[i+1] == 'x':
						bayes.find('xray').option=False
						given.append(bayes.find('xray'))

				
				elif item == 'p':
					
					given.append(bayes.find('pollution'))

				elif item == 's':
					
					given.append(bayes.find('smoker'))

				elif item == 'c':
					
					given.append(bayes.find('cancer'))

				elif item == 'd':
					
					given.append(bayes.find('dyspnoea'))

				elif item == 'x':
					
					given.append(bayes.find('xray'))

				else:
					print "Unhandled option", item

				i += 1


			print "arg:", option
			for item in given:
				print "given:", item.name, item.option

			if option == "p":
				current_node=bayes.find('pollution')

			elif option == "s":
				current_node=bayes.find('smoker')

			elif option == "c":
				current_node=bayes.find('cancer')

			elif option == "x":
				current_node=bayes.find('xray')

			elif option == "d":
				current_node = bayes.find('dyspnoea')

			elif option == "~p":
				current_node=bayes.find('pollution')
				flag = False

			elif option == "~s":
				current_node=bayes.find('smoker')
				flag = False

			elif option == "~c":
				current_node=bayes.find('cancer')
				flag = False

			elif option == "~x":
				current_node=bayes.find('xray')
				flag = False

			elif option == "~d":
				current_node = bayes.find('dyspnoea')
				flag = False

			else:
				print "unhandled option:", option

			print "My flag is", flag
			current_node.option=flag
			print "My current node is", current_node.name, current_node.option

			conditional = bayes.calc_conditional(current_node, given)
			print "Conditional probability for",current_node.name,"being",current_node.option ,"given",conditions,"is",conditional



		elif o in ("-j"):
			print "flag", o
			print "args", a

			i=0
			conditions = []
			my_list = list(a)
			for argument in my_list:
				if i==0:

					if argument == '~':

						option = '~' + my_list[i+1]

					else:
						option = argument

				else:
					conditions.append(argument)

				i=i+1

			i=0
			given = []
			for item in conditions:

				if item == '~':
					
					if conditions[i+1] == 'p':
						bayes.find('pollution').option=False
						given.append(bayes.find('pollution'))

					elif conditions[i+1] == 's':
						bayes.find('smoker').option=False
						given.append(bayes.find('smoker'))

					elif conditions[i+1] == 'c':
						bayes.find('cancer').option=False
						given.append(bayes.find('cancer'))

					elif conditions[i+1] == 'd':
						bayes.find('dyspnoea').option=False
						given.append(bayes.find('dyspnoea'))

					elif conditions[i+1] == 'x':
						bayes.find('xray').option=False
						given.append(bayes.find('xray'))

				
				elif item == 'p':
					
					given.append(bayes.find('pollution'))

				elif item == 's':
					
					given.append(bayes.find('smoker'))

				elif item == 'c':
					
					given.append(bayes.find('cancer'))

				elif item == 'd':
					
					given.append(bayes.find('dyspnoea'))

				elif item == 'x':
					
					given.append(bayes.find('xray'))

				else:
					print "Unhandled option", item

				i += 1




			print "arg:", option, "conditions:",conditions

			if option == "p":
				current_node=bayes.find('pollution')
				current_node.option=True

			elif option == "s":
				current_node=bayes.find('smoker')
				current_node.option=True

			elif option == "c":
				current_node=bayes.find('cancer')
				current_node.option=True

			elif option == "x":
				current_node=bayes.find('xray')
				current_node.option=True

			elif option == "d":
				current_node = bayes.find('dyspnoea')
				current_node.option=True

			elif option == "~p":
				current_node=bayes.find('pollution')
				current_node.option=False

			elif option == "~s":
				current_node=bayes.find('smoker')
				current_node.option=False

			elif option == "~c":
				current_node=bayes.find('cancer')
				current_node.option=False

			elif option == "~x":
				current_node=bayes.find('xray')
				current_node.option=False

			elif option == "~d":
				current_node = bayes.find('dyspnoea')
				current_node.option=False

			else:
				print "unhandled option:", option

			
			joint = bayes.calc_joint(current_node, given)
			print "Joint probability for",current_node.name ,"being",current_node.option,"with",conditions,"is", joint



		else:
			assert False, "unhandled option"
	


		#Extra parsing for args if prior is set
		a = ''
		for word in args:

			my_list = list(word)
			i=0
			for option in my_list:
				if option == "-":
					o = my_list[i]+my_list[i+1]
					i=1
					j=1
					while i+j < len(my_list):
						a = a + my_list[i+j]
						j=j+1

			if o in ("-m"):
				print "flag", o
				print "args", a

					#print "Passed!"

					#Should calculate marginal density for dyspnoea
					#Find marginal for args[counter]
				print a
				false=False
				if a == "P":
					current_node=bayes.find('pollution')

				elif a == "S":
					current_node=bayes.find('smoker')

				elif a == "C":
					current_node=bayes.find('cancer')

				elif a == "X":
					current_node=bayes.find('xray')

				elif a == "D":
					current_node = bayes.find('dyspnoea')

				elif a == "~p":
					current_node=bayes.find('pollution')
					false = True
				elif a == "~s":
					current_node=bayes.find('smoker')
					false=True

				elif a == "~c":
					current_node=bayes.find('cancer')
					false=True

				elif a == "~x":
					current_node=bayes.find('xray')
					false=True

				elif a == "~d":
					current_node = bayes.find('dyspnoea')
					false=True

				else:
					print "unhandled option:", a


			
				#print "Calculating marginal for",current_node.name
				
				if false:
					current_node.option = False
				else:
					current_node.option = True

				marginal = bayes.calc_marginal(current_node)
				print "Marginal probability for", current_node.name,"being",current_node.option,"is",marginal








			elif o in ("-g"):
				print "flag", o
				print "args", a

				'''you may want to parse a here and pass the left of |
				and right of | as arguments to calcConditional
				'''
				#print "Unit test 4! Calculate and return conditional probabilities"
				#print "...."
				#print


				i=0
				conditions = []
				flag = True
				my_list = list(a)
				for argument in my_list:
					if i==0:

						if argument == '~':

							option = '~' + my_list[i+1]
							del my_list[i+1]
							flag=False

						else:
							option = argument

					else:
						conditions.append(argument)

					i=i+1

				
				i=0
				given = []
				for item in conditions:

					if item == '~':
						
						if conditions[i+1] == 'p':
							bayes.find('pollution').option=False
							given.append(bayes.find('pollution'))

						elif conditions[i+1] == 's':
							bayes.find('smoker').option=False
							given.append(bayes.find('smoker'))

						elif conditions[i+1] == 'c':
							bayes.find('cancer').option=False
							given.append(bayes.find('cancer'))

						elif conditions[i+1] == 'd':
							bayes.find('dyspnoea').option=False
							given.append(bayes.find('dyspnoea'))

						elif conditions[i+1] == 'x':
							bayes.find('xray').option=False
							given.append(bayes.find('xray'))

					
					elif item == 'p':
						
						given.append(bayes.find('pollution'))

					elif item == 's':
						
						given.append(bayes.find('smoker'))

					elif item == 'c':
						
						given.append(bayes.find('cancer'))

					elif item == 'd':
						
						given.append(bayes.find('dyspnoea'))

					elif item == 'x':
						
						given.append(bayes.find('xray'))

					else:
						print "Unhandled option", item

					i += 1


				print "arg:", option
				for item in given:
					print "given:", item.name, item.option

				if option == "p":
					current_node=bayes.find('pollution')

				elif option == "s":
					current_node=bayes.find('smoker')

				elif option == "c":
					current_node=bayes.find('cancer')

				elif option == "x":
					current_node=bayes.find('xray')

				elif option == "d":
					current_node = bayes.find('dyspnoea')

				elif option == "~p":
					current_node=bayes.find('pollution')
					flag = False

				elif option == "~s":
					current_node=bayes.find('smoker')
					flag = False

				elif option == "~c":
					current_node=bayes.find('cancer')
					flag = False

				elif option == "~x":
					current_node=bayes.find('xray')
					flag = False

				elif option == "~d":
					current_node = bayes.find('dyspnoea')
					flag = False

				else:
					print "unhandled option:", option

				print "My flag is", flag
				current_node.option=flag
				print "My current node is", current_node.name, current_node.option

				conditional = bayes.calc_conditional(current_node, given)
				print "Conditional probability for",current_node.name,"being",current_node.option ,"given",conditions,"is",conditional



			elif o in ("-j"):
				print "flag", o
				print "args", a

				i=0
				conditions = []
				my_list = list(a)
				for argument in my_list:
					if i==0:

						if argument == '~':

							option = '~' + my_list[i+1]

						else:
							option = argument

					else:
						conditions.append(argument)

					i=i+1

				i=0
				given = []
				for item in conditions:

					if item == '~':
						
						if conditions[i+1] == 'p':
							bayes.find('pollution').option=False
							given.append(bayes.find('pollution'))

						elif conditions[i+1] == 's':
							bayes.find('smoker').option=False
							given.append(bayes.find('smoker'))

						elif conditions[i+1] == 'c':
							bayes.find('cancer').option=False
							given.append(bayes.find('cancer'))

						elif conditions[i+1] == 'd':
							bayes.find('dyspnoea').option=False
							given.append(bayes.find('dyspnoea'))

						elif conditions[i+1] == 'x':
							bayes.find('xray').option=False
							given.append(bayes.find('xray'))

					
					elif item == 'p':
						
						given.append(bayes.find('pollution'))

					elif item == 's':
						
						given.append(bayes.find('smoker'))

					elif item == 'c':
						
						given.append(bayes.find('cancer'))

					elif item == 'd':
						
						given.append(bayes.find('dyspnoea'))

					elif item == 'x':
						
						given.append(bayes.find('xray'))

					else:
						print "Unhandled option", item

					i += 1




				print "arg:", option, "conditions:",conditions

				if option == "p":
					current_node=bayes.find('pollution')
					current_node.option=True

				elif option == "s":
					current_node=bayes.find('smoker')
					current_node.option=True

				elif option == "c":
					current_node=bayes.find('cancer')
					current_node.option=True

				elif option == "x":
					current_node=bayes.find('xray')
					current_node.option=True

				elif option == "d":
					current_node = bayes.find('dyspnoea')
					current_node.option=True

				elif option == "~p":
					current_node=bayes.find('pollution')
					current_node.option=False

				elif option == "~s":
					current_node=bayes.find('smoker')
					current_node.option=False

				elif option == "~c":
					current_node=bayes.find('cancer')
					current_node.option=False

				elif option == "~x":
					current_node=bayes.find('xray')
					current_node.option=False

				elif option == "~d":
					current_node = bayes.find('dyspnoea')
					current_node.option=False

				else:
					print "unhandled option:", option

				
				joint = bayes.calc_joint(current_node, given)
				print "Joint probability for",current_node.name ,"being",current_node.option,"with",conditions,"is", joint



			else:
				assert False, "unhandled option"


    # ...

class Node():
	def __init__(self, name, info):
		self.name = name
		self.info = info
		self.parents = []
		self.children = []
		self.option = True

	def set_parents(self, parents):
		for parent in parents:

			self.parents.append(parent)

	def set_children(self, children):
		for child in children:

			self.children.append(child)

class BayesNet():
	def __init__(self):
		self.network = []
		self.dgivenc=0.65
		self.dgivennc=0.30
		self.xgivenc=0.9
		self.xgivennc=0.2
		self.cgivennps=0.05
		self.cgivennpns=0.02
		self.cgivenps=0.03
		self.cgivenpns=0.001
		self.npollution=0.9
		self.psmoker=0.3


	def find(self, node):
		for item in self.network:
			if item.name == node:
				return item
		
		print "Node not Found!:", node

	def initialize(self):
		self.network.append(Node('pollution', {True : {True : 0.9}, False : {False : 0.1}}))
		self.network.append(Node('smoker', { True : {True : 0.3}, False : {False : 0.7}}))
		self.network.append(Node('cancer', { True: {'ps' : 0.05, 'p~s': 0.02, '~ps': 0.03, '~p~s': 0.001}, False : {'ps' : 0.95, 'p~s': 0.98, '~ps': 0.97, '~p~s': 0.999}}))
		self.network.append(Node('dyspnoea', { True : {'c' : 0.65, '~c': 0.30}, False : {'c' : 0.35, '~c': 0.70}}))
		self.network.append(Node('xray', { True : {'c' : 0.90, '~c': 0.20}, False : {'c' : 0.10, '~c': 0.80}}))
		

		pollution=self.find('pollution')
		smoker=self.find('smoker')
		cancer=self.find('cancer')
		dyspnoea=self.find('dyspnoea')
		xray=self.find('xray')

		children = []
		parents = []

		children.append(cancer)

		pollution.set_children(children)
		smoker.set_children(children)

		parents.append(pollution)
		parents.append(smoker)

		xray.set_parents(children)
		dyspnoea.set_parents(children)

		children.pop()

		children.append(dyspnoea)
		children.append(xray)

		cancer.set_parents(parents)
		cancer.set_children(children)

		print "Bayes Net Initialized!"
		print

	def update(self, node, probability, new_probability, value):

		#for item in self.network:

		#	for probability_type, probabilities in item.items():
		current_node = self.find(node)
		if current_node == None:
			print "Node not found:", node
			return

		#Check for new probability otherwise add it
		print current_node.info[probability]
		f_found=False
		for item, x in current_node.info[probability].items():
			if item == new_probability:
				#print "Probability Found!:", new_probability
				current_node.info[probability][new_probability]=value
				f_found=True

		if f_found is not True:
			current_node.info[probability].update({new_probability : value})

		print "Node updated!:", current_node.name, current_node.info
		print
		#print current_node.info

	def get_value(self, node, dist, label):

		cur_node = self.find(node)

		for probability, value in cur_node.info[dist].items():

			if label == probability:

				print "Adding value to node:", node, value
				return value

	def calc_marginal(self, node):
		total = 0
		numerator=0
		denominator=0

		#Base Case
		#P(A) = P(A|parents(A))

		if len(node.parents) == 0:
			#No parents return A
			return node.info[node.option][node.option]


		else:
			for parent in node.parents:
				#Calc conditional for P(A|Parents(A)) P(A) = P(AB) = P(A/B)*P(B)
				parent.option = True
				total = total + self.calc_conditional(node, [parent])
				parent.option = False
				total = total + self.calc_conditional(node, [parent])

		return total


	def calc_conditional(self, node, given, option_flag=None):
		
		total = 0

		# Node / parent
		#P(A/B) = P(AB)/P(B)
		#P(A/B) = P(Ab)/P(b)+P(A~b)/P(~b)
		parent_found=False
		child_found = False


		pollution=self.find('pollution')
		smoker=self.find('smoker')
		cancer=self.find('cancer')
		dyspnoea=self.find('dyspnoea')
		xray=self.find('xray')

		#P(C/s)
		#Given is parent
		#P(C/S)
		for item in given:


			for parent in node.parents:

				if parent == item:
					parent_found=True
					if parent == cancer:

						if node == dyspnoea:

							if node.option:

								if parent.option:
									total = total + self.dgivenc * self.calc_marginal(cancer)
								else:
									total = total + self.dgivennc * self.calc_marginal(cancer)

							else:

								if parent.option:
									total = total + (1-self.dgivenc) * self.calc_marginal(cancer)
								else:
									total = total + (1-self.dgivennc) * self.calc_marginal(cancer)

						else:
							#xray
							if node.option:

								if parent.option:
									total = total + self.xgivenc * self.calc_marginal(cancer)
								else:
									total = total + self.xgivennc * self.calc_marginal(cancer)

							else:
							
								if parent.option:
									total = total + (1-self.xgivenc) * self.calc_marginal(cancer)
								else:
									total = total + (1-self.xgivennc) * self.calc_marginal(cancer)

					elif parent == pollution:

						if node.option:
							#node true
							if parent.option:
								#parent true
								if option_flag is True:

									total = total + self.cgivenps * self.calc_marginal(pollution)*self.calc_marginal(smoker)
								
								elif option_flag is False:

									smoker.option = False
									total = total + self.cgivenpns * self.calc_marginal(pollution)*self.calc_marginal(smoker)

								else:
									total = total + self.cgivenps * self.calc_marginal(pollution)*self.calc_marginal(smoker)
									smoker.option = False
									total = total + self.cgivenpns * self.calc_marginal(pollution)*self.calc_marginal(smoker)
							else:
								if option_flag:

									total = total + self.cgivennps * self.calc_marginal(pollution)*self.calc_marginal(smoker)
								
								elif option_flag is False:

									smoker.option = False
									total = total + self.cgivennpns * self.calc_marginal(pollution)*self.calc_marginal(smoker)

								else:

									total = total + self.cgivennps * self.calc_marginal(pollution)*self.calc_marginal(smoker)									
									smoker.option = False
									total = total + self.cgivennpns * self.calc_marginal(pollution)*self.calc_marginal(smoker)

						else:

							if parent.option:

								if option_flag:

									total = total + (1-self.cgivenps) * self.calc_marginal(pollution)*self.calc_marginal(smoker)
	
								elif option_flag is False:
									smoker.option = False
									total = total + (1-self.cgivenpns) * self.calc_marginal(pollution)*self.calc_marginal(smoker)

								else:
									total = total + (1-self.cgivenps) * self.calc_marginal(pollution)*self.calc_marginal(smoker)
									smoker.option = False
									total = total + (1-self.cgivenpns) * self.calc_marginal(pollution)*self.calc_marginal(smoker)

							else:

								if option_flag:
									total = total + (1-self.cgivennps) * self.calc_marginal(pollution)*self.calc_marginal(smoker)
								
								elif option_flag is False:

									smoker.option = False
									total = total + (1-self.cgivennpns) * self.calc_marginal(pollution)*self.calc_marginal(smoker)
								else:
									total = total + (1-self.cgivennps) * self.calc_marginal(pollution)*self.calc_marginal(smoker)
									smoker.option = False
									total = total + (1-self.cgivennpns) * self.calc_marginal(pollution)*self.calc_marginal(smoker)
					else:
						#smoker
						if node.option:
							#cancer
							if parent.option:

								if option_flag:
									total = total + self.cgivenps * self.calc_marginal(pollution) * self.calc_marginal(smoker)
								elif option_flag is False:
									pollution.option=False
									total = total + self.cgivennps * self.calc_marginal(pollution) * self.calc_marginal(smoker)

							else:
								if option_flag:

									total = total + self.cgivenpns * self.calc_marginal(pollution) * self.calc_marginal(smoker)
								
								elif option_flag is False:
									pollution.option=False
									total = total + self.cgivennpns * self.calc_marginal(pollution) * self.calc_marginal(smoker)
								else:
									total = total + self.cgivenps * self.calc_marginal(pollution) * self.calc_marginal(smoker)
									pollution.option=False
									total = total + self.cgivennps * self.calc_marginal(pollution) * self.calc_marginal(smoker)

						else:
							#~cancer
							if parent.option:
								
								if option_flag:
									total = total + (1-self.cgivenps) * self.calc_marginal(pollution) * self.calc_marginal(smoker)
								elif option_flag is False:
									pollution.option=False
									total = total + (1-self.cgivennps) * self.calc_marginal(pollution) * self.calc_marginal(smoker)
								else:
									total = total + (1-self.cgivenps) * self.calc_marginal(pollution) * self.calc_marginal(smoker)
									pollution.option=False
									total = total + (1-self.cgivennps) * self.calc_marginal(pollution) * self.calc_marginal(smoker)

							else:
								if option_flag:
									total = total + (1-self.cgivenpns) * self.calc_marginal(pollution) * self.calc_marginal(smoker)
								elif option_flag is False:
									pollution.option=False
									total = total + (1-self.cgivennpns) * self.calc_marginal(pollution) * self.calc_marginal(smoker)
								else:
									total = total + (1-self.cgivenpns) * self.calc_marginal(pollution) * self.calc_marginal(smoker)
									pollution.option=False
									total = total + (1-self.cgivennpns) * self.calc_marginal(pollution) * self.calc_marginal(smoker)


			#given is child P(A/B) = P(B) * P(B/A)
			for child in node.children:

				if child == item:
					child_found=True
					if child == cancer:

						if node == pollution:
								
							if node.option:
								
								if child.option:
									
									if option_flag:

										total = total + self.cgivenps * self.calc_marginal(pollution) * self.calc_marginal(smoker) * self.calc_marginal(cancer)
									elif option_flag is False:
										smoker.option = False
										total = total + self.cgivenpns * self.calc_marginal(pollution) * self.calc_marginal(smoker) * self.calc_marginal(cancer)
									else:
										total = total + self.cgivenps * self.calc_marginal(pollution) * self.calc_marginal(smoker) * self.calc_marginal(cancer)
										smoker.option = False
										total = total + self.cgivenpns * self.calc_marginal(pollution) * self.calc_marginal(smoker) * self.calc_marginal(cancer)
								
								else:
									if option_flag:
										total = total + (1-self.cgivenps) * self.calc_marginal(pollution) * self.calc_marginal(smoker) * self.calc_marginal(cancer)
									elif option_flag is False:
										smoker.option = False
										total = total + (1-self.cgivenpns) * self.calc_marginal(pollution) * self.calc_marginal(smoker) * self.calc_marginal(cancer)
									else:
										total = total + (1-self.cgivenps) * self.calc_marginal(pollution) * self.calc_marginal(smoker) * self.calc_marginal(cancer)
										smoker.option = False
										total = total + (1-self.cgivenpns) * self.calc_marginal(pollution) * self.calc_marginal(smoker) * self.calc_marginal(cancer)
							else:
								
								if child.option:
								
									if option_flag:
										total = total + self.cgivennps * self.calc_marginal(pollution) * self.calc_marginal(smoker) * self.calc_marginal(cancer)
									elif option_flag is False:
										smoker.option = False
										total = total + self.cgivennpns * self.calc_marginal(pollution) * self.calc_marginal(smoker) * self.calc_marginal(cancer)
									else:
										total = total + self.cgivennps * self.calc_marginal(pollution) * self.calc_marginal(smoker) * self.calc_marginal(cancer)
										smoker.option = False
										total = total + self.cgivennpns * self.calc_marginal(pollution) * self.calc_marginal(smoker) * self.calc_marginal(cancer)
								
								else:

									if option_flag:

										total = total + (1-self.cgivennps) * self.calc_marginal(pollution) * self.calc_marginal(smoker) * self.calc_marginal(cancer)
									elif option_flag is False:
										smoker.option = False
										total = total + (1-self.cgivennpns) * self.calc_marginal(pollution) * self.calc_marginal(smoker) * self.calc_marginal(cancer)
									else:
										total = total + (1-self.cgivennps) * self.calc_marginal(pollution) * self.calc_marginal(smoker) * self.calc_marginal(cancer)
										smoker.option = False
										total = total + (1-self.cgivennpns) * self.calc_marginal(pollution) * self.calc_marginal(smoker) * self.calc_marginal(cancer)


						else:
							#smoker
							if node.option:

								if child.option:
										
									if option_flag:

										total = total + self.cgivenps * self.calc_marginal(pollution) * self.calc_marginal(smoker) * self.calc_marginal(cancer)
									elif option_flag is False:
										pollution.option = False
										total = total + self.cgivennps * self.calc_marginal(pollution) * self.calc_marginal(smoker) * self.calc_marginal(cancer)
									else:
										total = total + self.cgivenps * self.calc_marginal(pollution) * self.calc_marginal(smoker) * self.calc_marginal(cancer)
										pollution.option = False
										total = total + self.cgivennps * self.calc_marginal(pollution) * self.calc_marginal(smoker) * self.calc_marginal(cancer)

								else:

									if option_flag:
										total = total + (1-self.cgivenps) * self.calc_marginal(pollution) * self.calc_marginal(smoker) * self.calc_marginal(cancer)
									elif option_flag is False:
										pollution.option = False
										total = total + (1-self.cgivennps) * self.calc_marginal(pollution) * self.calc_marginal(smoker) * self.calc_marginal(cancer)
									else:
										total = total + (1-self.cgivenps) * self.calc_marginal(pollution) * self.calc_marginal(smoker) * self.calc_marginal(cancer)
										pollution.option = False
										total = total + (1-self.cgivennps) * self.calc_marginal(pollution) * self.calc_marginal(smoker) * self.calc_marginal(cancer)


							else:

								if child.option:
									
									if option_flag:
										total = total + self.cgivenpns * self.calc_marginal(pollution) * self.calc_marginal(smoker) * self.calc_marginal(cancer)
									elif option_flag is False:
										pollution.option = False
										total = total + self.cgivennpns * self.calc_marginal(pollution) * self.calc_marginal(smoker) * self.calc_marginal(cancer)
									else:
										total = total + self.cgivenpns * self.calc_marginal(pollution) * self.calc_marginal(smoker) * self.calc_marginal(cancer)
										pollution.option = False
										total = total + self.cgivennpns * self.calc_marginal(pollution) * self.calc_marginal(smoker) * self.calc_marginal(cancer)


								else:
									if option_flag:

										total = total + (1-self.cgivenpns) * self.calc_marginal(pollution) * self.calc_marginal(smoker) * self.calc_marginal(cancer)
									
									elif option_flag is False:
										pollution.option = False
										total = total + (1-self.cgivennpns) * self.calc_marginal(pollution) * self.calc_marginal(smoker) * self.calc_marginal(cancer)

									else:

										total = total + (1-self.cgivenpns) * self.calc_marginal(pollution) * self.calc_marginal(smoker) * self.calc_marginal(cancer)
										pollution.option = False
										total = total + (1-self.cgivennpns) * self.calc_marginal(pollution) * self.calc_marginal(smoker) * self.calc_marginal(cancer)


					elif child == dyspnoea:

						if node.option:

							if child.option:
								#P(C/d)=P(d)*P(d/C)
								#P(A/B)=P(B)*P(B/A)
								total = total + self.dgivenc * self.calc_marginal(dyspnoea)
							else:

								total = total + self.dgivennc * self.calc.marginal(dyspnoea)

						else:

							if child.option:

								total = total + (1-self.dgivenc) * self.calc_marginal(dyspnoea)
							else:

								total = total + (1-self.dgivennc) * self.calc.marginal(dyspnoea)

					else:
						#xray
						if node.option:

							if child.option:

								total = total + self.xgivenc * self.calc_marginal(xray)
							else:

								total = total + self.xgivennc * self.calc.marginal(xray)

						else:

							if child.option:

								total = total + (1-self.xgivenc) * self.calc_marginal(xray)
							else:

								total = total + (1-self.xgivennc) * self.calc.marginal(xray)


		#Given is not parent or child (independent)
			if child_found is not True and parent_found is not True:
				total = total + self.calc_marginal(node) * self.calc_marginal(parent)

		#print "Conditional probability for",node.name,"being",node.option, "given", given.name,"being",given.option,"is",total
		return total



		# Node / child
		#P(A/B) = P(B) * P(B/A)	

		
		# Node / Node
		#P(A/B) = P(A)P(B)


	def calc_joint(self, node, args):
		total=0

		#if not parent or child independent
		#P(AB) = P(A)*P(B)

		#else
		#P(AB) = P(B)*P(A|B)

		child_found = False
		parent_found = False
		joint = 0

		pollution=self.find('pollution')
		smoker=self.find('smoker')
		cancer=self.find('cancer')
		dyspnoea=self.find('dyspnoea')
		xray=self.find('xray')

		if len(args) > 1:
			option_flag = args[1].option

		
		for item in args:

			for parent in node.parents:

				if parent == item:
					parent_found=True

					total = total + self.calc_conditional(node, parent, option_flag) * self.calc_marginal(parent)
					

			#given is child P(AB) = P(B/A) * P(A)
			for child in node.children:

				if child == item:
					child_found=True
					if child == cancer:

						if node == pollution:
								
							if node.option:
								
								if child.option:
								
									total = total + self.cgivenps * self.calc_marginal(pollution) * self.calc_marginal(smoker) * self.calc_marginal(cancer)
									smoker.option = False
									total = total + self.cgivenpns * self.calc_marginal(pollution) * self.calc_marginal(smoker) * self.calc_marginal(cancer)
								
								else:
									total = total + (1-self.cgivenps) * self.calc_marginal(pollution) * self.calc_marginal(smoker) * self.calc_marginal(cancer)
									smoker.option = False
									total = total + (1-self.cgivenpns) * self.calc_marginal(pollution) * self.calc_marginal(smoker) * self.calc_marginal(cancer)
							else:
								
								if child.option:
								
									total = total + self.cgivennps * self.calc_marginal(pollution) * self.calc_marginal(smoker) * self.calc_marginal(cancer)
									smoker.option = False
									total = total + self.cgivennpns * self.calc_marginal(pollution) * self.calc_marginal(smoker) * self.calc_marginal(cancer)
								
								else:
									total = total + (1-self.cgivennps) * self.calc_marginal(pollution) * self.calc_marginal(smoker) * self.calc_marginal(cancer)
									smoker.option = False
									total = total + (1-self.cgivennpns) * self.calc_marginal(pollution) * self.calc_marginal(smoker) * self.calc_marginal(cancer)


						else:
							#smoker
							if node.option:

								if child.option:
									
									total = total + self.cgivenps * self.calc_marginal(pollution) * self.calc_marginal(smoker) * self.calc_marginal(cancer)
									pollution.option = False
									total = total + self.cgivennps * self.calc_marginal(pollution) * self.calc_marginal(smoker) * self.calc_marginal(cancer)

								else:

									total = total + (1-self.cgivenps) * self.calc_marginal(pollution) * self.calc_marginal(smoker) * self.calc_marginal(cancer)
									pollution.option = False
									total = total + (1-self.cgivennps) * self.calc_marginal(pollution) * self.calc_marginal(smoker) * self.calc_marginal(cancer)


							else:

								if child.option:
									
									total = total + self.cgivenpns * self.calc_marginal(pollution) * self.calc_marginal(smoker) * self.calc_marginal(cancer)
									pollution.option = False
									total = total + self.cgivennpns * self.calc_marginal(pollution) * self.calc_marginal(smoker) * self.calc_marginal(cancer)

								else:

									total = total + (1-self.cgivenpns) * self.calc_marginal(pollution) * self.calc_marginal(smoker) * self.calc_marginal(cancer)
									pollution.option = False
									total = total + (1-self.cgivennpns) * self.calc_marginal(pollution) * self.calc_marginal(smoker) * self.calc_marginal(cancer)

					elif child == dyspnoea:

						if node.option:

							if child.option:
								#P(C/d)=P(d)*P(d/C)
								#P(A/B)=P(B)*P(B/A)
								total = total + self.dgivenc * self.calc_marginal(dyspnoea)
							else:

								total = total + self.dgivennc * self.calc.marginal(dyspnoea)

						else:

							if child.option:

								total = total + (1-self.dgivenc) * self.calc_marginal(dyspnoea)
							else:

								total = total + (1-self.dgivennc) * self.calc.marginal(dyspnoea)

					else:
						#xray
						if node.option:

							if child.option:

								total = total + self.xgivenc * self.calc_marginal(xray)
							else:

								total = total + self.xgivennc * self.calc.marginal(xray)

						else:

							if child.option:

								total = total + (1-self.xgivenc) * self.calc_marginal(xray)
							else:

								total = total + (1-self.xgivennc) * self.calc.marginal(xray)


		#Given is not parent or child (independent)
			if child_found is not True and parent_found is not True:
				total = total + self.calc_marginal(node) * self.calc_marginal(item)

		return total


if __name__ == "__main__":
    main()