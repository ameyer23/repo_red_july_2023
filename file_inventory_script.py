import os
directory = os.getcwd()
#print(directories) #to check that we got cwd

file_details = []

def file_details_fn(): #wrapping it all in a function, indent code after function
    for file in os.listdir(directory):
        file_size = os.path.getsize(file)
        mod_time = os.path.getmtime(file)
        creation_time = os.path.getctime(file)
        file_path = os.path.realpath(file)
        file_details.append({'name': file, 'size': file_size, 'mod time':mod_time, 'path': file_path})

    for details in file_details:
        print("File Details:")
        for key, value in details.items():
            print(f"{key}: {value}")
        print("\n") 
    
file_details_fn()  #calling the function