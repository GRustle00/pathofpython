def panic_counter(days_with_panic, days_without_panic):
    print(f"I've had {days_with_panic} days where I panicked, and {days_without_panic} that I have not.")
    print("Looking at it in hindsight I have panicked less than being calm.")
    print("I believe we call that progress.")
    print("I blieve I call that hope.\N{GRINNING FACE}")

panic_counter(12, 75) #1

panic_counter(3* 4, 5 * 15) #2

#setting variables
days_of_panic = 12
days_of_calm = 75
panic_counter(days_of_panic, days_of_calm) #3

panic_counter('Twelve', 'Seventy Five') #4

#setting input variables
print("Now you try it!")
print("How many days of panic?")
panic_input = int(input("> "))
print("How many days of calm?")
calm_input = int(input("> "))
panic_counter(panic_input, calm_input) #5

#more set variables
panic1 = 3
panic2 = 4
calm1 = 5
calm2 = 15
panic_counter(panic1 * panic2, calm1 * calm2) #6

panic_counter(15 - 3, 175 - 100) #7

panic_counter(days_of_panic, calm1 * calm2) #8

panic_counter(panic_input, calm2 * calm1) #9

panic_counter(days_of_panic, calm_input > calm2)