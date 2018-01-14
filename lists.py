spam = {'age': 32, 'name': 'alex', 'lives': 'west norwood'}

# print(spam) # This prints the whole dictionary {}
# # print(spam.keys) # THIS PRINT THE LOCATION (PRINTING THE FUNCTION NOT THE RETURNED VALUE
# # print(spam.values)
# # print(spam.items)

# print(spam)  # PARANTHESIS NOT NEEDED HERE AS SPAM IS NOT A FUNCTION
# print(spam.keys())
# print(spam.values())
# print(spam.items())


# print(list(spam))
# print(list(spam.keys())) # Same as spam
# print(list(spam.values()))
# print(list(spam.items()))

# keysVar = list(spam)
# print(keysVar)


# print('name' in spam) #True
# print('age'in spam.keys()) #True
# print('west norwood' in spam) #False
# print('west norwood' in spam.values()) # True 

picnicItems = {'apples': 5, 'cups': 2}
print('I am bringing' + str(picnicItems.get('cups', 0)) + ' cups')
print('I am bringing' + str(picnicItems.get('eggs', 0)) + ' eggs')

print('I am bringing' + str(picnicItems['cups']) + ' cups')
# print('I am bringing' + str(picnicItems['eggs']) + ' eggs') # Won't run, as eggs doesnt eixst

# STR puts the returned value (2) into a string
# The second example is not great if the key doesnt exist