from sys import argv #from the system improt argument vector

script, input_file = argv #script and input_file are equal to the argument vector

def print_all(f): #define function 'print_all'
    print(f.read()) # execture read following argument

def rewind(f): #define the rewind function for the argument provided
    f.seek(0) # call seek function on absolute file positioning (begining of file)

def print_a_line(line_count, f): # define function 'print_a_line' with arguments provided (line_count, f)
    print(line_count, f.readline()) #Execute In 'line_count' read following argument/file

current_file = open(input_file) #Store variable as 'current_file' to open file provided by argument vector

print("First let's print the whole file:\n") #Print following message

print_all(current_file) #Execute defined function 'print_all' utilizing stored variable 'current_file'

print("Now let's rewind, kind of like a tape.") #print following message

rewind(current_file) #execute defined function 'rewind' utilizing stored variable 'current_file'

print("Let's print three lines:") # print following message

current_line = 1 #store variable 'current_line' as 1
print_a_line(current_line, current_file) #execute defined function 'print_a_line' counting a first line

current_line += 1 #set stored variable into new 'current_line' which should be  1 + 1
print_a_line(current_line, current_file) #execute defined function 'print_a_line' counting a second line

current_line += 1 #set stored variable into new 'current_line' which should be 2 + 1
print_a_line(current_line, current_file) #execture defined function 'print_a_line' counting a third line