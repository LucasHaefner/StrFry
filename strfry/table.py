# ...StrFry/main.py

"""
A simple module for creating human-readable tables in Python
"""

class Table:

    """
    Methods for operating on and printing tables
    """

    def __init__(self, table, separators=[{':':False}], sort='rows'):

        self.table = table
        self.separators = separators
        self.sort = sort
        self.errors = {'sort':f'Invalid sorting key \'{self.sort}\'. Use \'rows\' or \'columns\'.'}

        if self.sort == 'rows':

            if len(self.separators) < (len(self.table) - 1):

                for _ in range(len(self.table) - 1):

                    self.separators.append(separators[:1][0])

        elif self.sort == 'columns':

            if len(self.separators) < (len(self.flip()) - 1):

                for _ in range(len(flip(self.table)) - 1):

                    self.separators.append(separators[:1][0])

        else:

            raise ValueError(self.errors[sort])

    def separate(self, chars, alignments):

        """
        Inherits from Table()
        Takes 'self', iterable 'chars', iterable 'alignments'
        Returns dict of keys 'chars' and values 'alignments'
        """

        return [dict(zip(chars(i), alignments(i))) for i in min(chars, alignment)]

    def normalize(self):

        """
        Inherits from Table()
        Takes 'self'
        Returns 'self.table' with all 'elements' of grouping' converted to type(str)
        """

        return [[str(element) for element in grouping] for grouping in self.table]

    def flip(self):

        """
        Inherits from Table()
        Takes 'self'
        Returns flip floping 'rows' and 'columns' grouping of 'self.table'
        """
        
        set = []

        for index, grouping in enumerate(self.table):
            
            line = []

            for list in self.table:
                
                line.append(grouping[index])

            set.append(line)

        self.sort = ['rows' if self.sort == 'columns' else 'columns']

        return set

    def align(self):

        """
        Inherits from Table()
        Takes 'self'
        Returns string of 'self.table' with left justified elements formatted with a separator
        """

        string = ''
        width = []
        padding = 1

        for index, grouping in enumerate(self.table):

            width.append(len(max(grouping, key=len)))

        set = []

        for grouping in self.table:

            line = []

            for index, element in enumerate(grouping):

                line.append(element.ljust(width[index] + padding))

            line += '\n'
            set.append(line)

        for i in range(len(self.table)):

            char = list(self.separators[i].keys())[0]

            if self.separators[i][char] == False:

                string += (str(char) + ' ').join(set[i])

            elif self.separators[i][char] == True:
                
                string += (' ' + str(char)).join(set[i])

        return string


    def saute(self):

        """
        Inherits from Table()
        Takes 'self'
        Returns properly formatted form of 'self.table'
        """

        table = self.normalize()
        table = self.align()

        return table
    
if __name__ == '__main__':

    my_table = [['R1C1', 'R1C2', 'R1C3'],
                ['R2C1', 'R2C2', 'R2C3'],
                ['R3C1', 'R3C2', 'R3C3']]

    table = Table(my_table)
    print(table.saute())