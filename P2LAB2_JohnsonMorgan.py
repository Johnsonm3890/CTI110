# Morgan Johnson
# 3/10/2025
# P2LAB2
# How to write code that uses a dictionary to store user input and display output to user

my_dict = {'Camaro':18.21,'Prius':52.36,'Model S':110,'Silverado':26}
my_dict_keys= my_dict.keys()
print(my_dict_keys)
print("Enter a vehicle to see it's mpg:",end=" ")
vehicle = input()
print(f'The {vehicle} gets {(my_dict[vehicle])} mpg.')
print(f'How many miles will you drive the {vehicle}?', end=" ")
miles = float(input())
gas = float(miles/my_dict[vehicle])
print(f"{gas:.2f} gallon(s) of gas are needed to drive the {vehicle} {miles} miles.")
