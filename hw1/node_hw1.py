# DOCUMENTATION
# =====================================
# Class node attributes:
# ----------------------------
# children - dictionary containing the children where the key is child number (1,...,k) and the value is the actual node object
# if node has no children, self.children = None
# value - value at the node
#
#
# The values for bfs should be returned as simply a string of value space value space value. For example if the tree looks like the following:
#     5
#   2   3
#
# The tree data structure is a node with value 5, with a dictionary of children {1: b, 2: c} where b is a node with value 2 and c is a node with value 3.  Both b and c have children of None.
# The bfs traversal of the above tree should return the string '5 2 3'
import Queue

class Node:
	def __init__(self):
		self.value = None
		self.children = None

	def get_value(self):

		'''
		given a node, will return the value at this node
		'''
		return self.value

	def get_children(self):

		'''
		given a node, will return the children of this node
		'''
		return self.children

def breadth_first_search(root):

	'''
	given the root node, will complete a breadth-first-search on the tree, returning the value of each node in the correct order
	'''
	queue=Queue.Queue()
	bfs_order=[]
	if root:
		queue.put(root)
		bfs_order.append(root)
	while queue.qsize()>0:
		node=queue.get()
		children=node.get_children()
		if children:
			for child in children.itervalues():
				queue.put(child)
				bfs_order.append(child)
	result=[]
	for node in bfs_order:
		result.append(node.get_value())
	return result


def tester():
	a = Node()
	a.value = 5
        b = Node()
	b.value = 7
	a.children = {1: b}
	#for more test
	# c=Node()
	# c.value=2
	# a.children={1:b, 2:c}
	# d=Node()
	# d.value=3
	# b.children={1:d}
	print str(a.get_value()) + ' should be 5.'
	print str(a.get_children()) + ' should be {1: ' + str(b) + '}.'
	print str(breadth_first_search(a)) + ' should be 5 7.'

tester()
