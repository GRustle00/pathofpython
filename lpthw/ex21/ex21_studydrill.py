def percentage(a, b):
    return a % b

def potence(a, b):
    return a ^ b

def greaterthan(a, b):
    return a > b

def comparative(a, b):
    return a is not b

tip = percentage(60, 18)
power = potence(7, 3)
bigger = greaterthan(8, 7)
smaller = greaterthan(7, 8)
unequal = comparative(1, 2)
equal = comparative(1, 1)

print(f"The tip would come up to {tip} which is eighteen percent of sixty\n")

print(f"Total units would be optained by elevating seven, three times which would total to {power}\n")

print(f"I have a 7 inch I think it feels bigger than the 8inch am I right? {smaller}. Ok how about this 9inch {bigger}\n")

print(f"One equals one? {equal}, what about two? {unequal}\n")