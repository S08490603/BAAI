#
# Hansen
# Grade Calculator
#

# 1. Input
n1 = int(input('Score Mathematics: '))
n2 = int(input('Score English: '))
n3 = int(input('Score Mandarin: '))

# 2. Process

total_score = n1 + n2 + n3
average = total_score / 3

if average >= 90:
    letter_grade = 'A'
elif average >= 80:
    letter_grade = 'B'
elif average >= 70:
    letter_grade = 'C'
elif average >= 60:
    letter_grade = 'D'
else:
    letter_grade = 'F'

# 3. Output
print(f"Total Score: {total_score}")
print(f"Average Score: {average:.2f}")
print(f"Letter Grade: {letter_grade}")

# Providing feedback based on letter grade
if letter_grade == 'A':
    word = "Excellent!"
elif letter_grade == 'B':
    word = "Good work!"
else:
    word = "Keep it up, student!"

print(word)