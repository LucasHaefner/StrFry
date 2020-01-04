# ...StrFry/main.py

"""
A simple module for creating human-readable tables in Python
"""


# imports

# import string


# body

def separate(repeat=1, chars=':', alignments=True):
	"""
	Takes:
		chars : tuple
			char to separate columns
		alignments : tuple
			True for left justified
			False for center justified
	Returns:
		separators : dict
			keys holds chars
			values holds alignments
	"""
	separators = {}

	for i in range(length):

		separators[chars] = aligmnents

	return separators


def row(row_num, columns, separators, headers=None):
	"""
	Takes:
		row_num : int
			the current row to render
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
		rows : list
			tuple(s)
				elements for each column
	"""
	column_set = [columns.keys(), columns.values()] if type(columns) == dict else columns

	margin = 1
	row = ()

	for index, c in enumerate(columns):

		width = len(max(column_set(index), key=len)) + margin
		row.append(str(c).ljust(width, separators.keys()[row_num]))

	return row


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


columns = [('ROW_1', 1), ('ROW_2', 2), ('ROW_3', 3)]
separators = separate(2)

print('SEPARATE: ', separators, '\n')
print('ROW: ', row(0, columns, separators))