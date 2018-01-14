
# a dictionary uses {}
# unlike lists, dictionaries can use data types other than integers as indexes
# indexes for dictionaries are called keys
# a key and its associated value is called a key-value pair

myCat = {'size':'fat', 'colour':'white', 'disposition':'bossy'}
print(myCat['size']) # fat
print('My cat has ' + myCat['colour'] + ' fur') # white

# dictionaries are unordered

spam = ['cats', 'dogs', 'moose']
bacon = ['moose', 'dogs', 'cats']
print(spam == bacon) # False

eggs = {'name': 'Alex', 'species': 'cat', 'age': '32'}
ham = {'age': '32', 'name': 'Alex', 'species': 'cat'}
print(eggs == ham) # True

# The returned values cannot be modified. Cannot use append or remove here

spam = {'colour': 'red', 'age': '42'}
for v in spam.values():
    print(v)

# returned
# 42
# Values is a METHOD

for k in spam.keys():
    print(k)

# colour
# age

for i in spam.items():
    print(i)

# (colour: red)
# (age: 42)


for k, v in spam.items():
    print('Key: ' + k + 'Value: ' + str(v)) # WHY DOES THIS NEED TO BE A STRING?

# THESE ARE TUPLES!

# If you want to make this a list, need to covert it

notATuple = list(spam.keys())
print(notATuple)

# ['colour', 'age']

spam = {'name': 'Zophie', 'age': '7'}
print('name' in spam.keys())
# True 
