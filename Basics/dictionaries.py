birthdays = {'Alice': 'Apr 1', 'Bob': 'Dec 12', 'Carol': 'Mar 4'}

while True:
    print('Enter a name (or blank to exit):')
    name = input()
    if name == '':
        break

    if name in birthdays:
        print(f"{name}'s birthday is {birthdays[name]}")
    else:
        print(f"I don't have birthday information for {name}.")
        print('What is their birthday?')
        bday = input()
        birthdays[name] = bday
        print('Birthday database updated.')

