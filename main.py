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
	for index, element in enumerate(list):

		list[index] = str(element)

	return list


def table_to_string(table):
	"""
	Takes:
		table : list of lists
			the table to convert
	Returns:
		table : list of lists
			list(s) with all string elements
	"""
	for index, list in enumerate(table):

		table[index] = list_to_string(list)

	return table


def row(row_num, columns, headers=None):
	"""
	Takes:
		row_num : int
			the current row to render
		columns : iterable
			elements for each row
		headers : tuple (default None)
			a title string for each column
	Returns:
		rows : list-o'-lists
			list(s)
				elements for each column
	"""
	output = []
	width = []
	margin = 1
	columns = table_to_string(columns)

	for index, row in enumerate(columns):

		width.append(len(max(row, key=len)))

	width = max(width) + margin

	for row in columns:

		for index, element in enumerate(row):

			row[index] = element.ljust(width, '-')

		
	return columns


def table(columns, separators, headers=None):
	"""
	Takes:
		columns : iterable
			elements for each row
		separators : dict
			keys holds chars
				char to separate columns
			values holds aligmnents
				True for left justified
				False for center justified
		headers : tuple (default None)
			a title string for each column
	Returns:
		table : string
			columns and aligned rows in a readable table
	"""
	table = ''

	for i in columns:

		table += row(i, columns, separators, headers)

	return table


columns = [['ROW_1', 1], ['ROW_2', 2], ['ROW_3', 3]]

print('ROW: ', row(0, columns))
# print('SEPARATE: ', separators, '\n')