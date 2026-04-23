# Create a Python program that stores the grades of five students
# in a dictionary. Allow users to input the names of the students
# and their respective grades. Calculate and display the average grade of the students.

student_grades = [
    {"id":1, "name":"venu", "grade":500},
    {"id":2, "name":"gopi", "grade":480},
    {"id":4, "name":"varun", "grade":360},
    {"id":3, "name":"vikas", "grade":590},
]

###Add student
next_id = len(student_grades)+1
name = input("enter student name: ")
grade = int(input("enter student grade: "))

student_grades.append({"id":next_id, "name":name, "grade":grade})

print(student_grades)

total_grades = 0
for student in student_grades:
    print(student)
    total_grades += student["grade"]

print(len(student_grades))
print("total grades: ", total_grades)
print("Avg: ", total_grades/ len(student_grades))


# student_grades.sort(key=lambda x:x["grade"])
# print(student_grades)