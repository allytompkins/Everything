from sys import argv

script, filename = argv

print(f"We're going to erase {filename}.")
print("If you don't want that, hit CTRL-C.")
print("If you do want that hit 'Return'") # Lines 1 to 8 don't do anything

input("?") # There is no variable to capture the input (does it matter what you put here?)

print("Opening the file...")
target = open(filename, 'w') # The W refers to "write mode". 

print("Truncating the file. Goodbye!")
target.truncate() # truncate empties the file

print("Now I'm going to ask you for three lines.")

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I'm going to write these to the file")

# target.write(line1 + "\n" + line 2 + "\n" + line3 + "\n")

target.write(line1) # the "target" variable opens the file, "write" adds text to the file (only text?)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print("And finally, we close it.")
target.close()
