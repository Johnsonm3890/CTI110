# Morgan Johnson
# 3/29/2025
# P3HW2
# Gross Pay Calculator with Overtime


# Start Pseudocode

# name = input(name prompt)
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

# End Pseudocode


name = input("Enter employee's name: ")
hours = float(input("Enter number of hours worked: "))
pay_rate = float(input("Enter employee's pay rate: "))


if hours>40:
 overtime_hours = float(hours - 40)
 overtime_pay = float(overtime_hours*(1.5*pay_rate))
 hours_adj = float(40)
else:
 overtime_hours = float(0)
 overtime_pay = float(0)
 hours_adj = float(hours)

reg_pay = float(hours_adj*pay_rate)
gross_pay = float(reg_pay + overtime_pay)

print('-------------------------------')
print(f'{'Employee name:':<15}{name:<15}')
print()
print(f'{'Hours Worked':<15}{'Pay Rate':<15}{'OverTime':<15}{'OverTime Pay':<15}{'RegHour Pay':<15}{'Gross Pay':<15}')
print('------------------------------------------------------------------------------------------')
print(f'{hours:<15.1f}${pay_rate:<14.1f}{overtime_hours:<15.1f}${overtime_pay:<14.2f}${reg_pay:<14.2f}${gross_pay:<14.2f}')






