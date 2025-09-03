import random

spam = ['cat', 'bat', 'rat', 'elephant']

print("Hello, " + spam[0])
print(spam[-1]) # last index

print(spam[0:3]) # slicing
print(spam[:2])
print(spam[1:])
print(spam[:])
print(spam[1:-1])

print(len(spam))

spam[1] = 'bunny'
print(spam)

print(spam + [1, 2, 3])
print(spam * 3)

del spam[2]
print(spam)

# a program with lists
print('\n----------cat names-----------')
cat_names = []
while True:
    print('Enter the name of cat ' + str(len(cat_names) + 1) + ' (Or enter nothing to stop)')
    name = input()
    if name == '':
        break
    cat_names = cat_names + [name]
print('The cat names are:')
for name in cat_names:
    print('  ' + name , end='')

print('\n\n--------in and not in-------')
arr = ['hello', 'hi', 'howdy', 'heyas']
print('cat' in arr)
print('howdy' in arr)
print('cat' not in arr)

print('')
print('---------multiple assingments----')

cat = ['fat', 'gray', 'loud']
size, color, disposition = cat

print(size, color, disposition, sep=', ')

# List enumeration
print('\n------------enumeration--------')
for index, item in enumerate(cat):
    print('Index', str(index), 'in cat is:', item)

print('\n---------random selection------')
print(random.choice(cat))

print('\n-------shuffle---------')
print('cats before', cat)
random.shuffle(cat)
print('cat after', cat)

# methods
print('\n\n-----------methods----------')

chars = ['Arisu', 'Usagi', 'Aan', 'Chishiya', 'koina', 'Aaguni']

print(chars)

print(chars.index('Usagi'))

chars.append('Alice')
print(chars)

chars.insert(2, 'Mira')
print(chars)

chars.remove('Alice')
print(chars)

chars.sort()
print(chars)

chars.reverse()
print(chars)

# short program
print('\n--------Magic 8 Ball--------')

messages = ['It is certain',
            'It is decidedly so',
            'Yes definitely',
            'Reply hazy try again',
            'Ask  again later',
            'Concentrate and ask again',
            'My replay is no',
            'Outlook not so good',
            'Very doubtful']

while True:
    print('Ask a yes or no question: ')
    inp = input('>')
    if inp == '':
        break
    print(random.choice(messages))

# Lists are mutable that is you can change their values

# Tuple : immutable and you write tuple with parenthesis

eggs = ('hello', 43, 0.5)
print(eggs)
# eggs.append('cat') # error!

# copy and deepcopy
import copy
spam = ['A', 'B', 'C']
alpha = spam # copy
cheese = copy.copy(spam) # deepcopy
cheese[1] = 42
print(spam)
print(cheese)
alpha[1] = 56
print('after change alpha spam is :' , spam)