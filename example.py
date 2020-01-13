import strfry

rows_example = [['R1C1', 'R1C2', 'R1C3'],
            	['R2C1', 'R2C2', 'R2C3'],
            	['R3C1', 'R3C2', 'R3C3']]

cols_example = [['R1C1', 'R2C1', 'R3C1'],
            	['R1C2', 'R2C2', 'R3C2'],
            	['R1C3', 'R2C3', 'R3C3']]

print('Rows:\n')
rows = strfry.align(rows_example, 'ROWS')
print(rows)

print('Flipped:\n')
print('DEBUG: ', rows_example)
rows_example = rows.flip()
print('DEBUG: ', rows_example)
print(rows)

print('Columns:\n')
columns = strfry.align(cols_example, 'COLS')
print(columns)

print('Flipped:\n')
print('DEBUG: ', cols_example)
cols_example = columns.flip()
print('DEBUG: ', cols_example)
print(columns)