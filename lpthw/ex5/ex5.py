name = 'Guillermo A Fernandez'
age = 29
height = 66
weight = 156
eyes = 'Brown'
teeth = 'White'
hair = 'Black'
weight_kilograms = weight * 0.453
height_cm = height * 2.5

print(f"Let's talk about {name}.")
print(f"He's {height} inches tall ({height_cm} cm).")
print(f"He's {weight} pound heavy.")
print(f"how much is that in kg?")
print(f"It should be {weight_kilograms} heavy")
print(f"Actually that's not too heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee.")

# this line is tricky, try to get it exactly right
total = age + height + weight
print(f"If I add {age}, {height}, and {weight} I get {total}.")
