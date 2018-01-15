
# spam = {'name': 'alex', 'age': 32}
# spam.setdefault('colour', 'black')
# print(spam)
# # {colour : black}

# spam.setdefault('colour', 'white')
# print(spam)
# # {colour : black}

# # Cannot modify dictionaries

import pprint 

message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
count= {}

for character in message:
    count.setdefault(character, 0)
    count[character] = count[character] + 1

pprint.pprint(count)

# print(pprint.pformat(count))

# line 16 : Works through each character of the string.
# line 17 : empty list - setdefault checks whether a key exists (a key here is each letter) and assigns the letter 0
# W = 0, o = 0, etc 
# line 18 : If the list value exists, add 1?

