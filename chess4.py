def buildBoard(white, black, size):
    board = []
    for y in range(0, size):
        for x in range(0, size):
            board.append(white if (x + y) % 2 == 0 else black)
        board.append('\n')
    return ''.join(board)

print(buildBoard('  ', '#', 8))