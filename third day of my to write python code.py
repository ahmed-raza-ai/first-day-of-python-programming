"""    now i am writting code in python
about if elif and else condition
 find the greatest number    """

number = int(input("enter the number:"))

if number > 0:
    print("The number is positive.")
elif number == 0:
    print("The number is zero.")
else:
    print("The number is negative.")
    
# according to marks give grades
marks = int(input("Enter the marks: "))

if marks >= 90 and marks <= 100:
    print("YOU HAVE TAKEN A GRADE")
elif marks >= 82 and marks <= 89 :
    print("YOU HAVE TAKEN B GRADE")
elif marks >= 75 and marks <= 81 :
    print("YOU HAVE TAKEN C GRADE")
elif marks >= 60 and marks <= 74 :
    print("YOU HAVE TAKEN d GRADE")
else:
    print("you are fail better luck next time")
    
# how to find the greatest number
a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))
c = int(input("Enter the value of c: "))

if a >= b and a >= c:
    print("a is the largest number.")
elif b >= a and b >= c:
    print("b is the largest number.")
else:
    print("c is the largest number.")

if a == b == c:
    print("a, b, and c are equal.")
elif a == b:
    print("a and b are equal.")
elif b == c:
    print("b and c are equal.")
elif a == c:
    print("a and c are equal.")

# this program is about age categorization

age = int(input( "enter your age"))

if age < 13:
    print("you are a child")
elif age < 19:
    print("you are a teenager")
elif age < 36:
    print("you are a  adult")
else:
 print(" senior ")



