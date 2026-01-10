
# so today i am coding  in python about list and it methods

# ADD TWO LIST AND THEN PRINT
list1 =["my","name","is"]
list2 =[ "muhammad", "ahmed" , "raza" , ]
list3 = list1+list2
print(list3)

# MULTIPLICATION OF list3
list4 =["ahmed","ali",11]
list5 = list4 * 5
print(list5)

#append method to add the last element in the list5

list5.append("software")
print(list5)

# sort method to use ascendig order 

list = [4,4,4,5,6,7,8,1,2,3,4,5,5,]
list.sort()
print(list)

#take input from user in the list
list = []
list.append (input("ENTER THE FIRST country name:"))
list.append (input("ENTER THE second country name:"))
list.append (input("ENTER THE third country name:"))
print(list)

#take input from user in the from of integers
num = []
num.append (input("ENTER THE FIRST number :"))
num.append (input("ENTER THE second number :"))
num.append (input("ENTER THE third number:"))
print(num)

#SORT THE list
num.sort()
print(num)


#unsort the list
num.sort(reverse = True)
print(num)

#sorting in base string
names = []
names.append(input("enter the first name :"))
names.append(input("enter the second name :"))
names.append(input("enter the third name :"))
names.append(input("enter the fourth name :"))
names.append(input("enter the fifth name :"))


names.sort()
print(names)

 # unsorting
names.sort(reverse = True)
print(names)

#insert method use to ad element in the list
names.insert(1 , "ahmed")
print(names)

#remove method 
list = ["ahmed","khan", "ali", "raza"]
list.remove("khan")
print(list)

#lenghth method
total_lenghth = len(list)
print( total_lenghth)

#find class
print(type( names))

#copy method
list = [1,2,3,4,5,6,7]
list2 = list.copy()
print(list2)


#slicing in list2

names = list[3:6]
print(names)

names = list[:6]
print(names)

names = list[1:]
print(names)

names = list[-5:-1]
print(names)


#palindrome
# Original list
list = [1, 2, 3, 4, 5, 6, 7]

# Copy the list
list1 = list.copy()
print("Original list:", list1)

# Reverse the copied list
list1.reverse()
print("Reversed list:", list1)

# Check if the original list is the same as the reversed list
if list1 == list:
    print("The list is a palindrome")
else:
    print("The list is not a palindrome")

#palindrome list example
carinfo = ["racecar"]

# Copy the list
list1 = carinfo.copy()
print("Original list:", list1)

# Reverse the copied list
list1.reverse()
print("Reversed list:", list1)

# Check if the original list is the same as the reversed list
if list1 == carinfo:
    print("The list is a palindrome")
else:
    print("The list is not a palindrome")

# TUPPLE EXAMPLE
    
ames = ("ahmed" , "raza","khan", "ali", "raza") 
# find type
print(type(names))

#find lenghth of tuple
print(len(names))
print(names)

# slicing of tuple in diffrent ways
info = names[1:3]
print(info)

info = names[1:5]
print(info)

info = names[3:]
print(info)

info = names[:5]
print(info)

info = names[-2:-1]
print(info)

#index to find the first occurence of element
car = ("corolla","city","civic", "alto")
num = car.index("corolla")
print(num)

string = ("hello world","company","house","flat")
indexnum = string.index("flat")
print(indexnum)

#count to find the how many time the element are using in the string  
num =string.count("flat")
print(num)

citynames = ("karachi", "hyderabad" , "banarass" , "multan", "lahore" )
num = citynames.count("lahore")
print(num) # return 1


string =("hello world",)
name = string.count("l")
print(name)
