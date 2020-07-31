from sys import argv
pathfile, one, two, three, four = argv

print("Your path file is:", pathfile)
print("Your second variable is:", two)
print("Your thid variable is:", three)
print("Your fourth variable is:", four)

first = input("What was the second variable?")
print(f"Correct ... {first}, Good Job!")
second = input("What was the third variable?")
print(f"Amazing it indeed was {second}")