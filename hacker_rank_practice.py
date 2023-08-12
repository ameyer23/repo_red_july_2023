'''
Consider a list (list = []). You can perform the following commands:

insert i e: Insert integer  at position .
print: Print the list.
remove e: Delete the first occurrence of integer .
append e: Insert integer  at the end of the list.
sort: Sort the list.
pop: Pop the last element from the list.
reverse: Reverse the list.

Initialize your list and read in the value of  followed by  lines of 
commands where each command will be of the  types listed above. Iterate 
through each command in order and 
perform the corresponding operation on your list.
'''

lst = []
n = int(input()) #number of commands to run 

#cmd is the input string 'append 2 0' for ex
for i in range(n):
    cmd = input().split() #insert 10 5 as a string, split into list ['insert', 10,5]
    if cmd[0] == 'insert':
        lst.insert(int(cmd[1]), int(cmd[2])) #since insert was index 0, insert 10 at 5
    elif cmd[0] == 'print':
        print(lst)
    elif cmd[0] == 'remove':
        lst.remove(int(cmd[1]))
    elif cmd[0] == 'append':
        lst.append(int(cmd[1]))
    elif cmd[0] == 'sort':
        lst.sort()
    elif cmd[0] == 'pop':
        lst.pop()
    elif cmd[0] == 'reverse': 
        lst.reverse()
        
    
# Take input from the user to determine the range
n = int(input())

# Loop through numbers from 0 to n-1 and calculate their squares
for i in range(n):
    print(i**2)  # Print the square of the current number
    
#takes a string, separates it, and return it with hyphes as delimeters
line = input()
def split_and_join(line):
    string = line.split(' ')
    return '-'.join(string) #if i stop here, we will not printed output
#split_and_join(line)