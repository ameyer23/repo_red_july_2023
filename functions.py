#Example 1: simple funciton
def greet():
    print('Hello, engineer!')
greet() #to invoke/call the fn

#Example 2: function with parameters: find avg from numbers in a list
#ORIGINAL CODE BELOW
input_numbers = [5.0, 3.5, 7.8, 9.9, 10.0]

summation = 0 #acts as counter for the for loop
for number in input_numbers:
    summation += number
average = summation / len(input_numbers)

print(average)


#CODE NOW WITHIN A FUNCTION: added def and indented the rest of the code
#input_numbers is our parameter
#input_numbers = [5.0, 3.5, 7.8, 9.9, 10.0] but we will only use the values to call the fn
#parameters are never originally assigned values, so we use value themselves to call the fn
def get_average(input_numbers):
    summation = 0 #acts as counter for the for loop
    for number in input_numbers:
        summation += number
    average = summation / len(input_numbers)

    print(average) #list is an arg
get_average([5.0, 3.5, 7.8, 9.9, 10.0]) #call/invoke fn to assign value to param, the list

'''
Functions with Parameters
'''
#takeaway 1: when you invoke an fn, you must provide all its arguments 
#takeaway 2: be sure to pass in the correct parameters to the function

#Example 3: function with two paramaters
#this fn will take a string and a letter and counts how many times it appears in string
#text and letter are the paramaters
#when you invoke the fn in the code, you must include the 2 params

def print_letter_count(text, letter):
    counter = 0
    for char in text:
        if char == letter:
            counter += 1
    print('Number of', letter, 'is', counter)
print_letter_count('Andrea', 'e')
    
#using same function but make one param longer
#counting how many times letter a appears in a sentence
#here, the order or args is important 
print_letter_count('People say nothing is impossible, but I do nothing every day', 'a')

#give sentence before the letter or it wont work
#since order of args matters here, they are POSITIONAL args
#here, positional values are assigned to paramaters based on their posistion
print_letter_count('a', 'andrea')

#the opposite is a KEYWORD/NAMED arg
#swapping will still read to correct output 
print_letter_count(text = 'Welcome', letter = 'e')
print_letter_count(letter = 'e', text = 'Welcome')


'''
Default Parameter Values 

Previously mentioned:
1. sep and end parameters are keyword args, used at the end of fn/invokation
after all positional args
2. keyword args are optional and have a default value
3. keyword args should appear at the end or there is an error
4. positional args go first, are necessary

'''

#Example 1: sep, and
#default of end is a newline character
#default of sep is a whitespace space char

print('Hello', 'How are you?', end='.', sep='-')

#Example 2: how keyword args work when you create your own fns
#we will use previous fn that found number of times char was in a string
#say we are mainly couting as, we can give the param letter a default val
#can invoke the fn with only one val, the string to pass into it
def print_letter_count(text, letter='a'):
    counter = 0
    for char in text:
        if char == letter:
            counter += 1
    print('Number of', letter, 'is', counter)
print_letter_count('andrea')

#Example 3: same code as before but we set the string AND the letter defauls
#now you can invoke the fn with NO args since params have default vals
def print_letter_count(text='andrea is all the awesome sauce', letter='a'):
    counter = 0
    for char in text:
        if char == letter:
            counter += 1
    print('Number of', letter, 'is', counter)
print_letter_count()

'''
Name Scopes

1. the scope of a name is the part of the code where the name is properly recognized
2. Can we define the variable outside the fn definition before fn call? YES. Variables 
that exist outside of the fn call hava scope outside the fns body, so fns can see them
and use them

'''

#Example: defining the variable inside the fn
def show_truth():
        mysterious_var = 'Surprise'
        print(mysterious_var)
show_truth()

#Example 1. like point 2 above. Define var outside the fn
def show_truth():
    print(mysterious_var)

mysterious_var = 'Surprise'
show_truth()

#Example 2: printing before and after fn call, and inside the fn, change the value of 
#mysterious_var
#known as SHADOWING: the variable and the fn printed out 2 diff things
#local var shadows the global var
def show_truth():
    mysterious_var = 'New surprise'   #LOCAL variable
    print(mysterious_var)

mysterious_var = 'Surprise' #GLOBAL variable, avail before and after fn call
print(mysterious_var) #prints var outside of fn
show_truth() #prints var inside of fn
print(mysterious_var) #prints var outside of fn

#Example 3: modify global var within fn, use global keyword
def show_truth():
    global  mysterious_var #this means dont use shadowing for the var, changes glo var out of fn
    mysterious_var = 'New surprise'
    print(mysterious_var)

mysterious_var = 'Surprise'
print(mysterious_var) #prints surprise
show_truth() #prints new surprise
print(mysterious_var) #prints new surprise

#Example 4: shadowing inside fn body when working with lists
#if you assign a new list to the same var in a fn, shadowing works fine
def show_truth():
    mysterious_var = ['New surprise'] #local var
    print(mysterious_var)

mysterious_var = ['Surprise'] #you need the brackets here to 
print(mysterious_var)
show_truth()
print(mysterious_var)

#Example 5: notice this is appending but we have no equals operator
#we never created a local variable
#if you change list using a method using square brakcets, the ilst outside will reflect the change
def show_truth():
    mysterious_var.append('New surprise') #list method
    print(mysterious_var)

mysterious_var = ['Surprise'] #this IS the original list
print(mysterious_var)
show_truth() #takes og list and appends new surpise
print(mysterious_var)



'''
The None Value

-None is returned by fns that don't return anything meaningful'''

#Example 1
def greet():
    print('hello')

x = greet()
print(x)



'''
Return Keyword

1. returns meaningful values
2. immediately exits the fn, so nothing after it runs
'''

#Example 1
def get_average(input_numbers):
    sum = 0.0
    for number in input_numbers:
        sum += number
    average = sum / len (input_numbers)
    return average #this would return nothing tho it does have a meaningful val
    print('ok') #would not print

print('average is: ', get_average([5.0, 3.5, 7.8, 9.9, 10.0]))

#Example 2: checks wheteher first and last elem of list are equal
def is_first_last_equal(number_list): 
    if number_list[0] == number_list[-1]:
        return True
    else:
        return False

print(is_first_last_equal([2, 3]))

#Example 3: same as ex 2 but we changed the code to include option of empty list
def is_first_last_equal(number_list): 
    if len(number_list) == 0: #if the list is empty, return will exit program and return none
        return
    if number_list[0] == number_list[-1]:
        return True
    else:
        return False

print(is_first_last_equal([]))



'''
PRACTICE PROBLEM: Get Rid of Duplicates!
Write a function named unique. The function should accept one parameter, 
which is a list with any number of elements inside. The default value for 
the parameter should be an empty list ([]).

The function should return a new list with all duplicate elements removed. 
The function should preserve the original order of elements.

Example 1: for unique([1, 1, 4, 5, 1]), the output should be [1, 4, 5]
Example 2: for unique(['Mark', 'Mark', 'John', 'Anne']), the output should be  
['Mark', 'John', 'Anne']
'''
def unique(input_list=[]):
  to_return = []
  for el in input_list:
    if el not in to_return:
      to_return.append(el)
  return to_return
  
  
