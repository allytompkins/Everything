
spam = {'george':16,'amber':18} # Note that the values are integers. User input is a string
search_age = int(input("Provide age"))
for name, age in list(spam.items()):
    if age == search_age:
        print (name)

# This is not ideal as the code is looping through every item and only stopping when it finds the right key