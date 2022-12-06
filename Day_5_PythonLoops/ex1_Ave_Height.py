student_height = input("Input a list of student height:").split()
for n in range(len(student_height)):
    student_height[n] = int(student_height[n])
print(student_height)

# TOTAL HEIGHT
# total_height = 0
# for height in student_height:
#     total_height += height
# print(total_height)

# 2nd way of solving
total_height = sum(student_height)
print(total_height)

# Number(len) of student height
# number_of_students = 0
# for number in student_height:
#     number_of_students += 1
# print(number_of_students)

# 2nd way of solving
number_of_students = len(student_height)
print(number_of_students)

# average_height
average_height = round(total_height / number_of_students)
print(average_height)
