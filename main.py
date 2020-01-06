# ...StrFry/main.py

"""
A simple module for creating human-readable tables in Python
"""

class Table:

    def __init__(self, table, sort='row'):

        self.table = table          
        self.sort = sort
        self.errors = {'sort':f'Invalid sorting key \'{self.sort}\'. Use \'row\' or \'col\'.'}


    def normalize(self):

        self.table = {sort: [[str(i) for i in list] for list in nest] for sort, nest in self.table.items()}

        return self.table

    def flip_by_rows(self):
        pass

    def flip_by_columns(self):

        set = []

        for index, list in enumerate(self.table):
            
            group = []

            for list in self.table:
                
                group.append(list[index])

            set.append(group)
            
        return set

    def flip(self):
        
        if self.sort == 'rows':

            self.table = self.flip_by_columns()
            self.sort = 'columns'

        elif self.sort == 'columns':

            self.table = self.flip_by_rows()
            self.sort = 'rows'

        else:

            raise Exception(self.errors['sort'])
        
        return self.table


    # def create(self):

my_table = [['THIS', 'IS1', 'ROW1'],
            ['IS'  , 'IS2', 'ROW2'],
            ['COL' , 'IS3', 'ROW3']]

table = Table(my_table, 'rows')
[print(table.flip()) for _ in range(3)]

# implement (different) separators for each column