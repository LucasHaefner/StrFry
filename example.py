import strfry

rows_example = [['R1C1', 'R1C2', 'R1C3'],
            	['R2C1', 'R2C2', 'R2C3'],
            	['R3C1', 'R3C2', 'R3C3']]

cols_example = [['R1C1', 'R2C1', 'R3C1'],
            	['R1C2', 'R2C2', 'R3C2'],
            	['R1C3', 'R2C3', 'R3C3']]

print('Rows:\n')
print(strfry.align(rows_example, 'ROWS'))

print('Flipped:\n')
rows_example = strfry.flip(rows_example)
print(strfry.align(rows_example, 'ROWS'))

print('Columns:\n')
print(strfry.align(cols_example, 'COLS'))

print('Flipped:\n')
cols_example = strfry.flip(cols_example)
print(strfry.align(cols_example, 'COLS'))