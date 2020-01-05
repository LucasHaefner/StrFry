# ...StrFry/main.py

"""
A simple module for creating human-readable tables in Python
"""

def normalize_list(list):
	"""
	Takes:
		list : list
			the list to convert
	Returns:
		list : list
			list with all string elements
	"""
	normal_list = []

	for index, element in enumerate(list):

		normal_list.append(str(element))

	return normal_list


def normalize_table(table):
	"""
	Takes:
		table : list of lists
			the table to convert
	Returns:
		table : list of lists
			list(s) with all string elements
	"""
	normal_table = []

	for index, list in enumerate(table):

		normal_table.append(normalize_list(list))

	return normal_table

# def flip_table(table):


def row(list, row_num=0, separator='|', headers=None):
	"""
	Takes:
		row_num : int
			the current row to render
		list : list of lists
			elements for each row
		headers : list (default None)
			a title string for each column
	Returns:
		rows : list of lists
			list(s)
				elements for each column
	"""
	output = []
	width = []
	padding = 1
	separator = str(separator)
	table = normalize_table(list)
	unsorted = []
	column = []

	for index, list in enumerate(table):

		for list in table:
			
			print('element: ', list[index])


	for index, row in enumerate(table):

		width.append(len(max(row, key=len)))

	print('Width: ', width)
	width = [i + padding for i in width]

	for row in table:

		for index, element in enumerate(row):

			row[index] = element.ljust(width[index])


	for i in range(len(table)):

		output = (separator + ' ').join(table[row_num])

	return output


def table(list, headers=None):
	"""
	Takes:
		list : list of lists
			elements for each row
		separator : list of dicts

		headers : list (default None)
			a title string for each column
	Returns:
		string : string
			columns and rows aligned in a readable table
	"""
	string = ''

	for i in range(len(columns)):

		# string += f'{row(columns, i)}\n'
		string += row(columns, i) + '\n'

	return string


table = {'group_by_rows' : [['ROW_1', 1, '#1'],
							['ROW_2', 2, '#commffffffffffffffffent'],
							['ROW_3', 3, '#oo']
						   ]
		}

# print(table(columns))
table(table)

# implement separators for each column
# allow different width for each column