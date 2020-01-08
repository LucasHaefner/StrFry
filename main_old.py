# ...StrFry/main.py

"""
A simple module for creating human-readable tables in Python
"""

class Table:

    def __init__(self, table, separators=[{':':False}], sort='rows'):

        self.table = table
        self.separators = separators
        self.sort = sort
        self.errors = {'sort':f'Invalid sorting key \'{self.sort}\'. Use \'rows\' or \'columns\'.'}

        if self.sort == 'rows':

            if len(self.separators) < len(self.table):

                for _ in range(len(self.table)):

                    self.separators.append(separators[:1][0])

        elif self.sort == 'columns':

            if len(self.separators) < len(flip(self.table)):

                for _ in range(len(flip(self.table))):

                    self.separators.append(separators[:1][0])

        else:

            raise ValueError(self.errors[sort])

    def separate(self, chars, alignments):

        return [dict(zip(chars(i), alignments(i))) for i in min(chars, alignment)]

    def normalize(self):

        return [[str(i) for i in list] for list in self.table]

    def flip(self):
        
        set = []

        for index, grouping in enumerate(self.table):
            
            group = []

            for list in self.table:
                
                group.append(grouping[index])

            set.append(group)

        self.sort = ['rows' if self.sort == 'columns' else 'columns']

        return set

    def align(self):

        string = ''
        widths = []
        space = ''
        padding = 1

        for index, grouping in enumerate(self.table):

            widths.append(len(max(grouping, key=len)))

        print('Widths: ', widths)

        for grouping in self.table:

            for index, element in enumerate(grouping):

                element = element.ljust(widths[index] + padding)

                for i in range(len(self.table)):

                    char = list(self.separators[i].keys())[0]

                    if self.separators[i][char] == True:

                        string += element + str(char)

                    elif self.separators[i][char] == False:
                
                        string += str(char) + element

        return string


    # def saute(self):

    #     self.normalize()

    #     string = ''

    #     for grouping in self.table:

    #         for element in list:

    #             string += element

    #         string += '\n'

    #     return string


    # def create(self):

my_table = [['THIS', 'IS1', 'ROW1'],
            ['IS'  , 'IS2', 'ROW2'],
            ['COL' , 'IS3', 'ROW3']]

table = Table(my_table)
# [print(table.flip()) for _ in range(3)]
print(table.align())

# implement (different) separators for each column