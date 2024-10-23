#
# Hansen
# Shopping Cart Calculator Assignment
#

# 1. Input
total_people = int(input('How many people are dining? '))
counter = 1

total_spending = []


# Loop 
while counter <= total_people:
    spending = input(f'Enter the amount spent by person {counter}: ')
    tip = int(input(f'Enter the tip percentage : '))

    total_bill = sum(total_spending) 

    counter += 1  
    
    total_tip = (total_bill * tip) / 100 
    
    

# 2. Process
total_cost_with_tip = total_bill + total_tip

# 3. Output

(print(f'The total bill including tip is : ${total_cost_with_tip}'))