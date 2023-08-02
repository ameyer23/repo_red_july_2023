##while loop
#interger variables are common with while loops
#common rookie mistake: not including increment portion
#without counter, this program would run infinitely
#this is known as "incrementation" - increment by 1

#Example 1
counter = 1
while counter < 11:
    print(counter)
    counter += 1
print('Finished')


#Example 2: here, condition is not satisfied so we exit loop 
counter = 1
while counter > 11:
    print(counter)
    counter += 1
print('Finished')

#Example 3
secret_number = 14
print('''
=======================
===SECRET NUMBER GAME!!
=======================
''')
user_input = int(input('Try to guess the secret number from 0 to 20: '))
while user_input != secret_number:
    print('Wrong!')
    user_input = int(input('Try to guess the secret number from 0 to 20: '))
print('Perfect! You have guessed the secret number!')

############################################################################

'''for Loops
-are used to scan all elements of a specific sequence 
-in these loops, conditions are checked internally 
-after for keyword, we define control variable, here it's "letter"
-control variable can be anything
-python automatically assings letters from string to the variable
-in keyword defines the range of the string
-loop is excited when we reach last element of string
-finite loop, in which we iterate a sequence 
'''

#Example 1
for letter in 'hello':
    print('Current letter:', letter)

#Example 2
#for range fn, default start value is 0 and last value is not included
for counter in range(1,11):
    print(counter)
print('Finished!')

############################################################################

#Break and Continue

'''
Break 
-allows you to leave while loop
-used inside loops with if statements
'''

#Example 1: 
while True:
    name = input('Enter your name or EXIT to close the program: ')
    if (name == 'EXIT'):
        break
    print('Hello', name)
    
'''
Continue
-allows you to exit current interation and continue to the next one
-for when you want to skip a certain iteration
-also commonly used with if statements
'''

#Example 1:
#We want to show all numbers from 1-20, except those 
#that can be divided by 5

for i in range (1,21):
    if i % 5 == 0:
        continue
    print(i)
 
############################################################################

# Other Loop Features

'''
pass
-doesn't do much
-we use it because loop syntax requires at least one instruction inside 
the loop's body - also true for if, elif, else
-if we removed pass from exmaple 1, we would get a syntax error
-good practice to use pass when creating loops and preventing errors
'''

#Example 1: 
for i in range(11):
    pass

#Example 2: Nested Loops
for a in range(1,6):
    for b in range(1,6):
        print(a, 'x', b, '=', a *b)

############################################################################
'''
Loops with Else Statements
-rarely used in practice
'''

#Example 1
#here, loop's condition is never satisfied from the start so
#we only print else instruction
#else branch of a loop is always executed exactly once
#exception: break statement

i = 5
while i < 5:
    print(i)
    i =+ i
else:
    print ('else', i)

#######################################################################

#Python Guessing Game

'''
Ask the user to guess the year when Python 1.0 was released (the correct answer is 1994) with the following prompt:

When was Python 1.0 released? << remember to add a space at the end of this prompt

If the user answers 1994, show:

Correct! and finish the program. 

If the user answers with any year that is later than 1994, show a hint and ask again for a new year on a new line:

It was earlier than that!
When was Python 1.0 released? << remember to add a space

If the user answers with any year that is earlier than 1994, show a hint and ask again for a new year on a new line:

It was later than that!
When was Python 1.0 released? << remember to add a space
'''

while True:
    answer = int(input('When was Python 1.0 released? '))
    if answer > 1994:
        print('It was earlier than that!')
    elif answer < 1994:
        print('It was later than that!')
    else:
        print('Correct!')
        break