import csv
import pdb

from family_tree import FamilyTree
from Person import Person

def add_node(tree, unmatched_persons):
	"""This function takes the current family tree and the list of people not assigned to a tree
	and links them into the tree"""

	#First list all unknown persons
	print("Here all of the people who haven't been added to the tree:")
	
	i = 0
	for person in unmatched_persons:
		print(f"{i+1}. {person.first_name} {person.last_name}")
		i += 1

	assign = int(input("Which person would you like to assign? "))
	assign -= 1
	unmatched_parent = unmatched_persons[assign]

	print(f"You selected {unmatched_parent.first_name} {unmatched_parent.last_name}")

	print("Here are all of the unassigned parent slots in the tree:")
	"""maybe make a function that only display's open slots"""

	options = tree.print_root_open()

	selection = int(input("Where would you like this person added? "))
	unmatched_child = options[selection]['child']


	unmatched_child.add_parent(unmatched_parent, options[selection]['slot'])
	unmatched_persons.pop(assign)

def read_data(root):
	"""Reads in a csv, and adds all members to unmatched_persons array"""

	filename = 'Hanson_long.csv'
	with open(filename) as f:
		reader = csv.reader(f)
		header_row = next(reader)

	#Get info from csv

		for row in reader:
			first_name = row[0]
			middle_name = row[1]
			last_name = row[2]
			nickname = row[3]
			comment = row[4]
			birth = row[5]
			death = row[6]
			child_first = row[7]
			child_last = row[8]
			relation = row[9]
			#print(f"{first_name} {middle_name} {last_name}")
			new_person = Person(first_name=first_name, middle_name=middle_name, last_name=last_name, nickname=nickname,
				comment=comment, birth=birth, death=death)
			
			did_match = try_match(new_person, child_first, child_last, relation, root)

			if not did_match:
				print(f"No match found for {first_name.title()} {last_name.title()} value of did match is {did_match}")
				unmatched_persons.append(new_person)	

def try_match(unmatched, child_first, child_last, relation, matched, did_match=False):
	"""Tries to match unmatched_persons with those in the tree based on first and last name"""
	
	if did_match:
		return did_match

	matched_name = f"{matched.first_name} {matched.last_name}"
	unmatched_name = f"{child_first.title()} {child_last.title()}"
	
	if matched_name == unmatched_name:
		if relation == "father":
			print(f"we have a father match for {unmatched.first_name}")
			did_match = True
			matched.father = unmatched
		elif relation == "mother":
			print(f"we have a mother match for {unmatched.first_name}")
			did_match = True
			matched.mother = unmatched
		return did_match


	if not did_match:
		if matched.father:
			print(f"{matched.first_name} has a father, so checking father for match")
			did_match = try_match(unmatched, child_first, child_last, relation, matched.father, did_match)
		if matched.mother:
			print(f"{matched.first_name} has a mother, so checking father for match")
			did_match = try_match(unmatched, child_first, child_last, relation, matched.mother, did_match)

	
	print(f"returning did_match {did_match} {unmatched.first_name}")
	return did_match




if __name__ == '__main__':

	Hanson = FamilyTree("Hanson")
	Drew=Person(first_name="Drew", last_name="Hanson", comment = "Its me")
	Hanson.root = Drew
	Janis = Person(first_name="Janis", last_name="Hanson", comment="this is mom")
	Drew.mother = Janis
	unmatched_persons = []

	read_data(Hanson.root)
	

	while True:
		print("""
Menu:
1. Create a person
2. Link a person
3. View entire tree
q. Quit
""")
		selection = input("What would you like to do? ")

		if selection == "1":
			new_person = Person()
			if new_person:
				unmatched_persons.append(new_person)
		elif selection == "2":
			"""link people, will need unmatched people, tree"""
			add_node(Hanson, unmatched_persons)
		elif selection == "3":
			"""Some function to print the tree"""
			Hanson.print_root()
		else:
			break
