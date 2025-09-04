spam = "That is Alice's cat."
print(spam)

# Escape characters
print('\nThat is Alice\'s cat.')
print('Hello there!\nHow are you?\nI\'m fine.\n')

# Raw string
print(r'The file is in C:\Users\Alice\Desktop')

# Multiline string
print('''\nDear Alice,
Eve's cat has been arrested for catnapping, cat burglary, and extortion.''')

""" This is test python program
It is a multiline comment
Written by Trupti """

# String indexing and slicing
greeting = 'Hello, World!'
print(greeting[7:-1])

# in and not in operators
print('\nHello' in 'Hello, World!')
print('Hello' not in 'Hello, World!')

# F strings
print('\n----------F Strings----------')
name = 'Alice'
age = 30
print(f'{name} is {age} years old.')
print(f'{{name}} will be {age + 1} next year.')

# %s and format() method
print('\n----------%s and format() method----------')
print('%s is %s years old.' % (name, age))
print('{} is {} years old.'.format(name, age))
print('{1} is {0} years old.'.format(age, name))

# String methods
print('\n----------String methods----------')
print(greeting.lower())
print(greeting.upper())
print('hello'.isupper())
print('hello'.isalpha())
print('hello123'.isalnum())
print('123'.isdecimal())
print('      '.isspace())
print('Hello, World!'.startswith('Hello'))
print('Hello, World!'.endswith('World!'))

# Joining and splitting strings
print('\n----------Joining and splitting strings----------')
print(', '.join(['Alice', 'Bob', 'Charlie']))
print('Alice, Bob, Charlie'.split(', '))

# Justifying and centering strings
print('\n----------Justifying and centering strings----------')
print('Hello'.rjust(10))
print('Hello'.ljust(10))
print('Hello'.center(10))
print('Hello'.center(30, '='))

# Stripping whitespace
print('\n----------Stripping whitespace----------')
print('   Hello   '.strip())
print('   Hello   '.rstrip())
print('SpamSpamBaconSpamEggsSpam'.strip('Spam'))

# Numeric code points of characters
print('\n----------Numeric code points of characters----------')
print(ord('A'))
print(chr(65))
print('Hello'.encode('utf-8'))
print(b'Hello'.decode('utf-8'))

# copying and pasting strings
print('\n----------Copying and pasting strings----------')

import pyperclip
pyperclip.copy('Hello, World!') # or just copy any string to clipboard
print(pyperclip.paste())

# Practice Program: Table printer
print('\n----------Practice Program: Table printer----------')

tableData = [['apples', 'oranges', 'cherries', 'banana'],['Alice', 'Bob', 'Carol', 'David'],['dogs', 'cats', 'moose', 'goose']]

def printTable(table):
    rows = len(tableData[0])
    cols = len(tableData)

    for i in range(rows):
        for j in range(cols):
            if j == 0:
                print('| ', end='')
            print(tableData[j][i].center(10), end=' |')
        print()

printTable(tableData)