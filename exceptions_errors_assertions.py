
'''
Execption Handling

1. we may use try, except

'''

#Example 1: this would raise an exception when we enter something other than an int
#we deal with this using try
try:
    value = int(input('Enter an int:'))
    print('The inverse of', value, 'is', 1/value)
except: 
    print('You did not provide a number so we cant cal inverse')  #exception handling
    

#Example 2: same as above but input is 0, which cannot happen
try:
    value = int(input('Enter an int:'))
    print('The inverse of', value, 'is', 1/value)
except ValueError:  #since input was a letter and not an int
    print('You did not provide a number so we cant calc inverse')  #exception handling
except ZeroDivisionError: #ince dividing ints by 0 yields this error
    print('You provided zero and division by 0 is not possible.')  #exception handling
    

#Example 3: General except block for other errors, no general exception name
try:
    value = int(input('Enter an int:'))
    print('The inverse of', value, 'is', 1/value)
except ValueError:  #since input was a letter and not an int
    print('You did not provide a number so we cant calc inverse')  #exception handling
except ZeroDivisionError: #ince dividing ints by 0 yields this error
    print('You provided zero and division by 0 is not possible.')  #exception handling
except: #general except block
    print('Something strange happened here.')
  
  
    
    
'''
There is one special exception type: SyntaxError. You should pay 
attention to how it works.

If you raise a SyntaxError manually, then you can catch it in 
the except block just fine: see below
'''
try: 
    raise SyntaxError
except:
    print('Got it!')  #SyntaxError caught here

    
'''However, if you make a syntax error in the try block and Python 
automatically raises a SyntaxError for you, then you cannot catch it:
'''
try:
  5:4 # this line generates a SyntaxError
except:
  print('Got it!') # SyntaxError is NOT caught here




'''
Exception hierarchy: these are raised by Python

1. Top is BaseException, not common
2. Below it: Exception, SystemExit, KeyboardInterrupt
3. SystemExit is raised when we call specific method which is used to terminate program. Must
import Sys
4. KeyboardInterrupt: interrupts running code that would run forever, same as stop button
5. 
'''

#Exceptions are propagated through functions in python


'''
Assertions: assumptions in our program that should always be true

1. assertions are for debugging and testing code
2. they are for documenting code
'''

#Example 1:
def calculate_inverse(number):
    assert (number != 0), 'Got 0 as a numner!' #this is the condition, and the error message to show
    return 1/number
calculate_inverse(0) #this is the zero we put in, and returns the error we set