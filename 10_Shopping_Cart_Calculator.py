#
# Hansen
# Shopping Cart Calculator Assignment
#

# 1. Input
total_item = int(input('How many items do you want to buy? '))
counter = 1

total_shopping_cost = []


# Loop 
while counter <= total_item:
    item_name = input(f'Enter the name of item {counter}: ')
    item_price = int(input(f'Enter the price of the : '))
    item_quantity = int(input(f'Enter the quantity of the {item_name}: '))
    total_cost = item_price*item_quantity
    
    (print(f'Total cost for {item_name}: {total_cost}'))

    total_shopping_cost.append(total_cost)
    
    counter += 1  

# 2. Process
sum_total_cost = int(sum(total_shopping_cost))

# 3. Output

print(f"Total cost of your shopping cart: {sum_total_cost}")