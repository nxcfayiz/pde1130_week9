# Calculating Grades (ok, let me think about this one)

# Write a program that will average 3 numeric exam grades, return an average test score, a corresponding letter grade, and a message stating whether the student is passing.

# Average	Grade
# 90+	A
# 80-89	B
# 70-79	C
# 60-69	D
# 0-59	F

# Exams: 89, 90, 90
# Average: 90
# Grade: A
# Student is passing.

# Exams: 50, 51, 0
# Average: 33
# Grade: F
# Student is failing.

exam_one = int(input("Input exam grade one: "))
#convert the input to integer
exam_two = int(input("Input exam grade two: "))
#input is converted to integer and variable is changed from exam_3 to exam_three
exam_three = int(input("Input exam grade three: "))

#a coma is missing in list grades
grades = (exam_one, exam_two, exam_three)
total = 0

for grade in grades:
    total += grade

#spelling error for variable grades
avg = total / len(grades)

if avg >= 90:
    letter_grade = "A"
elif 80 <= avg < 90: #colon missing
    letter_grade = "B"
elif 70 <= avg < 80:
    letter_grade = "C"
elif 65 <= avg <= 69:
    letter_grade = "D"
else:
    letter_grade = "F"

# Print individual grades
for grade in grades:
    print("Exam:", grade)

print("Average:", avg)
print("Grade:", letter_grade)

# Check if the student is passing or failing
if letter_grade == "F": #hyphun in letter-grade changed to _ and 'is' changed to ==
    print("Student is failing.")
else:
    print("Student is passing.")
    
