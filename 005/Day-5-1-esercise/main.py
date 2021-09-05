# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
height_sum = 0
num_students = 0
for h in student_heights:
  h = int(h)
  height_sum += h
  num_students += 1
print(f"The average height is {round(height_sum / num_students)}")


