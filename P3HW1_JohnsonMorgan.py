# Morgan Johnson
# 3/21/2025
# P3HW1
# Program to calculate Lowest, Highest, Sum, and Average Grade. Additionally, Program produces letter grade based on average.


# Enter grades for six modules

mod_1 = float(input('Enter grade for Module 1: '))
mod_2 = float(input('Enter grade for Module 2: '))
mod_3 = float(input('Enter grade for Module 3: '))
mod_4 = float(input('Enter grade for Module 4: '))
mod_5 = float(input('Enter grade for Module 5: '))
mod_6 = float(input('Enter grade for Module 6: '))

# add grades entered to a list

grades = [mod_1, mod_2, mod_3, mod_4, mod_5, mod_6]


low_out = min(grades) #Lowest Grade
high_out = max(grades) #Highest Grade
sum_out = sum(grades) #Sum Grades
avg_out = sum_out/ len(grades) #Average Grades

#Print Grade Info

print('------------Results------------')
print(f'{"Lowest Grade:":<15}{low_out:>10.1f}')
print(f'{"Highest Grade:":<15}{high_out:>10.1f}')
print(f'{"Sum of Grades:":<15}{sum_out:>10.1f}')
print(f'{"Average:":<15}{avg_out:>10.2f}')
print('-------------------------------')

#Print Letter Grade

if avg_out >= 90: #if over 90 Grade is A
 print('Your grade is: A')
elif avg_out >= 80: #if over 80 less than 90 Grade is B
 print('Your grade is: B')
elif avg_out >= 70: #if over 70 less than 80 Grade is C
 print('Your grade is: C')
elif avg_out >= 60: #if over 60 less than 70 Grade is D
 print('Your grade is: D')
else: #if less than 60 Grade is F
 print('Your grade is: F')



