empty_tuple = ()
one_el_tuple_a = (1,)
one_el_tuple_b = 1, 

three_el_tuple = 1, 2, 3 
print(three_el_tuple)



'''
Mutable data can be changed. This includes lists

Unmutable data: cannot be changed. This includes tuples. For Example, you can't add new elements
to a tuple like you would a list using append. 

To change a tuple. you'd have to assign a new variable to the old tuple

NOTE: strings also are unmutable.
'''
user_data = ('John', 'American', 1964)



'''
Tuple Operations
'''
#Example 1: len operation
user_data = ('John', 'American', 1964)
print(len(user_data))

#Example 2: len 
user_data = ('John', 'American', 1964)
if 'American' in user_data:
    print('This person comes form the US')
    
#Exmaple 3: iterate a tuple with a for loop
user_data = ('John', 'American', 1964)
for element in user_data:
    print(element)

#Exmaple 4: Like lists, tuples can be added or multiplied together
user_data = ('John', 'American', 1964) + ('teacher', 'male')
print(user_data)

#Example 5: 
numbers = (0,1) *10
print(numbers)


'''
When to use lists or tuples?

1. lists are usually when you want values of the same data type
2. tuples are usually used when you have values of different type but are somehow related
'''

#Example 6
first = 5
second = 7
first, second = second, first #this is a tuple


'''
Tuples in lists, lists in tuples
'''
#Example 1: Tuples in lists
city_1 = ('London', 'UK', 8.98)
city_2 = ('Canberra', 'Australia', 0.4)
city_3 = ('Algiers', 'Algeria', 3.9)

#create a list with all this similar info
capitals = [('London', 'UK', 8.98), ('Canberra', 'Australia', 0.4),('Algiers', 'Algeria', 3.9)]
print(capitals)

#Example 2
for capital in capitals:
    print('Name:', capital[0], ', Country:', capital[1], ', Population:', capital[2])

#list of John's weight changes
#though you cannot change the tuple, you CAN add elements to the list within the tuple
user_data = ('John', 'American', 1964, [77.0, 78.2, 77.5])
user_data[3]
user_data[3].append(79.6)
print(user_data)




'''
PRACTICE PROBLEM
All Roads Lead to Rome
You are given a list with various flight connections in Europe. Each connection is 
represented as a tuple with the following elements:

(city_from, city_to, time)

For example, the following tuple represents a flight from Amsterdam to Dublin which 
takes 100 minutes:

('Amsterdam', 'Dublin', 100)

Your task is to go through all the routes in a loop and check how many of them lead 
to Rome (i.e. how many of them have city_to equal to 'Rome'). Among the routes to Rome, 
you should also calculate the average flight time. Print the following the output:

{} connections lead to Rome with an average flight time of {} minutes

Replace {} with the number of connections and the average flight time.


'''
connections = [
    ('Amsterdam', 'Dublin', 100),
    ('Amsterdam', 'Rome', 140),
    ('Rome', 'Warsaw', 130),
    ('Minsk', 'Prague', 95),
    ('Stockholm', 'Rome', 190),
    ('Copenhagen', 'Paris', 120),
    ('Madrid', 'Rome', 135),
    ('Lisbon', 'Rome', 170),
    ('Dublin', 'Rome', 170)
    ]
 
counter = 0
sum = 0.0
 
for route in connections:
    if route[1] == 'Rome':
        counter += 1
        sum += route[2]
 
print(counter, 'connections lead to Rome with an average flight time of', sum/counter, 'minutes')
        
#Takeaway: for loops, use a counter to keep track of iterations, use indexing with control variable 



'''
Dictionaries

-dicts are mutable
-access values by indexing using keys
-you cannot get keys from values
-keys can be of any other immutable datatype, not lists tho-since they are mutable
-values, on the other hand, CAN be of a mutable type 

'''

emails = {
        'Anne Stahl': 'astall@gmail.com',
        'Andrea Meyer': 'ameyer@gmail.com',
        'Oliver Meyer': 'omeyer@gmail.com'
}

print(emails['Oliver Meyer'])


'''
Dictionary operations
'''
#Example 1: Adding new elements to lists
grades = {}
grades['John'] = 'A-'
grades['Anne'] = 'B'
print(grades)

#Example 2: another way to update the dict
grades.update({'John':'A'})
print(grades)

#Exmaple 3: check number of key-value pairs in a dict use len
print(len(grades))

#Example 4: print grades for john
if 'John' in grades:
    print('John got:', grades['John'])

#Example 5: To delete a key and its value
del grades['John']
print(grades)

#Example 6: iterate through a dict, for loop to access keys
#dicts are now ordered by default
grades = {}
grades['John'] = 'A-'
grades['Anne'] = 'B'

for element in grades:
    print(element)
    
#Example 7: iterate through a dict, for loop to access keys using KEYS METHOD-like above
for element in grades.keys():
    print(element)
    
#Example 8: print only values using values method
for element in grades.values():
    print(element)
    
#Example 9: to access keys and values using items method
for person, grade in grades.items():
    print(person, 'got an', grade)


'''
PRACTICE PROBLEM: Interactive Dictionary

Write a program that implements a simple interactive dictionary. 
Start by prompting the user with the following:

Enter a word in English or EXIT: << put a space at the end of this message

When the user enters EXIT in capital letters, terminate the program with the following:

Bye!

Otherwise, try to find the German equivalent in the dictionary provided in the exercise.

a. if the word is in the dictionary, print: Translation: {} << replace {} with the word 
from the dictionary
b. if the word is not in the dictionary, print: No match!

You should keep asking the user for new words with the same prompt ('Enter a word in 
English or EXIT: ') until the user provides EXIT.

Here's an example of how the program could work with user input shown in the bold:

Enter a word in English or EXIT: dog
No match!
Enter a word in English or EXIT: face
Translation: Gesicht
Enter a word in English or EXIT: EXIT
Bye!

'''
sample_dict = {
    "mouth": "Mund",
    "finger": "Finger",
    "leg": "Bein",
    "hand": "Hand",
    "face": "Gesicht",
    "nose": "Nase"
}
 
while True: #infinite loop, hence the break
    user_input = input('Enter a word in English or EXIT: ')
    if user_input == 'EXIT':
        break
    if user_input in sample_dict:
        print ('Translation:', sample_dict[user_input])
    else:
        print('No match!')
 
print('Bye!')


#dicts and lists
print('awesomeeeeee')