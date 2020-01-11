# ...StrFry/main.py

class Table:
    def __init__(self, table, separators=[':'], grouping='rows'):
        self.table = table
        self.separators = separators
        self.grouping = grouping
        errors = {'grouping':f'Invalid groupinging key \'{self.grouping}\'. Use \'rows\' or \'columns\'.'}
        
        if self.grouping != 'rows' and self.grouping != 'columns':
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
        Adds text justification and character separator (if valid)
        :retur:s string with left justified elements formatted with a separator
        """
        string = ''
        array, width, alignments = [], [], []
        margin = 1
        padding = margin * ' '

        [width.append(len(max(s, key=len))) for s in self.table]

        for i in self.separators:
            if i[0] == '/' and len(i) > 1:
                alignments.append(True)
                i = i[1:]
            else:
                alignments.append(False)

        for s in self.table:
            slot = []
            for i, element in enumerate(s):
                slot.append(element.ljust(width[i]))
            array.append(slot)

        for slot in array:
            try:
                char = str(list(self.separators[i].keys())[0])
            except:
                char = ' '
            for i, element in enumerate(slot):
                string += f'{element}{padding}{char}{padding}'
            string += '\n'
        return string

    def __str__(self):
        table = self.normalize()
        table = self.align()
        return table
