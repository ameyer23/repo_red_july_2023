'''Foundational
Allow the user to input how many EC2 instances they want names for and output 
the same amount of unique names.

Allow the user to input the name of their department that is used in the unique name.

Generate random characters and numbers that will be included in the unique name.
'''

import random
import string

instance_amount = int(input('Amount of names needed: '))
dept = input('Department name: ')
length = 10

for name in range(instance_amount):
    random_name = ''.join(random.choices(string.ascii_letters + string.digits, k=length))
    print(random_name)
    
###############################################################################

'''
Advanced
The only departments that should use this Name Generator are the Marketing, 
Accounting, and FinOps Departments. List these departments as options and if 
a user puts another department, print a message that they should not use this 
Name Generator. Be sure to account for incorrect upper or lowercase letters in 
the correct department. Example: a user inputs 
accounting vs Accounting.
'''

import random
import string

instance_amount = int(input('Amount of names needed: '))
dept = input('Department name: ')
length = 10

if dept.lower() in ['marketing', 'accounting', 'finops']: #.lower to make sure all inputs are conv. to lowercase
    for name in range(instance_amount):
        random_name = ''.join(random.choices(string.ascii_letters + string.digits, k=length))
        print(random_name)
else: 
    print('Your department is not eligible for name randomization')

###############################################################################

'''
Complex
Turn the above into a Function and execute the Function to verify it works.
'''

import random
import string

#input variables
instance_amount = int(input('Amount of names needed: '))
dept = input('Department name: ')

#define the function: wrap code from Advanced section within a new function
def random_name_generator(instance_amount, dept, length=10):
    if dept.lower() in ['marketing', 'accounting', 'finops']:
        for name in range(instance_amount):
            random_name = ''.join(random.choices(string.ascii_letters + string.digits, k=length))
            print(random_name)
    else: 
        print('Your department is not eligible for name randomization')


#Call the function
random_name_generator(instance_amount, dept)
