#
# Hansen
# Simple Tip Calculator Assignment
#

# 1. Input
total_people = int(input('How many people are dining? '))
counter = 1

total_spending = []

# Loop 
while counter <= total_people:
    spending = int(input(f'Enter the amount spent by person {counter}: '))
    total_spending.append(spending)

    counter += 1     

    total_bill = sum(total_spending) 

# 2. Process
tip = int(input(f'Enter the tip percentage : '))
total_tip = (total_bill * tip) / 100 

total_cost_with_tip = total_bill + total_tip

# 3. Output

(print(f'The total bill including tip is : ${total_cost_with_tip}'))