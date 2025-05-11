# Morgan Johnson
# 3/21/2025
# P2HW2
# Program to calculate min,max,sum, and average grade.

#psuedo Code

# input1 = input('enter grade 1') type float
# input2 = input('enter grade 2') type float
# input3 = input('enter grade 3') type float
# input4 = input('enter grade 4') type float
# input5 = input('enter grade 5') type float
# input6 = input('enter grade 6') type float

# list of grades = [input1, input2, ..., input6]

# Lowest grade = min(grades)
# Highest grade = max(grades)
# Sum grades = sum (grades)
# average grades = sum grades / number of grades (6)

# print results header
# print fstring the lowest grade width set and print calculated lowest 1 decimal place
# print fstring the highest grade width set and print calculated highest 1 decimal place
# print fstring the sum of grades width set and print calculated sum 1 decimal place
# print fstring the average grade width set and print calculated average 2 decimal place
# print results footer

#End psuedo code

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





