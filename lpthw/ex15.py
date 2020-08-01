#From the system import the argument variable
from sys import argv
#run the script (the file with the program) and open the filename given in the argument
script, filename = argv
#The text you will open is the (filename) given in the command line
txt = open(filename)
#Print the message "Here's your file add the (filename) selected"
print(f"Here's your file {filename}:")
#print the filename provided
print(txt.read())
#print the message "Type filename again:"
print("Type filename again:")
#ask fo user input to reopen the file
file_again = input("> ")
#open the file provided by the user input (file_again)
txt_again = open(file_again)
#open the text information again
print(txt_again.read())