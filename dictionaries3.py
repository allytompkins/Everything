spam = {'name': 'Zophie', 'age':7}
print('Zophie' in spam.keys()) # False

spam = {'name': 'Zophie', 'age':7}
print('Zophie' in spam) # False

# Only searches in the keys by default

spam = {'name': 'Zophie', 'age':7}
print('Zophie' in spam.values()) # True


print(spam.keys())

print(spam)
print(spam.values())
print(spam.items())