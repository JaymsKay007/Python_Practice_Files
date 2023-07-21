"""
Instructions to teacher...
Write a program that convert their scores to grades. By the end of the program, you should have a new dictionary called
student_grades that should contain students names for keys and their grades for values.
The final version of students_grades dictionary will be checked.
DO NOT modify the existing students_grades dictionary.
DO NOT write any print statements.
This is the score criteria...
Score 91 - 100: Grades = "Outstanding"
Score 81 - 90: Grades = "Exceeds expectation"
Score 71 - 80: Grades = "Acceptable"
Score 70 or lower: Grades = "Fail"
"""
student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}
# 🚨 Don't change the code above 👆

# TODO-1: Create an empty dictionary called student_grades.
student_grades = {}

# TODO-2: Write your code below to add the grades to student_grades.👇
for students in student_scores:
    scores = student_scores[students]
    if scores > 90:
        student_grades[students] = "Outstanding"
    elif scores > 80:
        student_grades[students] = "Exceeds expectation"
    elif scores > 70:
        student_grades[students] = "Acceptable"
    else:
        student_grades[students] = "Fail"

# 🚨 Don't change the code below 👇
# for students, grades in student_grades.items():
#     print(students, "=", grades)
print(student_grades)
