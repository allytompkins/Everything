def buildBoard(white, black, size):
    for y in range(0, size):
            for x in range(0, size):
                    if((x + y) % 2 == 0):
                            print(white, end='')
                    else:
                            print(black, end='')
            print('\n')

buildBoard('  ', '#', 8)