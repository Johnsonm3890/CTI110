# Morgan Johnson
# 3/15/2025
# P2HW1
# Building on P1HW2 Assignment, changing how results are diplayed


print("This program caculates and displays travel expenses")
print()
print("Enter Budget:", end=" ")
Enter_Budget=float(input())
print()
print("Enter your travel destination:", end=" ")
travel_destination=input()
print()
print("How much do you think you will spend on gas?", end=" ")
gas=float(input())
print()
print("Approximately, how much will you need for accomodation/hotel?", end=" ")
accomodation_hotel=float(input())
print()
print("Last, how much do you need for food?", end=" ")
food=float(input())
print()
print("------------Travel Expenses------------")
text='Location:'
print(f"{text:20}{travel_destination:<15}")
text='Inital Budget:'
print(f"{text:20}${Enter_Budget:<15.2f}")
text='Fuel:'
print(f"{text:20}${gas:<15.2f}")
text='Accomodation:'
print(f"{text:20}${accomodation_hotel:<15.2f}")
text='Food:'
print(f"{text:20}${food:<15.2f}")
print('---------------------------------------')
print()
output = Enter_Budget - gas - food - accomodation_hotel
text='Remaining Balance:'
print(f"{text:20}${output:<15.2f}")






