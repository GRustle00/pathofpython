from sys import argv
script, filename = argv

print("Good morning, which file would you like to open today?")
txtfile = input("> ")

txtfileopen = open(txtfile)

print(txtfileopen.read())