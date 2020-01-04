# ...StrFry/main.py

"""
A simple module for creating human-readable tables in Python
"""

def list_to_string(list):
	"""
	Takes:
		list : list
			the list to convert
	Returns:
		list : list
			list with all string elements
	"""
	string_list = []

	for index, element in enumerate(list):

		string_list.append(str(element))

	return string_list


def table_to_string(table):
	"""
	Takes:
		table : list of lists
			the table to convert
	Returns:
		table : list of lists
			list(s) with all string elements
	"""
	string_table = []

	for index, list in enumerate(table):

		string_table.append(list_to_string(list))

	return string_table


def row(list, row_num=0, headers=None):
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
	columns = table_to_string(list)

	for index, row in enumerate(columns):

		width.append(len(max(row, key=len)))

	width = max(width) + padding

	for row in columns:

		for index, element in enumerate(row):

			row[index] = element.ljust(width, '-')


	return columns[row_num]


def table(list, headers=None):
	"""
	Takes:
		list : list of lists
			elements for each row
		headers : list (default None)
			a title string for each column
	Returns:
		table : string
			columns and rows aligned in a readable table
	"""
	table = ''

	for i in range(len(columns)):

		table += str(row(columns, i)) + '\n'

	return table


columns = [['ROW_1', 1], ['ROW_2', 2], ['ROW_3', 3]]

print(table(columns))