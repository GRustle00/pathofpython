#Print function. Output text into console.
print("Hello Python world!")

message = "Hello Python world!"
print(message)

message = "Hello Python Crash Course world!"
print(message)

message = "Hello Python Crash Course reader!"
print(message)

name = "Guillermo Fernandez"
print(name.title())
print(name.upper())
print(name.lower())

first_name = "guillermo"
Last_name = "fernandez"
full_name = f"{first_name} {Last_name.upper()}"
print(full_name)

first_name = "guillermo"
last_name = "fernandez"
full_name = "{} {}".format(first_name.upper(), last_name)
print(full_name)