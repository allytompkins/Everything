grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

newString = ''

for i in range(len(grid)):
    newString += str(grid[i][0])

# print(grid[0][0], grid[1][0], grid[2][0], grid[3][0], grid[4][0], grid[5][0], grid[6][0], grid[7][0], grid[8][0])


newString1 = '\n'
for i in range(len(grid)):
    newString1 += str(grid[i][1])

newString2 = '\n'
for i in range(len(grid)):
    newString2 += str(grid[i][2])

newString3 = '\n'
for i in range(len(grid)):
    newString3 += str(grid[i][3])

newString4 = '\n'
for i in range(len(grid)):
    newString4 += str(grid[i][4])

newString5 = '\n'
for i in range(len(grid)):
    newString5 += str(grid[i][5])

print(newString+newString1+newString2+newString3+newString4+newString5)
