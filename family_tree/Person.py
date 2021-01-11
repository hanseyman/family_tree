class Person:
	
	def __init__(self, first_name='', middle_name='', last_name='', nickname='',
		comment='', birth='', death=''):
		
		if not first_name:
			first_name = input("What is this person's first name? ")

		self.first_name = first_name.title()

		if not last_name:
			last_name = input("What is this person's last name? ")
		self.last_name = last_name.title()

		# if not comment:
		# 	comment = input("What comments would you like to add? Can be blank: ")
		self.comment = comment
		self.middle_name = middle_name.title()
		self.nickname = nickname.title()
		self.birth = birth
		self.death = death
		self.father = ''
		self.mother = ''

		self.full_name = ''
		if self.first_name:
			self.full_name += f"{self.first_name}"
		if self.middle_name:
			self.full_name += f" {self.middle_name}"
		if self.last_name:
			self.full_name += f" {self.last_name}"
		if self.nickname:
			self.full_name += f" '{self.nickname}'"

	def AddMember(self):
		"""Add a member to the tree"""
		self.first_name = input("First name? ")
		self.last_name = input("Last name? ")
		self.comment = input("Comments? ")
		self.mother = ""
		self.father = ""

	def print_cascade(self):

		
		misc = ""
		if self.birth:
			misc += f"b. {self.birth} "
		if self.death:
			misc += f"d. {self.death} "
		if self.comment:
			misc += f"{self.comment}"

		

		print(self.full_name)
		print(f"\t{misc}")
		#print(f"\t{parent_str}")
		if self.father:
			print(f"\tFather: {self.father.full_name}")
		if self.mother:
			print(f"\tMother: {self.mother.full_name}")


		if self.father:
			self.father.print_cascade()
		if self.mother:
			self.mother.print_cascade()

	def print_cascade_open(self, options=[]):
		"""Prints unassigned slots"""

		#print(f"here's i: {i}. Here's person: {self.first_name} {self.last_name}")
		if not self.father:
			print(f"{len(options)}. {self.first_name} does not have a father assigned")
			options.append({'child': self, 'slot': 'father'})
		if not self.mother:
			print(f"{len(options)}. {self.first_name} does not have a mother assigned")
			options.append({'child': self, 'slot': 'mother'})


		if self.mother:
			self.mother.print_cascade_open(options)
		if self.father:
			self.father.print_cascade_open(options)

		return options

	def add_parent(self, parent, relationship):
		print(f"Adding {parent.first_name} as {self.first_name}'s {relationship}")
		if relationship == "father":
			self.father = parent
			print(f"{self.first_name} now has father of {self.father.first_name}")
		if relationship == "mother":
			self.mother = parent
			print(f"{self.first_name} now has mother of {self.mother.first_name}")

	def update_person_details(self):
		"""Allow user to update info
		Does not allow to update mother and father"""