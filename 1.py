#A String
class_name = "P5_Delinquents: " 
#error class_name +
student1 = "Carlos "
top_delinquents = student1 + "Nickolas, Gianna, Gonzalo"
class_students = class_name + top_delinquents

print(class_students)

same_name = 2
third_student =3
print(type(same_name))
student2 = "Carlos" + str(same_name)
print(student2)
student3 = "Carlos" + str(third_student)
print(student3)

grade1 = (input("What did you get in P1?"))
grade2 = (input("What did you get in P2?"))
grade3 = (input("What did you get in P3?"))
grade4 = (input("What did you get in P4?"))

print("To verify: You scored " + grade1 + "ln" + grade2 + grade3 + grade4)

gpa = (grade1 + grade2 + grade3 + grade4)
print(gpa)
