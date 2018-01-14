def collatz(number):
    if number % 2 == 0:
        calc = number // 2
        print(calc)
        return calc

    else:
        calc = 3 * number + 1
        print(calc)
        return calc

print("Enter a number please!")
guess = int(input())
while guess != 1:
    guess = collatz(int(guess))





# What if user doesnt type an integer?
