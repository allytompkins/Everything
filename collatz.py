def collatz(number):
    if number % 2 == 0:
        print(f"{number} is an even number")
        print(f"{number} // 2 =", number // 2)
        return number // 2
    else:
        print(f"{number} is an odd number")
        print(f"3 * {number} + 1 = ", 3 * number + 1)
        return 3 * number + 1


print("Attempt 1, using the number 20:")
collatz(20)

print("\nAttempt 1, using the number 13:")
collatz(13)

print("\nAttempt 1, using the number 345:")
collatz(345)
