def buildBoard(white, black, size):
    string = ''
    board = []
    for y in range(0, size):
        for x in range(0, size):
            if((x + y) % 2 == 0):
                board.append(white)
            else:
                board.append(black)
        board.append('\n')
    return string.join(board)

print(buildBoard('  ', '#', 8))