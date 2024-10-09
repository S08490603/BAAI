#
# Hansen
# Print Hello Hansen!
#

# 1. Input
n1 = int(input('Number 1: '))
n2 = int(input('Number 2: '))

# 2. Process
if (n1 < n2):
    bigger = n2
elif(n1 > n2):
    bigger = n1
else:
    bigger = 'Same'

# 3. Output
print(f'Bigger number: {bigger}')
