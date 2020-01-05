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
                
                # print('element: ', list[index])
                group.append(list[index])
                print('list[index]: ', list[index])

            set.append(group)
            print('group[index]: ', group)

    def flip(self):
        
        if self.sort == 'rows':

            self.table = flip_by_columns(self.table)

        elif self.sort == 'columns':

            self.table = rows(self.table)
            
        else:

            raise Exception(self.errors['sort'])
        # self.table = [flip_by_columns(self.table) if self.sort == 'rows' else flip_by_rows(self.table) if self.sort == 'columns']

        return self.table


    # def create(self):

my_table = [['THIS', 'IS1', 'ROW1'],
            ['IS'  , 'IS2', 'ROW2'],
            ['COL' , 'IS3', 'ROW3']]

# print(table(columns))
table = Table(my_table, 'row')
print(table.flip())
print(table.flip())

# implement separators for each column
# allow different width for each column