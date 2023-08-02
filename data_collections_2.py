'''Changing Element Positions

swapping values usually requires a third variable, so no values are lost
'''

first = input('Enter first number: ')
second = input('Enter second number: ')
print('Before swapping:', first, second)
temporary = first
first = second
second = temporary
print('After swapping:', first, second)

#python has a nicer shortcut to do this
#this requires only one line to swap variables
#same logic can be used with list elements
first = input('Enter first number: ')
second = input('Enter second number: ')
print('Before swapping:', first, second)
first, second = second, first
print('After swapping:', first, second)


#Example 1: swapping first and last elements
top_cities = ['New York City', 'Los Angeles', 'Chicago', 'Houston','Phoenix']
top_cities[0], top_cities[4] = top_cities[4], top_cities[0]
print(top_cities)

#Example 2: using sort for alpha order
#sort is a list METHOD
#this cannot be undone, so changes original list
#AKA sorting in places
top_cities = ['New York City', 'Los Angeles', 'Chicago', 'Houston','Phoenix']
top_cities.sort()
print(top_cities)

#Example 3: sorting in reverse order with keyword arg reverse
top_cities = ['New York City', 'Los Angeles', 'Chicago', 'Houston','Phoenix']
top_cities.sort(reverse = True)
print(top_cities)

#Example 4: sorting using sort FUNCTION
#this allows us to keep original list as well

top_cities = ['New York City', 'Los Angeles', 'Chicago', 'Houston','Phoenix']
print(sorted(top_cities))
print(top_cities)




'''
Checking Element Presence
'''

#Example 1
for char in 'happy message':
    print(char)

#Example 2: Checking if guest name is on the list
invited_guests = ['Kate', 'Adam', 'Kerry', 'Joe', 'Anne', 'Marie']
name = input('what is your name?')
if name in invited_guests:
    print('Welcome!')
else:
    print('You are not invited.')


#Example 3: Checking if guest name is NOT on the list
invited_guests = ['Kate', 'Adam', 'Kerry', 'Joe', 'Anne', 'Marie']
name = input('what is your name? ')
if name not in invited_guests:
    print('You are not invited.')
else:
    print('Welcome')
    



'''
Copying Lists
'''

#Example 1: this was supposed to return the original and new list but didnt 
list_original = [1,2,3]
list_new = list_original
list_original[0] = -5
print('Original:', list_original, '\nNew:', list_new

#Exmaple 2: use slicing to achieve this since lists are referenced to and not directly changed
#we added slicing from the very beginning to the very end of list
list_original = [1,2,3]
list_new = list_original[:] 
list_original[0] = -5
print('Original:', list_original, '\nNew:', list_new)

#Example 3: copy selected fragment of list, first 2 elements of list
list_original = [1,2,3]
list_new = list_original[:2]
list_original[0] = -5
print('Original:', list_original, '\nNew:', list_new)





'''
List Comprehensions

Allows us to speed up list creation
It;s an actual list created on the fly
'''

#Example 1: creating long list of numbers using a loop
#does the trick but takes up lots of space
numbers = []
for i in range(0,101):
    numbers.append(i)
print(numbers)

#Example 2: simplified and faster version of ex 1
numbers = [i for i in range(0,101)]
print(numbers)

#Example 3: another list comprehension example
#create list of numbers 1-100 but skip numbers that are divisble by 3

numbers = [i for i in range(0,101) if i % 3 != 0]
print(numbers)




'''
Nested Lists

**convention: lists should contain the same data type
**Nested lists are used frequently to represent multi dimensional objects
'''

#Example 1: accessing specific element of list
#get element 0, position 0
cells = [['A1', 'A2', 'A3'], ['B1', 'B2', 'B3']]
cells[0][0]


#Example 2: use for loop to iterate list and print its elements - x is element
cells = [['A1', 'A2', 'A3'], ['B1', 'B2', 'B3']]
for x in cells:
    print('Element:', x)
    
#Example 3: access individual string elements inside sublists
#use nested for loops
cells = [['A1', 'A2', 'A3'], ['B1', 'B2', 'B3']]
for x in cells:
    for y in x:
        print('Element:', y)
        
#Example 4: nested lists reminds us of tables
table = [['A1', 'A2', 'A3'], ['B1', 'B2', 'B3']]
for row in cells:
    for cell in x:
        print('Element:', cell)


#Example 5: take above and make it resemble a real table
table = [['A1', 'A2', 'A3'], ['B1', 'B2', 'B3']]
for row in cells:
    for cell in row:
        print(cell, '', end='')
    print()
    
#Example 6: Create a list that represents the below table

#1 2 3 4 5 
#1 2 3 4 5
#1 2 3 4 5
#1 2 3 4 5

table = [[i for i in range(1, 6)] for j in range(4)]
print(table)



'''
Adding and Multiplying Lists
'''

#Example 1: adding lists using +
list_us = ['New York City', 'Chicago']
list_uk = ['Londong', 'Bristol']
list_all = list_us + list_uk
print(list_all)

#Example 2: mutiplying lists
list_numbers = [0,1] * 10
print(list_numbers)

print('we are all done with this part.')



