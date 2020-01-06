# ...StrFry/main.py

"""
A simple module for creating human-readable tables in Python
"""

class Table:

    def __init__(self, table, sort='rows'):

        self.table = table          
        self.sort = sort
        self.errors = {'sort':f'Invalid sorting key \'{self.sort}\'. Use \'rows\' or \'columns\'.'}

        if self.sort != 'rows' and self.sort != 'columns':

            raise ValueError(self.errors[sort])

    def normalize(self):

        self.table = {sort: [[str(i) for i in list] for list in nest] for sort, nest in self.table.items()}

        return self.table

    def flip(self):
        
        set = []

        for index, list in enumerate(self.table):
            
            group = []

            for list in self.table:
                
                group.append(list[index])

            set.append(group)

        self.table = set
        self.sort = ['rows' if self.sort == 'columns' else 'columns']

        return self.table


    # def create(self):

my_table = [['THIS', 'IS1', 'ROW1'],
            ['IS'  , 'IS2', 'ROW2'],
            ['COL' , 'IS3', 'ROW3']]

table = Table(my_table)
[print(table.flip()) for _ in range(3)]

# implement (different) separators for each column