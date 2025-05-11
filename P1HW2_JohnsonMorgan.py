# Morgan Johnson
# 3/2/2025
# P1HW2
# Create a python program that does basic math


print("This program caculates and displays travel expenses")
print()
print("Enter Budget:", end=" ")
Enter_Budget=int(input())
print()
print("Enter your travel destination:", end=" ")
travel_destination=input()
print()
print("How much do you think you will spend on gas?", end=" ")
gas=int(input())
print()
print("Approximately, how much will you need for accomodation/hotel?", end=" ")
accomodation_hotel=int(input())
print()
print("Last, how much do you need for food?", end=" ")
food=int(input())
print()
print("------------Travel Expenses------------")
print("Location:", end=" ")
print(travel_destination)
print("Inital Budget:", end=" ")
print(Enter_Budget)
print()
print("Fuel:", end=" ")
print(gas)
print("Accomodation:", end=" ")
print(accomodation_hotel)
print("Food:", end=" ")
print(food)
print()
output = Enter_Budget - gas - food - accomodation_hotel
print("Remaining Balance:", end=" ")
print(output)





