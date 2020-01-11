# ...StrFry/strfry/main.py

class Table:
    def __init__(self, table, grouping='rows', separators=['>:']):
        self.table = table
        self.grouping = grouping
        self.separators = separators
        errors = {'grouping':f'Invalid groupinging key \'{self.grouping}\'. Use \'rows\' or \'columns\'.'}
        
        if self.grouping == 'rows':
            pass
        elif self.grouping == 'columns':
            self.table = self.flip()
        else:
            raise ValueError(errors[grouping])

    def normalize(self):
        """
        Allows for text justification for table of non-string elements.
        :return: list of lists of self.table's elements in string form
        """
        return [[str(e) for e in s] for s in self.table]

    def flip(self):
        """
        Switches self.table between ting by lists of rows/lists of columns.
        :return: list of lists of the nth element of each list in self.table
        """
        array = []

        for i, s in enumerate(self.table):
            slot = []
            for e in s:
                slot.append(e)
            array.append(slot)
        self.grouping = ['rows' if self.grouping == 'columns' else 'columns']
        return array

    def align(self):
        """
        Adds text justification and character separator (if valid)
        :return: string with left justified elements formatted with a separator
        """
        string = ''
        array, width, alignments, chars = [], [], [], []
        margin = 1
        padding = margin * ' '

        [width.append(len(max(s, key=len))) for s in self.table]

        for i, element in enumerate(self.separators):
            chars.append(element)

            if element[0] == '>' and len(element) > 1:
                alignments.append(True)
                chars[i] = element[1:]
            else:
                alignments.append(False)

        for s in self.table:
            slot = []
            for i, element in enumerate(s):
                slot.append(element.ljust(width[i]))
            array.append(slot)

        for slot in array:
            for i, element in enumerate(slot):
                try:
                    char = str(chars[i])
                except:
                    char = ' '

                try:
                    if alignments[i]:
                        char += 2 * padding
                    elif not alignments[i]:
                        char = f'{padding}{char}{padding}'
                except:
                    char += padding

                string += f'{element}{char}'
            string += '\n'
        return string

    def __str__(self):
        table = self.normalize()
        table = self.align()
        return table
