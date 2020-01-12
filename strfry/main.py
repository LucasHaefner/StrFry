from enum import Enum, auto

class AutoName(Enum):
    def _generate_next_value(name, start, count, last_value):
        return False if bool(last_value) else True

class Group(AutoName):
    ROWS = auto()
    COLUMNS = auto()

class Table:
    def __init__(self, table, group: Group, divider=['>:', '|']):
        self.table = table
        self.group = group
        self.divider = divider

    @property
    def group(self):
        return self._sort

    @group.setter
    def group(self, group: Group):
        # if group not in Group:
        #     raise Exception
        self._group = group

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
        return array

    def align(self):
        """
        Adds text justification and divider
        :return: string with left justified elements formatted with a divider
        """
        string = ''
        array, width, indentations, chars = [], [], [], []
        margin = 1
        padding = margin * ' '

        [width.append(len(max(s, key=len))) for s in self.table]

        for i, element in enumerate(self.divider):
            chars.append(element)

            if element[0] == '>' and len(element) > 1:
                indentations.append(True)
                chars[i] = element[1:]
            else:
                indentations.append(False)

        for s in self.table:
            slot = []
            for i, element in enumerate(s):
                slot.append(element.ljust(width[i]))
            array.append(slot)

        for slot in array:
            for i, element in enumerate(slot):
                if i < len(self.table) - 1:
                    try:
                        char = str(chars[i])
                    except:
                        pass
                else:    
                    char = ' '

                try:
                    if indentations[i]:
                        char += 2 * padding
                    elif not indentations[i]:
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
