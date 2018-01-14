birthdays = {'Alice': 'April 1', 'Bob': 'December 12', 'Carol': 'March 4'}

while True:
    print('Enter a name: (blank to quit)')
    name = input()
    if name == '':
        break

    if name in birthdays.keys():
        print(birthdays[name] + ' is the birthday of ' + name) # (birthdays[name]) pulls in what is located at name, not the name itself
    else:
        print('I do not have birthday information for ' + name)
        print('When is their birthday?')
        bday = input()
        birthdays[name] = bday
        print('Birthday database updated')

# all data you enter in this program is forgotten when the program terminates
