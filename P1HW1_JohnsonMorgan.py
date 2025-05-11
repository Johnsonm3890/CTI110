# Morgan Johnson    
# 3/1/2025
# P1HW1
# Writing a Python Program that uses mathematical expressions


print("-----Calculating Exponenets----\n\n") 
print("Enter an integer as the base value:", end=" ")
Base_Value=int(input())
print("Enter an integer as the exponent:", end=" ")
Exponent=int(input())
output = Base_Value ** Exponent
print("\n")
print(Base_Value, end=" ")
print("raised to the power of", end=" ")
print(Exponent, end=" ")
print("is",end=" ")
print(output, end=" ")
print("!!")
print("\n\n-----Addition and Subtraction----\n\nEnter a starting integer:",end=" ")
Starting_Value=int(input())
print("Enter an integer to add:", end=" ")
Add_Value=int(input())
print("Enter an integer to subtract:", end=" ")
Sub_Value=int(input())
output2 = Starting_Value + Add_Value - Sub_Value
print("\n\n")
print(Starting_Value, end=" ")
print("+", end=" ")
print(Add_Value, end=" ")
print("-", end=" ")
print(Sub_Value, end=" ")
print("is equal to", end=" ")
print(output2)
 
