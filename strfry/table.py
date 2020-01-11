# ...StrFry/main.py

"""
A simple module for creating human-readable tables in Python
"""

class Table:

    def __init__(self, table, separators=[{':':False}], grouping='rows'):

        self.table = table
        self.separators = separators
        self.grouping = grouping
        
        errors = {'grouping':f'Invalid groupinging key \'{self.grouping}\'. Use \'rows\' or \'columns\'.'}

        if self.grouping == 'rows':

            if len(self.separators) < len(self.table):

                for _ in range(len(self.table) - 2):

                    self.separators.append(separators[:1][0])

        elif self.grouping == 'columns':

            if len(self.separators) < len(self.flip()):

                for _ in range(len(self.flip()) - 2):

                    self.separators.append(separators[:1][0])

        else:

            raise ValueError(errors[grouping])

    def separate(self, chars, alignments):

        """
        Makes it easier to find the correct character to separate later on.
        :param chars: iterable of single characters
        :param alignments: iterable of boolean values :True: center :False: left
        :return: list of dicts :key: char :value: alignment
        """

        return [dict(zip(chars(i), alignments(i))) for i in range(min(len(chars), len(alignment)))]

    def normalize(self):

        """
        Allows for text justification for table of non-string elements.
        :return: list of lists of self.table's elements in string form
        """

        return [[str(e) for e in s] for s in self.table]

    def flip(self):

        """
        Switches self.table between ting by lists of rows/lists of columns.
        :return: 'flipped' form of self.table
        """
        
        array = []

        for index, s in enumerate(self.table):
            
            slot = []

            for _ in self.table:
                
                slot.append(s[index])

            array.append(slot)

        self.grouping = ['rows' if self.grouping == 'columns' else 'columns']

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

        [width.append(len(max(s, key=len))) for s in self.table]

        array = []

        for s in self.table:

            slot = []

            for i, element in enumerate(s):

                slot.append(element.ljust(width[i] + padding))

            array.append(slot)

        for slot in array:

            for i, element in enumerate(slot):

                if i < (len(s) - 1):

                    pair = slot[i], slot[i + 1]

                    try:

                        char = str(list(self.separators[i].keys())[0])

                    except:

                        char = ''

                    try:

                        if not bool(self.separators[i].get(char)):

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
    print(table)