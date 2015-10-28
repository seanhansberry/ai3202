import getopt, sys
from itertools import chain, combinations




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

			print "Unit Test 1: Set prior for pollution OR smoker"
			print "..."
			print
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

			
			print "Unit test 2: Calculate marginal dyspnoea"
			print "..."
			print "Passed!"

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


		
			print "Calculating marginal for",current_node.name
			
			if false:
				marginal = bayes.calc_marginal(current_node, 'false')
			else:
				marginal = bayes.calc_marginal(current_node, 'true')
			
			print "Marginal is:", marginal








		elif o in ("-g"):
			print "flag", o
			print "args", a

			'''you may want to parse a here and pass the left of |
			and right of | as arguments to calcConditional
			'''
			print "Unit test 4! Calculate and return conditional probabilities"
			print "...."
			print


			i=0
			conditions = []
			flag = 'true'
			my_list = list(a)
			for args in my_list:
				if i==0:
					if a == '~':

						option = my_list[i+1]
						flag='true'
					else:
						option = args
				else:
					conditions.append(args)

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


			#Joint density for pollution smoking
			bayes.get_joint(a)
			joint_options = a
			joint_flag = True


		else:
			assert False, "unhandled option"
	
    # ...

class Node():
	def __init__(self, name, info):
		self.name = name
		self.info = info
		self.parent1=None
		self.parent2=None
		self.child1=None
		self.child2=None
		self.use=False
		self.true=False
		self.false=False
		self.m=0
		self.j=0
		self.g=0

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
				
				print item, probability

				for element, number in probability.items():
					
					if item == option:

						numerator = numerator + number

					denominator = denominator + number

			print "numerator for base node",node.name,"is:", numerator
			value = numerator / denominator


		print "Marginal for node", node.name, "is:", value
		return value

	def get_conditional(self, node, conditions, flag):
		
		start_node = node
		print flag
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
				print "item:",item,"value:",value
				for word in conditions:
					if item == word:
						total = total + value
						found=True
				if not found:
					total = total + self.calc_marginal(node, flag)
				i=i+1
		print "P(A)",total
		for prob_type, node in conditionals.items():
		#P(B|A)
			if node.parent1 is None:

				sub_total = sub_total + node.info[prob_type]

			else:
				for element, probabilities in node.info[prob_type].items():
				
					print element, probabilities
					
					sub_total = sub_total + probabilities


		print "P(B|A):",sub_total
		for prob_type, cur_node in conditionals.items():
		#P(B)
			for item, probability in cur_node.info.items():
				if item == prob_type:
					if cur_node.parent1 is None:
						denominator = probability

					else:
						for element, value in cur_node.info[prob_type].items():
							denominator = denominator + value

		print "P(B):",denominator


		print "Conditional probability for", start_node.name, "given options", conditions, "is", (total * sub_total) / denominator
		return (total * sub_total) / denominator


	def get_joint(self, options, want_probability="joint"):
		
		joint = 0
		valid_options = list(options)
		#options = ['P','S','C','D','X','ps','pc','px','pd','psc','psx','psd','pcx','pxd','pscx','pscxd', 'p~s', 'p~c', 'p~x', 'p~d', 'ps~c', 'ps~x', 'ps~d', 'pc~x~', 'px~d', 'p~sc', 'p~sx', 'p~sd', 'p~cx', 'p~xd', 'p~s~c', 'p~s~x', 'p~s~d', 'p~c~x', 'p~x~d', 'p~scx', 'ps~cx', 'psc~x', 'p~s~cx', 'p~sc~x', 'ps~c~x', 'p~s~c~x', 'p~scxd', 'ps~cxd', 'psc~xd', 'pscx~d', 'p~s~cxd', 'p~sc~xd', 'p~scx~d', 'p~s~c~xd', 'p~sc~x~d', 'p~s~cx~d', 'p~s~c~x~d', '~ps','~pc','~px','~pd','~psc','~psx','~psd','~pcx','~pxd','~pscx','~pscxd', '~p~s', '~p~c', '~p~x', '~p~d', '~ps~c', '~ps~x', '~ps~d', '~pc~x~', '~px~d', '~p~sc', '~p~sx', '~p~sd', '~p~cx', '~p~xd', '~p~s~c', '~p~s~x', '~p~s~d', '~p~c~x', '~p~x~d', '~p~scx', '~ps~cx', '~psc~x', '~p~s~cx', '~p~sc~x', '~ps~c~x', '~p~s~c~x', '~p~scxd', '~ps~cxd', '~psc~xd', '~pscx~d', '~p~s~cxd', '~p~sc~xd', '~p~scx~d', '~p~s~c~xd', '~p~sc~x~d', '~p~s~cx~d', '~p~s~c~x~d']
		i=0

		pollution = self.find('pollution')
		smoker = self.find('smoker')
		cancer = self.find('cancer')
		xray = self.find('xray')
		dyspnoea = self.find('dyspnoea')
		
		



def powerset(iterable):
    '''powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)'''
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))



if __name__ == "__main__":
    main()