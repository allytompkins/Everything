def collatz(number):
    if number % 2 == 0:
        print(f"{number} is an even number")
        print(f"{number} // 2 =", number // 2)
        calc = number // 2
        return calc

    else:
        print(f"{number} is an odd number")
        print(f"3 * {number} + 1 = ", 3 * number + 1)
        calc = 3 * number + 1
        return calc

print("Enter a number please!")
guess = int(input())
while guess != 1:
    guess = collatz(int(guess))

    



# What if user doesnt type an integer?
