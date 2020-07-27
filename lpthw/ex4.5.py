#Variable defining amount of cars available.
cars = 100
#Variable defining space in the car by changing removing the decimal the end result is not represented as a float number.
space_in_a_car = 4
#variable defining amount of drivers
drivers = 30
#variable defining amount of passengers
passengers = 90
#The line below will translated to cars_not_drive = 100 - 30
cars_not_driven = cars - drivers
#The line below will equal 30 as its defined by the driver variable
cars_driven = drivers
#The line below will translate to 30 * 4 defined in line 3 (Space_in_a_car) and 4 (drivers)
carpool_capacity = cars_driven * space_in_a_car
# average_passengers_per_car = car_pool_capacity / passenger. Due to the way the code is written it does not match the previously defined variables causing an error when attempting to run If it was ran the way it was. In the "Runback error" it will be defined in Line 8 (Origin of error) since it does not atches variables in line 7 and 4.
average_passengers_per_car = passengers / cars_driven


print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car, "in each car.")
