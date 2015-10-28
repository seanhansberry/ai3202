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

    #First Test
    #Should print out list of nodes in Bayes Net
    #for node in bayes.network:
    #	print node.name, node.info

    #Second Test Update Element in List
    #bayes.update('dyspnoea', 'marginal' , 'b|idgaf' ,0.2)
    #bayes.update('dyspnoea', 'marginal', 'c|s,p', 0.5)
    print "Passed 2-4"
    print



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
				pollution.info['low'] = value
				pollution.info['high'] = 1-value
				print "Pollution Prior Set!:", float(value)

			elif a == "S":
				#Set Smoking Prior
				smoker=bayes.find('smoker')
				smoker.info['true'] = value
				smoker.info['false'] = 1-value
				print "Smoker Prior Set!:", value

			#setting the prior here works if the Bayes net is already built
			#setPrior(a[0], float(a[1:])
		elif o in ("-m"):
			print "flag", o
			print "args", a

			
			#print "Unit test 2: Calculate marginal dyspnoea"
			#print "..."
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
				marginal = bayes.calc_marginal(current_node, 'false')
			else:
				marginal = bayes.calc_marginal(current_node, 'true')
			
			if false:
				n_flag='false'
			else:
				n_flag='true'

			print "Marginal for", current_node.name, "being", n_flag, "is:", marginal








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
			flag = 'true'
			my_list = list(a)
			for argument in my_list:
				if i==0:

					if argument == '~':

						option = my_list[i+1]
						flag='false'

					else:
						option = argument

				else:
					conditions.append(argument)

				i=i+1


			print "arg:", option, "conditions:",conditions

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
				flag = 'false'

			elif option == "~s":
				current_node=bayes.find('smoker')
				flag = 'false'

			elif option == "~c":
				current_node=bayes.find('cancer')
				flag = 'false'

			elif option == "~x":
				current_node=bayes.find('xray')
				flag = 'false'

			elif option == "~d":
				current_node = bayes.find('dyspnoea')
				flag = 'false'

			else:
				print "unhandled option:", option

			conditional = bayes.get_conditional(current_node, conditions, flag)
			print "Conditional probability for",current_node.name ,"given",conditions,"is",conditional



		elif o in ("-j"):
			print "flag", o
			print "args", a

			i=0
			conditions = []
			flag = 'true'
			my_list = list(a)
			for argument in my_list:
				if i==0:

					if argument == '~':

						option = my_list[i+1]
						flag='false'

					else:
						option = argument

				else:
					conditions.append(argument)

				i=i+1


			print "arg:", option, "conditions:",conditions

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
				flag = 'false'

			elif option == "~s":
				current_node=bayes.find('smoker')
				flag = 'false'

			elif option == "~c":
				current_node=bayes.find('cancer')
				flag = 'false'

			elif option == "~x":
				current_node=bayes.find('xray')
				flag = 'false'

			elif option == "~d":
				current_node = bayes.find('dyspnoea')
				flag = 'false'

			elif option == "P":
					current_node=bayes.find('pollution')
					flag='both'

			elif option == "S":
				current_node=bayes.find('smoker')
				flag='both'

			elif option == "C":
				current_node=bayes.find('cancer')
				flag='both'

			elif option == "X":
				current_node=bayes.find('xray')
				flag='both'

			elif option == "D":
				current_node = bayes.find('dyspnoea')
				flag='both'

			else:
				print "unhandled option:", option

			if flag=='both':
				joint1 = bayes.get_conditional(current_node, conditions, 'true')
				joint2 = bayes.get_conditional(current_node, conditions, 'false')
				print "Joint probability for",current_node.name ,"being true with",conditions,"is", joint1
				print "Joint probability for",current_node.name ,"being false with",conditions,"is", joint2

			else:
				joint = bayes.get_joint(current_node, conditions, flag, option)
				print "Joint probability for",current_node.name ,"being",flag,"with",conditions,"is", joint



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

			
			
			#Should calculate marginal density for dyspnoea
			#Find marginal for args[counter]
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
				
				if false:
					marginal = bayes.calc_marginal(current_node, 'false')
				else:
					marginal = bayes.calc_marginal(current_node, 'true')
				
				if false:
					n_flag='false'
				else:
					n_flag='true'

				print "Marginal for", current_node.name, "being", n_flag, "is:", marginal









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
				flag = 'true'
				my_list = list(a)
				for argument in my_list:
					if i==0:

						if argument == '~':

							option = my_list[i+1]
							flag='false'

						else:
							option = argument

					else:
						conditions.append(argument)

					i=i+1


				#print "arg:", option, "conditions:",conditions

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
					flag = 'false'

				elif option == "~s":
					current_node=bayes.find('smoker')
					flag = 'false'

				elif option == "~c":
					current_node=bayes.find('cancer')
					flag = 'false'

				elif option == "~x":
					current_node=bayes.find('xray')
					flag = 'false'

				elif option == "~d":
					current_node = bayes.find('dyspnoea')
					flag = 'false'

				else:
					print "unhandled option:", option


				conditional = bayes.get_conditional(current_node, conditions, flag)
				print "Conditional probability for",current_node.name ,"given",conditions,"is",conditional



			elif o in ("-j"):
				print "flag", o
				print "args", a

				i=0
				conditions = []
				flag = 'true'
				my_list = list(a)
				for argument in my_list:
					if i==0:

						if argument == '~':

							option = my_list[i+1]
							flag='false'

						else:
							option = argument

					else:
						conditions.append(argument)

					i=i+1


				print "arg:", option, "conditions:",conditions

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
					flag = 'false'

				elif option == "~s":
					current_node=bayes.find('smoker')
					flag = 'false'

				elif option == "~c":
					current_node=bayes.find('cancer')
					flag = 'false'

				elif option == "~x":
					current_node=bayes.find('xray')
					flag = 'false'

				elif option == "~d":
					current_node = bayes.find('dyspnoea')
					flag = 'false'

				elif option == "P":
						current_node=bayes.find('pollution')
						flag='both'

				elif option == "S":
					current_node=bayes.find('smoker')
					flag='both'

				elif option == "C":
					current_node=bayes.find('cancer')
					flag='both'

				elif option == "X":
					current_node=bayes.find('xray')
					flag='both'

				elif option == "D":
					current_node = bayes.find('dyspnoea')
					flag='both'

				else:
					print "unhandled option:", option

				if flag=='both':
					joint1 = bayes.get_conditional(current_node, conditions, 'true')
					joint2 = bayes.get_conditional(current_node, conditions, 'false')
					print "Joint probability for",current_node.name ,"being true with",conditions,"is", joint1
					print "Joint probability for",current_node.name ,"being false with",conditions,"is", joint2

				else:
					joint = bayes.get_joint(current_node, conditions, flag, option)
					print "Joint probability for",current_node.name ,"being",flag,"with",conditions,"is", joint



    # ...

