print("hello", end=" ")
print("world!")

print('cats', 'dogs', 'mice', sep=", ")

# global variable and local variables

def spam():
    global eggs
    eggs = 'spam'

eggs = 'global'
spam()
print(eggs)

def func():
    print(name)
    # name = "Shweta" # Error! sameNameError

name = "Trupti"
func()

# Exception handling

def divide(divide_by):
    try:
        return 42 / divide_by
    except:
        print("Error: Invalid argument")

print(divide(2))
print(divide(0))
print(divide(12))

# print a pattern

n = int(input("Enter no. of stars > "))

def pattern(n):

    if n % 2 != 0:
        n = n - 1
    spaces = n // 2
    incre = False

    for i in range (0, n+1):
        print(" " * spaces , end="")
        for i in range (0, n-1):
            print("*", end="")
        print("*")
        if spaces == 0:
            incre = True
        if incre:
            spaces += 1
        else: 
            spaces -= 1

pattern(n)

# importing
import spam

spam.bacon()