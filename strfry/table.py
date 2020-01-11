# ...StrFry/main.py

"""
A simple module for creating human-readable tables in Python
"""

class Table:

    def __init__(self, table, separators=[{':':False}], assortment='rows'):

        self.table = table
        self.separators = separators
        self.assortment = assortment
        
        errors = {'assortment':f'Invalid assortmenting key \'{self.assortment}\'. Use \'rows\' or \'columns\'.'}

        if self.assortment == 'rows':

            if len(self.separators) < len(self.table):

                for _ in range(len(self.table) - 2):

                    self.separators.append(separators[:1][0])

        elif self.assortment == 'columns':

            if len(self.separators) < len(self.flip()):

                for _ in range(len(self.flip()) - 2):

                    self.separators.append(separators[:1][0])

        else:

            raise ValueError(errors[assortment])

    def separate(self, chars, alignments):

        """
        Makes it easier to find the correct character to separate later on.
        :param chars: iterable of single characters
        :param alignments: iterable of boolean values :True: center :False: left
        :return: list of dicts :key: char :value: alignment
        """

        return [dict(zip(chars(i), alignments(i))) for i in min(chars, alignment)]

    def normalize(self):

        """
        Allows for text justification for table of non-string elements.
        :return: list of lists of self.table's elements in string form
        """

        return [[str(element) for element in t] for t in self.table]

    def flip(self):

        """
        Switches self.table between ting by lists of rows/lists of columns.
        :return: 'flipped' form of self.table
        """
        
        array = []

        for index, t in enumerate(self.table):
            
            slot = []

            for list in self.table:
                
                slot.append(t[index])

            array.append(slot)

        self.assortment = ['rows' if self.assortment == 'columns' else 'columns']

        return array

    def align(self):

        """
        Inherits from Table()
        Takes 'self'
        Returns string of 'self.table' with left justified elements formatted with a separator
        """

        string = ''
        width = []
        padding = 1

        for index, t in enumerate(self.table):

            width.append(len(max(t, key=len)))

        array = []

        for t in self.table:

            slot = []

            for index, element in enumerate(t):

                slot.append(element.ljust(width[index] + padding))

            array.append(slot)

        for t in array:

            for index, element in enumerate(t):

                if index < (len(t) - 1):

                    pair = t[index], t[index + 1]

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

    def __str__(self):

        table = self.normalize()
        table = self.align()

        return table
    
if __name__ == '__main__':

    my_table = [['R1C1', 'R1C2', 'R1C3'],
                ['R2C1', 'R2C2', 'R2C3'],
                ['R3C1', 'R3C2', 'R3C3']]

    table = Table(my_table)
    print(table())

# error in align() function:
#   separator ends vertically rather than horizontally
#   add flip() functionality to make sauteing simpler