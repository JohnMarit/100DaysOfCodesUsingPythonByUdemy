# Input a Python list of student heights
student_heights = input("Enter students heights \n").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆
  
# Write your code below this row 👇
total_heights = 0
for height in student_heights:
  total_heights += height
print(f"total height = {total_heights}")

number_of_students = 0
for student in student_heights:
  number_of_students +=1
print(f"number of students = {number_of_students}")


average_heights = round(total_heights / number_of_students)
print(f"average height = {average_heights}")
