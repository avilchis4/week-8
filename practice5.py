# Problem 5
import student_data
students = student_data.students
HR = input('what is the homeroom: ')
found = False
for student in students:
    if HR == student['HR']:
      print(F'FOUND STUDENT {student['Combo,Name']}')
      found = True
      break
    else:
       print(student['HR'])
       print("That student is not in this homeroom.")