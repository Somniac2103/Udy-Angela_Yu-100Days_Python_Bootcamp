student_scores = {
  'Harry' : 88,
  'Ron' : 78,
  'Hermione' : 95,
  'Draco' : 75,
  'Neville' : 60
}

student_grades = student_scores


for student in student_grades:
  if student_grades[student] >= 91:
    student_grades[student] = "Outstanding"
  elif student_grades[student] >= 81:
    student_grades[student] = "Exceeds Expectations"
  elif student_grades[student] >= 71:
    student_grades[student] = "Acceptable"
  else:
    student_grades[student] = "Fail"

print(student_grades)

