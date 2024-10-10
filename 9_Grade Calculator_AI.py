#
# Hansen
# Grade Calculator with max_lap and curr_lap
#

# 1. Input
max_lap = int(input('How many subjects do you have? '))
curr_lap = 1

subjects = []
scores = []

# Loop using max_lap and curr_lap
while curr_lap <= max_lap:
    subject_name = input(f'Enter the name of subject {curr_lap}: ')
    score = int(input(f'Enter the score for {subject_name}: '))
    
    # Store subject name and score in lists
    subjects.append(subject_name)
    scores.append(score)
    
    curr_lap += 1  # Increment the lap counter

# 2. Process
total_score = sum(scores)  # Sum of all scores
average = total_score / max_lap  # Calculate average score

# 3. Output
print("\n--- Report ---")
for i in range(max_lap):
    print(f"{subjects[i]}: {scores[i]}")

print(f"Total Score: {total_score}")
print(f"Your average score is: {average:.2f}")

# Providing feedback based on average score
if average >= 90:
    word = "Excellent!"
elif average >= 80:
    word = "Good work!"
else:
    word = "Keep it up, student!"

print(word)