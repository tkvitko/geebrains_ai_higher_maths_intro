a = 7
b = 2
matrix = [[5, 10], [7, 12], [11.3, 5], [25, 30]]

for line in matrix:
    for item in line:
        item *= (a + b)
        print(f'{item:>5}', end='')
    print('')
