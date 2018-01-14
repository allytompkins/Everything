birthdays = {'Alice': 'April 1', 'Bob': 'December 12', 'Carol': 'March 4'}

while True:
    print('Enter a date: (blank to quit)')
    bday = input()
    if bday == '':
        break

    if bday in birthdays.values():
        print(bday + ' is the birthday of ' + list(birthdays.keys())[list(birthdays.values()).index(bday)])
    else:
        print('I do not have birthday information for ' + bday)
        print('Who has a birthday on that date?')
        name = input()
        birthdays[name] = bday
        print('Birthday database updated')
# all data you enter in this program is forgotten when the program terminates


# line 10 - list(birthdays.keys()) - is making a list of the keys # [Alice, etc]
# line 10 - [list(birthdays.values()).index(bday)] - As a seperate list taking the birthdates and looking for the index
# Then combined, looking for that index in the keys for example: 
# list(birthdays.keys())[0])