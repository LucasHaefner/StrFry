from enum import Enum, unique, auto

def normalize(table):
    """
    Allows for text justification for table of non-string elements.
    :return: list of lists of table's elements in string form
    """
    return [[str(e) for e in s] for s in table]

def flip(table):
    """
    Switches table between grouping by lists of rows/lists of columns.
    :return: list of lists of the nth element of each list in table
    """
    array = []

    for i, _ in enumerate(table):
        slot = []
        for s in table:
            slot.append(s[i])
        array.append(slot)
    return array

class AutoName(Enum):
    def _generate_next_value(name, start, count, last_value):
        return False if bool(last_value) else True

@unique
class Group(AutoName):
    ROWS = auto()
    COLUMNS = auto()

def align(table, group: Group, divider=['|', '*']):
    """
    Adds text justification and divider
    :return: string with left justified elements formatted with a divider
    """
    for i, element in enumerate(divider):
        if element == '*':
            for _ in range(len(divider) - i):
                divider.insert(i, divider[i - 1])
    
    string = ''
    array, width, indentations, chars = [], [], [], []
    margin = 1
    padding = margin * ' '

    [width.append(len(max(s, key=len))) for s in table]

    for i, element in enumerate(divider):
        chars.append(element)

        if element[0] == '>' and len(element) > 1:
            indentations.append(True)
            chars[i] = element[1:]
        else:
            indentations.append(False)

    for s in table:
        slot = []
        for i, element in enumerate(s):
            slot.append(element.ljust(width[i]))
        array.append(slot)

    for slot in array:
        for i, element in enumerate(slot):
            if i < len(table) - 1:
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
