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

            if len(self.separators) < len(self.table):

                for _ in range(len(self.table) - 2):

                    self.separators.append(separators[:1][0])

        elif self.sort == 'columns':

            if len(self.separators) < len(self.flip()):

                for _ in range(len(self.flip()) - 2):

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
        Returns 'self.table' with all 'elements' of group' converted to type(str)
        """

        return [[str(element) for element in group] for group in self.table]

    def flip(self):

        """
        Inherits from Table()
        Takes 'self'
        Returns flip floping 'rows' and 'columns' group of 'self.table'
        """
        
        set = []

        for index, group in enumerate(self.table):
            
            line = []

            for list in self.table:
                
                line.append(group[index])

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

        for index, group in enumerate(self.table):

            width.append(len(max(group, key=len)))

        set = []

        for group in self.table:

            line = []

            for index, element in enumerate(group):

                line.append(element.ljust(width[index] + padding))

            set.append(line)

        for group in set:

            for index, element in enumerate(group):

                if index < (len(group) - 1):

                    pair = group[index], group[index + 1]

                    try:

                        char = str(list(self.separators[index].keys())[0])

                    except:

                        char = ''

                    try:

                        if not bool(self.separators[index].get(char)):

                            string += (char + ' ').join(pair)

                        else:

                            string += (' ' + char).join(pair)

                    except:

                        string += ' '.join(pair)

                string += '\n'

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

# error in align() function:
#   separator ends vertically rather than horizontally
#   add flip() functionality to make sauteing simpler