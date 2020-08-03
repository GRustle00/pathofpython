#call defined function cheese_and_crackers where the argumens are cheese_count, boxes_of_crackers
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print(f"You have {cheese_count} cheeses!")
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    print("Man that's enough for a party!")
    print("Get a blanket.\n")

#print message below, call function cheese_and_crackers directly adding (20, 30) as the values
print("We can just give the function numbers directly:")
cheese_and_crackers(20, 30)
#print message below, setting variables to then call it on the defined function
print("OR, we can use variables from our script:")
amount_of_cheese = 10
amount_of_crackers = 50
#calling the defined function using the variables set previously on line 13 an 14 (amount_of_cheese, amount_of_crackers)
cheese_and_crackers(amount_of_cheese, amount_of_crackers)


#print message below, call defined function directly setting the value as a sum
print("We can even do math inside this too:")
cheese_and_crackers(10 + 20, 5 + 6)

#print message bewlo, calling defined function using a sum with the values set in the variables in line 13 and 14 and provided numbers.
print("And we can combine the two, variables and math:")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)