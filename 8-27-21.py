day = "Thursday"
print(type(day))
day = 32.5
print(type(day))
day = 19
print(type(day))
day = 21
print(type(day))

express1 = input("How much did you earn on Sunday?")
express2 = input("How much did you earn on Monday?")
#total$ is a bad var name because of the $
#2total is bad var name because starts with number
#total spent is bad var name because it has a space
total = float(express1) + float(express2)
total_rounded = round(total,3)

print("You spent $" + "{:.2f}".format(total))
print("You spent $" + str(total_rounded))

x = int(1)
y = int(2.8)
z = int("3")

print(x, end= " ")
print(y, end = " ")
print(z, end = " ")

x = float(1)
y = float(2.8)
z = float("3")
w = float("4.1")
print(x, end = " ")
print(y, end = " ")
print(z, end = " ")
print(w)

x = str("s1")
x = str(2)
x = str(3.0)
print(x)

#take a radius as an input. Print the area of that circle
#take a radius as an output.Print out the volume of sphere
#each answer should be rounded to 4 decimal points
