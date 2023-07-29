#order of operations
# 1. **
#2. * / // %
#3. + -
# can also use partenthesis 
print((2+3) * 2)

#the precision of floats is limited

#start from the right, right-bound 
print(2 ** 2 ** 3)

#len fn shows length of strings
print(len('Hello'))

#keyword arguments can be used at the end of a funciton after all other arguments, are optional
#see two pieces of code below. Notice second block is amost identical to first but includes 
#keyword arg end=
#note that default value of end arugment is a newline character. We also specified the .
print('Hello, world!')
print('Python speaking!')

print('Hello, world!', end='.')
print('Python speaking!')

#another keyword arguemnt is sep, which acts as a serparator

first_name = 'Andrea'
print('Your name is', first_name, 'Welcome!')

first_name = 'Andrea'
print('Your name is', first_name, 'Welcome!', sep='-')


#bits

#1 kB = 1000 bytes = 8000 bits
#1 MB = 1,000,000 bytes = 8,000,000 bits

#bit-wise operators are not used much

#some bit logic, this is AND logic
#you only see 1 when both of the bits are 1
#if both bits are diff, reflect the first bit
first_bit = 1
second_bit = 0
print(first_bit & second_bit)

#OR logic
#defaults to 1 if bits are diff
first_bit = 1
second_bit = 0
print(first_bit | second_bit)

#exclusive OR logic (XOR)
#when one of the is 0, the result is 1
#when both are 0, results is 0
first_bit = 1
second_bit = 0
print(first_bit ^ second_bit)

#logical negation
# ~x = -x -1
print(~1)
