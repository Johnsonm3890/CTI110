# Morgan Johnson
# 4/13/2025
# P4HW1
# Program to get number of scores input, calculate the lowest score, drop the lowest score and then calculate letter grade and average.

#Psuedo Code
#
# SC = input(scores from user)
#
# SCL = []
# for # of SCs
# temp value = input(score X from user)
# While True
    # if temp value < 0 or > 100
    #  print (User enter valid score between 0 - 100 please)
    # else
    # SCL.append(temp value)
    # break
#
# Lowest score = min(SCL)
# SCL.remove(lowest score)
# Sum scores = sum (SCL)
# average scores = sum scores / length(SCL)
#
# print results header
# print fstring the lowest grade width set and print calculated lowest 1 decimal place
# print fstring the modified list
# print fstring the average grade width set and print calculated average 2 decimal place
# print fstring the letter grade
# print results footer
#
#End Psuedo Code

#Prompt of # of scores

score_count = int(input('How many scores do you want to enter? '))



# initialize list

scores = []

for i in range(score_count):
    while True:
        temp = float(input(f"Enter score #{i+1}: ")) #get score

        if temp < 0 or temp > 100: #if invalid score prompt user
            print('Invalid Score Entered!!!!')
            print('Score should be between 0 and 100')
            pass
        else:
            scores.append(temp) #if valid score add to list
            break



low_out = min(scores) #Lowest score
scores.remove(min(scores))
sum_out = sum(scores) #Sum scores
avg_out = sum_out/ len(scores) #Average score

if avg_out >= 90: #if over 90 Grade is A
 letter = "A"
elif avg_out >= 80: #if over 80 less than 90 Grade is B
 letter = "B"
elif avg_out >= 70: #if over 70 less than 80 Grade is C
 letter = "C"
elif avg_out >= 60: #if over 60 less than 70 Grade is D
 letter = "D"
else: #if less than 60 Grade is F
 letter = "F"

#Print Score Info

print('------------Results------------')
print(f'{"Lowest Score:":<20}{low_out:.1f}')
print(f'{"Modified List:":<20}{scores}')
print(f'{"Scores Average:":<20}{avg_out:.2f}')
print(f'{"Grade:":<20}{letter}')
print('-------------------------------')






