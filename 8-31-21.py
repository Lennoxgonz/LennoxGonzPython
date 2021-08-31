#your_name = input("Write your name: ")
#print(your_name[6:])

school = "Coral Gables Senior High"
#print out 10th letter
#print(school[9])

"""
print out the tenth letter 
to the end of the string
"""

#print out second to fifth letter
#print(school[1:4])

#in reverse?
#print(school[::-1])

#the lenth of the string
#L = len(school)
#print("Size of string is", L)

#print every other letter 
#print(school[::2])

#print("Where is the first space in the string")
#print(school.index(" "))
#print("Where is the second space in in the string")
#print(school.index(" ", 6))
#print(school[:5])
#print(school[5:12])

month = input("Birth Month: ")
day = input("Birth Day: ")
year = input("Birth Year: ")
n = input("Your First and Last Name: ")

space = n.index(" ") 
initial = n[0] + n[space + 1]
print(month + day + year + initial)
