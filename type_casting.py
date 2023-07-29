#All converting between data types

#type casting can happen within single lines of code, for better readability 
#float converts intergers to decimals
height_cm = float(input('Height converter: enter your height in cm: '))
print('Your height in feet is ', height_cm / 30.48)

#int coverts floats to intergers
#especially useful when trying to covert number strings to ints for calculations
year_born = int(input('What year were you born?'))
print('In 2100, you will be', 2100-year_born, 'years old, provided you live this long.')

#str() converts the above to strings
#helpgul when incuding results of a calculation in a string
temp_c = input('Enter the temperature today in Cesius degrees: ')
temp_f = float(temp_c) * 1.8 + 32
temp_statement = str(temp_c) + ' degrees Celsius equals ' + str(temp_f) + ' degrees Farenheit'
print(temp_statement)

#test