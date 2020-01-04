# ...StrFry/main.py

"""
A simple module for creating human-readable tables in Python
"""


# imports

# import string


# body

"""
table = list of lists [[],[],[]]
"""

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
		rows : list
			list(s)
				elements for each column
	"""
	output = []
	width = []
	margin = 1

	for index, row in enumerate(columns):

		for index, element in enumerate(row):

			row[index] = str(element)

		width.append(len(max(row, key=len)))

	width = max(width) + margin

	for row in columns:

		for index, element in enumerate(row):

			row[index] = element.ljust(width, '-')
			print('Row2: ', row)


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