"""
A simple module for creating human-readable tables in Python
"""

class strfry:

	def table(columns=1, *rows, separator=' ') # wip
		"""
		Takes int columns, tuple of dicts rows, string separator
		Returns rows in dict form
		"""
		 
	
	def align(*tables): # wip
		"""
		Takes rows in dict form
		Returns string in table format
		"""
		columns = 

		keys = list(self.__dict__.keys())
		values = list(self.__dict__.values())
		width = len(max(keys, key=len)) + separator + 1

		for key in keys:
			column = (key + ':').ljust(width, '-')
			print('c', column)

		table = dict(zip(column, values))
		output = ''
		print('table: ', table)
		
		for key, value in table:

			output.append(f'{dict.keys[key]} {dict.values[value]}\n')

		return output