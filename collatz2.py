def collatz(number):
    if number % 2 == 0:
        print(f"{number} is an even number")
        print(f"{number} // 2 =", number // 2)
        return number // 2
    else:
        print(f"{number} is an odd number")
        print(f"3 * {number} + 1 = ", 3 * number + 1)
        return 3 * number + 1

number = 0
while number != 1:
    print("Enter a number please!")
    guess = int(input())
    collatz(guess)



# What if user doesnt type an integer?
