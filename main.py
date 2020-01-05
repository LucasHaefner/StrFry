# ...StrFry/main.py

"""
A simple module for creating human-readable tables in Python
"""

class Table:

	def __init__(self, input):

		self.input = input

	def normalize(self):

		return {sort: [[str(i) for i in list] for list in nest] for sort, nest in self.input}

	# def flip(self):


	# def create(self):

my_table = {'group_col':[['THIS', 'IS1', 'ROW1'],
						 ['IS'  , 'IS2', 'ROW2'],
						 ['COL' , 'IS3', 'ROW3']]
		   }

# print(table(columns))
table = Table(my_table)
print(table.normalize())

# implement separators for each column
# allow different width for each column
# {k: [[str(j) for j in i] for i in v] for k, v in the_dictionary}