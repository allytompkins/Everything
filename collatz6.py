

def collatz3(inputy):

    listy = [inputy]

    while inputy != 1:
        if inputy % 2 == 0:
            inputy = inputy // 1
        else:
            inputy = 3 * inputy + 1

        listy.append(inputy)

    return listy

userInput = input('Type in a number:')

while True:
    try:
        userInput = int(userInput)
        break
    except ValueError:
        userInput = input('That is not a number. Type in a number:')

collatzSeq = collatz3(userInput)
print(collatzSeq)

#  https://doitforthegram.wordpress.com/2016/01/22/the-collatz-conjecture-in-python/
