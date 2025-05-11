# Morgan Johnson
# 3/10/2025
# P2LAB1
# How to write code that performs mathmatical calculations and displays information

import math

print('What is the radius of the circle?',end=" ")
cradius = float(input())
cdia = '{:.1f}'.format(2*cradius)
ccir = '{:.2f}'.format(2*math.pi*cradius)
carea = '{:.3f}'.format(math.pi*(cradius ** cradius))
print('\n')

print(f'The diameter of the cirlce is {cdia}')
print('\n')
print(f'The circumference of the circle is {ccir}')
print('\n')
print(f'The area of the circle is {carea}')



