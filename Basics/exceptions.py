def box_print(symbol, width, height):
    if len(symbol) != 1:
        raise Exception("Symbol must be a single character string")
    if width <= 2:
        raise Exception("Width must be greater that 2")
    if height <= 2:
        raise Exception("height must be greater than 2")
    
    print(symbol * width)
    for i in range(height - 2):
        print(symbol + (' ' * (width - 2)) + symbol)
    print(symbol * width)

try:
    box_print('*', 4, 4)
    box_print('O', 20, 5)
    box_print('x', 1, 3)
    box_print('ZZ', 3, 3)
except Exception as err:
    print("An exception happend: " + str(err))

# Assertion
ages =  [26, 56, 92, 16, 22, 18, 80, 47, 73]
ages.sort() # use reverse() for statement to be false
assert ages[0] <= ages[-1]

# logggin
import logging
logging.basicConfig(filename='myProgramLog.txt', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logging.disable() # stops logging
logging.debug('Start the program')

def factorial(n):
    logging.debug('Start of factorial(' + str(n) + ')')
    total = 1
    for i in range(1, n + 1):
        total *= i
        logging.debug('i is ' + str(i) + ', total is ' + str(total))
    logging.debug('End of factorial(' + str(n) + ')')
    return total

print(factorial(5))
logging.debug('End of program')