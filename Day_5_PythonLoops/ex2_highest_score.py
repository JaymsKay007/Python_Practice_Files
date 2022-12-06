student_scores = input("Input a list of student score:").split()

for number in range(len(student_scores)):
    student_scores[number] = int(student_scores[number])
print(student_scores)

# highest_score = 0
# for score in student_scores:
#     if highest_score > score:
#         highest_score = score
# print(f"The highest score is {score}")

# 2nd solution
highest_score = max(student_scores)
lowest_score = min(student_scores)
print(f"The highest score is {highest_score}")
print(f"The lowest score is {lowest_score}")
