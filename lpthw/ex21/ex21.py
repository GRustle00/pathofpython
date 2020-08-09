def add(a, b):
    print(f"ADDING {a} + {b}")
    return a + b

def substract(a, b):
    print (f"SUBSTRACTING {a} - {b}")
    return a - b

def multiply(a, b):
    print(f"MULTIPLYING {a} * {b}")
    return a * b

def divide(a, b):
    print(f"DIVIDING {a} / {b}")
    return a / b


print("Let's do some math with just functions!")

age = add(30, 5)
height = substract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print(f"Age: {age}, Heights: {height}, weight: {weight}, IQ: {iq}")


# A puzzle for extra credit, type it in anyway.
print("Here is a puzzle.\n")

what = add (age, substract(height, multiply(weight, divide(iq, 2))))
# first = iq / 2
# second = weight * first
# third = height - second
# fourth = age + third
# what = fourth


print("That becomes: ", what, "Can you do it by hand?")
math = 35 + 74 - 180 * 50 / 2
print("bonus: ", math, what, "ez clap!")