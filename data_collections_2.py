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