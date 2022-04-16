student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}

# creating an empty dictionary name with student grades
student_grades={}

for student in student_scores:
    score=student_scores[student]
    if score>90:
        student_grades[student]="Outstanding"
    elif score>80:
        student_grades[student]="Exceeds Expectations"
    elif score>70:
        student_grades[student]="Acceptable"
    else:
        student_grades[student]="Fail"
    


print(student_grades)
# for grade in student_grades:
#     print(grade)
#     print(student_grades[grade])





