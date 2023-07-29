
conditional statements, we used age of 35. 
user_age = int(input('What is your age? '))
if user_age > 30:
    print('Your are over 30 years old')
    print('Sorry, you do not qualify!')
    
#notice that print statement outside of if block will be printed no matter what
user_age = int(input('What is your age? '))
if user_age > 30:
    print('Your are over 30 years old')
print('Sorry, you do not qualify!')

#else block is used if the condition is not met
user_age = int(input('What is your age? '))
if user_age > 30:
    print('Your are over 30 years old')
    print('Sorry, you do not qualify!')
else: 
    print('You are 30 years old or younger')
    print('Congratulations, you qualify!')
    

#you can ddd another condition using elif (else-f)
#note that we used == and not =
# = is used to assign values to variables
#you can have more than one elif statement 

user_age = int(input('What is your age? '))
if user_age > 30:
    print('Your are over 30 years old')
    print('Sorry, you do not qualify!')
elif user_age == 30: 
    print('You are exactly 30 years old')
    print('You will need to meet additional conditions to qualify.')
else: 
    print('You are 30 years old or younger')
    print('Congratulations, you qualify!')
    
# != is not equal to
password = input('Do you know the correct password? ')
if password != '--secret':
    print('not correct')
else: 
    print('correct password')

#booleans are either True of False
if True:
    print('Condition is met')

#Boolean Operators
#if, and, not

#and
user_age = int(input('What is your age? '))
user_country = input('What is your country? ')

if user_age < 25 and user_country == 'Germany':
    print('You can apply for a German student exchange program')
else:
    print('Sorry, you do not qualify.')
    
#or
user_country = input('What is your country? ')

if user_country == 'Sweden' or user_country == 'Denmark' or user_country == 'Norway':
    print('You can apply for a Scandinavian student exchange program')
else:
    print('Sorry, you do not qualify.')

#order of operations in boolean login
#1. not
#2. and
#3. or

#joining all 3 operators
user_age = int(input('What is your age? '))
user_country = input('What is your country? ')

if not user_country == 'Germany' and user_age < 25 or user_country == 'Germany' and user_age < 23:
    print('You qualify!')
else:
    print('Sorry, you don\'t qualify.')
    
#same as above but with parenthesis to improve readabililty
user_age = int(input('What is your age? '))
user_country = input('What is your country? ')

if ((not user_country == 'Germany') and user_age < 25) or \
(user_country == 'Germany' and user_age < 23):
    print('You qualify!')
else:
    print('Sorry, you don\'t qualify.')

    
 #Nested If statements
answer_a = input('DO you like traveling? y/n: ')

if answer_a == 'y':
    answer_b = input('And do you like Asia? ')
    if answer_b == 'y':
        print('Excellent, you can go to China!')
    else:
         print('Sorry to hear that.')
else:
    print('Sorry to hear that.')
    
    
