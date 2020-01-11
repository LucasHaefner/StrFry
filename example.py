import strfry

rows_example = [['R1C1', 'R1C2', 'R1C3'],
            	['R2C1', 'R2C2', 'R2C3'],
            	['R3C1', 'R3C2', 'R3C3']]

cols_example = [['R1C1', 'R2C1', 'R3C1'],
            	['R1C2', 'R2C2', 'R3C2'],
            	['R1C3', 'R2C3', 'R3C3']]

print('Rows:\n')
rows = strfry.Table(rows_example, 'rows')
print(rows, '\n')

print('Columns:\n')
columns = strfry.Table(cols_example, 'columns')
print(columns, '\n')