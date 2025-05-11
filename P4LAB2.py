# Morgan Johnson
# 4/06/2025
# P4LAB2
#Create multiplication table




#initialize while loop
cont = "yes"
#

while cont == 'yes':
 num = int(input("Enter an integer: ")) #get first integer
 if num < 0: #check if integer is negative
  print(f'This program does not handle negative numbers')
 else:
  y = 0 #initialize multiplication table
  for i in range(12): #print first 12 multiples
   y = y+1
   out = num*y
   print(f'{num}{' * '}{y}{' = '}{out}')
 while True: #Sub while loop to prompt user to continue looking specifically for a yes or a no.
  cont = input('Would you like to run the program again? ')
  if cont == 'yes': #if yes leave this sub while loop to main while loop and repeat program.
   break
  elif cont == 'no': #if no leave this sub while loop to main while loop and exit program.
   break
  else: #if cont !=  "no" or "yes" remain in sub while loop and be prompted again.
   pass
print(f'Exiting program...') #exit program when cont == no.







