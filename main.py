# ...StrFry/main.py

"""
A simple module for creating human-readable tables in Python
"""

class Table:

	def __init__(self, input):

		self.input = input

	def normalize(self):

		normal_table = []

		for index, list in enumerate(table.):

			normal_list = []

			for index, element in enumerate(list):

				normal_list.append(str(element))

		normal_table.append(normal_list)

		return normal_table

	# def flip(self):


	# def create(self):

my_table = {'group_col':[['ROW_1', 1, '#1'],
						 ['ROW_2', 2, '#commffffffffffffffffent'],
						 ['ROW_3', 3, '#oo']]
		   }

# print(table(columns))
table = Table(my_table)
print(table.normalize())

# implement separators for each column
# allow different width for each column