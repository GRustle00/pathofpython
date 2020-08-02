from sys import argv
script, filename = argv

print(f"We're going to write {filename} this document be advised this will overwrite the file.")

print("Opening the file...")
target = open(filename, 'w')

print("Now I'm going to ask you for three lines.")

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I'm going to write these to the file.")

target.write("{}\n{}\n{}".format(line1,line2,line3))

print("And finally, we close it.")
target.close()