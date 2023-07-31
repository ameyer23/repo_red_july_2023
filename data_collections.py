'''
We will cover complex data types

Basic data types can only store one value at a time inside of them.

Complex data types include: tuples, dictionaries, lists.
AKA Collection data types, container data types.They contain more than value.
'''

###############################################################################

'''
Lists
-store multiple values of the same type
-use [ ], separate values with commas
-elements are indexed, start at 0
'''

top_city = 'New York City'
to_cities = []
top_cities = ['New York City', 'Los Angeles', 'Chicago', 'Houston','Phoenix']
top_cities[0] #this is the first element of the list
top_cities[-5] #fifth element from the end, first element from the left 
top_cities[0:3] #slices list, output does not include index 3
top_cities[0]


'''
Deleting elements from a list
'''

top_cities = ['New York City', 'Los Angeles', 'Singapore', 'Chicago', 'Houston','Phoenix']
del top_cities[2]
print(top_cities)


#lets keep first 3 elements of list and delete remaining 2
top_cities = ['New York City', 'Los Angeles', 'Singapore', 'Chicago', 'Houston','Phoenix']
del top_cities[3:]
print(top_cities)


#delete all elements of the list using a slice with indices ommitted
top_cities = ['New York City', 'Los Angeles', 'Singapore', 'Chicago', 'Houston','Phoenix']
del top_cities[:]
print(top_cities)


#you can use del to delete the list itself
#this returns an error because the variable-list name- doesn't exist anymore
top_cities = ['New York City', 'Los Angeles', 'Singapore', 'Chicago', 'Houston','Phoenix']
del top_cities
print(top_cities)


'''
Adding. new elements to a list

Methods: specific kind of functions. It is owned by the kind of data it works for
So, no data = no function
'''

#append is a method, adds element to the END
#methods are invoked with a . after the data they work on
book_ratings = [7, 9, 5, 6, 8]
book_ratings.append(4)
print(book_ratings)

#adds argument based on index
#add 10 to index 1
book_ratings = [7, 9, 5, 6, 8]
book_ratings.insert(1,10)
print(book_ratings)


'''
Iterating Lists
'''

#Example 1:
#city is our control variable
#here, we cannot get the indexes of elements
top_cities = ['New York City', 'Los Angeles', 'Chicago', 'Houston','Phoenix']
for city in top_cities:
    print('Current city: ', city)


#Example 2: 
#here, we CAN get the indices of elements
#city_index is our control variable

top_cities = ['New York City', 'Los Angeles', 'Chicago', 'Houston','Phoenix']
for city_index in range(len(top_cities)):
    print('Current city: ', city_index, '| Current City', top_cities[city_index], )
    

#Example 3
#sum up all numbers and print out amount of money spent

spendings = [32.45, 18.65, 23.45, 78.32, 5.23]
sum = 0.0

for spending in spendings:
    sum += spending
print('Money spent', sum)

'''
Practice Problem

Helping with the Budget

John has a hard time keeping his budget. Write a program to help him analyse his spendings. You are given a list with John's spendings for each month. Go through the list, and count the number of times...

a. the spendings were low (< 1000.0)
b. the spendings were normal (between 1000.0 and 2500.0 inclusive)
c. the spendings were high (> 2500.0)
Then, print the following to the output:

Numbers of months with low spendings: {}, normal spendings: {}, high spendings: {}.
'''


spendings = [1346.0, 987.50, 1734.40, 2567.0, 3271.45, 2500.0, 2130.0, 2510.30, 2987.34, 3120.50, 4069.78, 1000.0]

low = 0
normal = 0
high = 0
 
for month in spendings:
    if month < 1000.0:
        low += 1
    elif month <= 2500.0:
        normal += 1
    else:
        high += 1
 
print('Numbers of months with low spendings: ' + str(low) + ', normal spendings: ' + str(normal) + ', high spendings: ' + str(high) + '.')