class Node():
	def __init__(self, name, info):
		self.name = name
		self.info = info
		self.parent1=None
		self.parent2=None
		self.child1=None
		self.child2=None

	def set_family(self, parent1 , parent2, child1, child2):
		self.parent1=parent1
		self.parent2=parent2
		self.child1=child1
		self.child2=child2

class BayesNet():
	def __init__(self):
		self.network = []

	def find(self, node):
		for item in self.network:
			if item.name == node:
				return item
		
		print "Node not Found!:", node

	def initialize(self):
		self.network.append(Node('pollution', {'true' : 0.9, 'false' : 0.1}))
		self.network.append(Node('smoker', { 'true' : 0.3, 'false' : 0.7}))
		self.network.append(Node('cancer', { 'true': {'ps' : 0.05, 'p~s': 0.02, '~pS': 0.03, '~p~s': 0.001}, 'false' : {'ps' : 0.95, 'p~s': 0.98, '~pS': 0.97, '~p~s': 0.999}}))
		self.network.append(Node('dyspnoea', { 'true' : {'c' : 0.65, '~c': 0.30}, 'false' : {'c' : 0.35, '~c': 0.70}}))
		self.network.append(Node('xray', { 'true' : {'c' : 0.90, '~c': 0.20}, 'false' : {'c' : 0.10, '~c': 0.80}}))
		

		pollution=self.find('pollution')
		smoker=self.find('smoker')
		cancer=self.find('cancer')
		dyspnoea=self.find('dyspnoea')
		xray=self.find('xray')

		pollution.set_family(None, None, cancer, None) 
		smoker.set_family(None, None, cancer, None)
		cancer.set_family(pollution, smoker, dyspnoea, xray)
		dyspnoea.set_family(cancer, None, None, None)
		xray.set_family(cancer, None, None, None)


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

	def calc_marginal(self, node, option):
		
		numerator=0
		denominator=0

		#Base Case

		if node.parent1 == None:
			
			for item, probability in node.info.items():

				if item == option:

					numerator = numerator + probability

				denominator = denominator + probability

			value = numerator / denominator

		else:
			
			for item, probability in node.info.items():
				
				#print item, probability

				for element, number in probability.items():
					
					if item == option:

						numerator = numerator + number

					denominator = denominator + number

			#print "numerator for base node",node.name,"is:", numerator
			value = numerator / denominator


		#print "Marginal for node", node.name, "is:", value
		return value

	def get_conditional(self, node, conditions, flag):
		
		start_node = node
		total = 0
		sub_total = 0
		denominator = 0

		conditionals = {}
		for name in conditions:
				
			if name == "p":
				pollution = self.find('pollution')
				conditionals['true']=pollution
			
			elif name == "s":
				smoker = self.find('smoker')
				conditionals['true']=smoker

			elif name == "c":
				cancer = self.find('cancer')
				conditionals['true']=cancer

			elif name == "x":
				xray = self.find('xray')
				conditionals['true']=xray
			
			elif name == "d":
				dyspnoea = self.find('dyspnoea')
				conditionals['true']=dyspnoea
			
			elif name == "~p":
				pollution = self.find('pollution')
				conditionals['false']=pollution
			
			elif name == "~s":
				smoker = self.find('smoker')
				conditionals['false']=smoker			

			elif name == "~c":
				cancer = self.find('cancer')
				conditionals['false']=cancer
			
			elif name == "~x":
				xray = self.find('xray')
				conditionals['false']=xray
			
			elif name == "~d":
				dyspnoea = self.find('dyspnoea')
				conditionals['false']=dyspnoea

		found=False
		i=0
		if node.parent1 is None:

			total = node.info[flag]

		else:
		#P(A)	
			for item, value in node.info[flag].items():
				#print "item:",item,"value:",value
				for word in conditions:
					if item == word:
						total = total + value
						found=True

				if not found:

					total = total + self.calc_marginal(node, flag)

				i=i+1
		#print "P(A)",total
		
		for prob_type, node in conditionals.items():
		#P(B|A)
			if node.parent1 is None:

				sub_total = sub_total + node.info[prob_type]

			else:
				for element, probabilities in node.info[prob_type].items():
				
					#print element, probabilities
					
					sub_total = sub_total + probabilities


		#print "P(B|A):",sub_total
		#print "Conditionals:", conditions


		for prob_type, cur_node in conditionals.items():
		#P(B)
			for item, probability in cur_node.info.items():
				if item == prob_type:
					if cur_node.parent1 is None:
						denominator = probability

					else:
						for element, value in cur_node.info[prob_type].items():
							denominator = denominator + value

	
		return (total * sub_total) / denominator


	def get_joint(self, node, options, flag, option):
		
		conditional = 1

		joint = 0

		conditionals = {}
		for name in options:
				
			if name == "p":
				pollution = self.find('pollution')
				conditionals['true']=pollution
			
			elif name == "s":
				smoker = self.find('smoker')
				conditionals['true']=smoker

			elif name == "c":
				cancer = self.find('cancer')
				conditionals['true']=cancer

			elif name == "x":
				xray = self.find('xray')
				conditionals['true']=xray
			
			elif name == "d":
				dyspnoea = self.find('dyspnoea')
				conditionals['true']=dyspnoea
			
			elif name == "~p":
				pollution = self.find('pollution')
				conditionals['false']=pollution
			
			elif name == "~s":
				smoker = self.find('smoker')
				conditionals['false']=smoker			

			elif name == "~c":
				cancer = self.find('cancer')
				conditionals['false']=cancer
			
			elif name == "~x":
				xray = self.find('xray')
				conditionals['false']=xray
			
			elif name == "~d":
				dyspnoea = self.find('dyspnoea')
				conditionals['false']=dyspnoea

			if name == "P":
				pollution = self.find('pollution')
				conditionals['true']=pollution
				condtionals['false']=pollution
			
			elif name == "S":
				smoker = self.find('smoker')
				conditionals['true']=smoker
				condtionals['false']=smoker

			elif name == "C":
				cancer = self.find('cancer')
				conditionals['true']=cancer
				condtionals['false']=cancer

			elif name == "X":
				xray = self.find('xray')
				conditionals['true']=xray
				condtionals['false']=xray
			
			elif name == "D":
				dyspnoea = self.find('dyspnoea')
				conditionals['true']=dyspnoea
				condtionals['false']=dyspnoea

		#P(AB) = P(A|B)P(B) = P(B|A)P(A)
		found=False
		i=0

		#P(A)
		total = self.calc_marginal(node, flag)
		#print "P(A):", total

		#P(B|A)	
		for prob_type, node in conditionals.items():
			del options[0]
			conditional = conditional * self.get_conditional(node, option, flag)
	
		return total * conditional




if __name__ == "__main__":
    main()