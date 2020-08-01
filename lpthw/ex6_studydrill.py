#numeric variable to determine the amount of "Type of people"
types_of_people = 10
#variable where you factor the type of people
x = "There are {types_of_people} types of people."
#variable to print determine the word binary
binary = "binary"
#self explanatory
do_not = 5
#variable to store string factors
y = f"Those who know {binary} and those who {do_not}"
#this equals to print(f"There are {types_of_people} types of people")
print(x)
#this equals to print(f"Those who know {binary} and those who {do_not})
print(y)
#pring determine dstring adding variable
print(f"I said: {x}")
print(f"I also said: '{y}'")
#variable containing a statement
hilarious = False
#An alternative way to format the string. It could be useful for some processes
joke_evaluation = "Isn't that joke so funny?! {}"
#this line executes the above statement and adds the condition to the empty bracket which is determined by the format code"
print(joke_evaluation.format(hilarious))
#'w' and 'e' are variables containing strings which will be printed by the print function in line 28
w = "This is the left side of..."
e = "a string with a right side."
 
print(w + e)