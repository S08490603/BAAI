#
# Hansen
# BMI Calculator Assignment
#

# 1. Input
while True:

    weight = float(input('Enter your weight in kilograms? '))
    height = float(input('Enter your height in meters? '))

# 2. Process
    BMI = weight / height**2 

# 3. Output

    print(f'Your BMi is : {BMI}')

# Loop

    answer = input('Continue?(yes/no): ')
    if answer == 'no':
        break