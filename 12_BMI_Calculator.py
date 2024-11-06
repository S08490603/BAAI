#
# Hansen
# BMI Calculator Assignment
#

# 1. Input
weight = float(input('Enter your weight in kilograms? '))
height = float(input('Enter your height in kilograms? '))
counter = 1

# 2. Process
BMI = weight / height**2 

# 3. Output

print(f'Your BMi is : {BMI}')

# Loop

answer = (input(f'Continue?(yes/no): '))
if answer == 'no':
    break
 



