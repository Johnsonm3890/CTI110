# Morgan Johnson
# 4/13/2025
# P4HW2
# Gross Pay Calculator with Overtime for multiple employees with business total calculation


# Start Pseudocode
# While loop
# name = input(name prompt or finished)\
# if name == done break while loop
# else continue
# hours = input(hours prompt)
# rate = input(rate prompt)

# if(hours>40)
# overtime hour = hours - 40
# overtime pay = overtimehours*(1.5*payrate)
# hours_adj = 40
# else
# overtime hour = 0
# overtime pay = 0
# hours_adj = hours

# reg pay = hours_adj*rate
# gross pay = reg pay + overtime pay

# print(format filler)
# print(employee name)
# print(hours worked Header:10,pay Header:10,Overtime Header:10,Overtimepay Header:10,regPay Header:10,grosspay Header:10
# print(format filler)
# print(hours:10,payrate:10,OvertimeHours:10,OvertimePay:10,RegPay:10,Grosspay:10)

# Add 1 employee to employee count
# Add Overtime pay to total
# Add regular pay to total
# add gross pay to total

# outside of while loop
# print employee total
# print overtime total
# print regular total
# print gross total

# End Pseudocode

#intialize variables
#name = 'test'
total_e = 0
total_over = 0
total_reg = 0
total_gross = 0


while True: #start while loop
 name = input("Enter employee's name or \"Done\" to terminate: ") #prompt user
 if name == 'Done': #if done leave while loop
  break
 else: #else pass
  pass



 hours = float(input("Enter number of hours worked: ")) #gather hours
 pay_rate = float(input("Enter employee's pay rate: ")) #gather pay rate

 if hours>40: #determine overtime
  overtime_hours = float(hours - 40)
  overtime_pay = float(overtime_hours*(1.5*pay_rate)) #determine overtime pay
  hours_adj = float(40)
 else:
  overtime_hours = float(0)
  overtime_pay = float(0)
  hours_adj = float(hours)

 reg_pay = float(hours_adj*pay_rate) #determine Pay
 gross_pay = float(reg_pay + overtime_pay) #deterime gross pay

#print results
 print('-------------------------------')
 print(f'{'Employee name:':<15}{name:<15}')
 print()
 print(f'{'Hours Worked':<15}{'Pay Rate':<15}{'OverTime':<15}{'OverTime Pay':<15}{'RegHour Pay':<15}{'Gross Pay':<15}')
 print('------------------------------------------------------------------------------------------')
 print(f'{hours:<15.1f}${pay_rate:<14.1f}{overtime_hours:<15.1f}${overtime_pay:<14.2f}${reg_pay:<14.2f}${gross_pay:<14.2f}')

#increment total counters
 total_e += 1
 total_over += overtime_pay
 total_reg += reg_pay
 total_gross += gross_pay


#print totals outside of while loop
print(f"Total number of employees entered: {total_e}")
print(f'Total amount paid for overtime: {total_over:.2f}')
print(f'Total amount paid for regular hours: {total_reg:.2f}')
print(f'Total amount paid in gross: {total_gross:.2f}')




