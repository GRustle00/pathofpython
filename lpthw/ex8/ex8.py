formatter = '{}, {}, {}, {}' #variable

print(formatter.format(1,2,3,4,)) #print function calling on variable to turn variable 'formatter' into 1,2,3,4
print(formatter.format("one", "two", "three", "four")) #print function to turn variable 'formatter'
print(formatter.format(True, False, False, True)) #print function to turn variable 'formatter' into true or false statements
print(formatter.format(formatter, formatter, formatter, formatter)) #print function to print the formatter variable unto itself
print(formatter.format(
    "/An old silent pond.../",
    "/A frog jumps into the pond/",
    "/Splash! Silence again./",
    "...Matsuo Basho(1644-1694)"
)) #print function to call upon the variable formatter and exchange the brackets into the text mentioned