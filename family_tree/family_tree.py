from Person import Person

class FamilyTree:
	"""A class to manage family Trees"""

	def __init__(self, name):
		self.name = name
		self.root = ""


	def print_root(self):
		"""Identifies the root node to print the rest of the tree"""
		print(f"""
******************************************************
**													**
**				{self.name}	Tree					**
**													**
******************************************************
			""")

		self.root.print_cascade()

	def print_root_open(self):
		"""Similar to print root, but only prints unassigned parents"""
		options = []
		options = self.root.print_cascade_open()
		return options

	
