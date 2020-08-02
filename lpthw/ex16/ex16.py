#request to import information from system based on argument variable given
from sys import argv
#variable set
script, filename = argv
#print messsage below including filename variable in string
print(f"We're going to erase {filename}.")
#print message below
print("If you don't want that, hit CTRL-C(^C).")
#print message below
print("If you do want't that hit, RETURN.")
#print input with question mark
input("?")
#print the message below
print("Opening the file...")
#set filename variable target, open filename and write
target = open(filename, 'w')
#print message below
print("Truncating the file. Goodbye!")
#delete'truncate' target variable
target.truncate()
#print message below
print("Now I'm going to ask you for three lines.")
#set line1 as variable, print message below ask for user input
line1 = input("line 1: ")
#set line2 as variable, print message below ask for user input
line2 = input("line 2: ")
#set line3 as variable, print message below ask for user input
line3 = input("line 3: ")
#print message below
print("I'm going to write these to the file.")
#write information inside 'target' variable
target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")
#print message below
print("And finally, we close it.")
#close 'target' variable
target.close()