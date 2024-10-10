#
# Hansen
# Grade Calculator Assignment
#

# 1. Input
max_lap = int(input('How many subjects do you have? '))
curr_lap = 1

subjects = []
scores = []

# Loop 
while curr_lap <= max_lap:
    subject_name = input(f'Enter the name of subject {curr_lap}: ')
    score = int(input(f'Enter the score for {subject_name}: '))
    
    subjects.append(subject_name)
    scores.append(score)
    
    curr_lap += 1  

# 2. Process
total_score = sum(scores)  
average = total_score / max_lap  

# 3. Output

print(f"Your average score is: {average:.2f}")

if average >= 90:
    word = "Excellent!"
elif average >= 80:
    word = "Good work!"
else:
    word = "Keep it up, student!"

print(word)