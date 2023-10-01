# Input a Python list of student heights
student_heights = input().split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])


total_height = 0
list_length = 0

for i in student_heights: 
  total_height += i
  list_length += 1
  

print(f"total height = {total_height}")
print(f"number of students = {list_length}")
print(f"average height = {round(total_height / list_length)}")