# using lenghth string to find lenght
a = "my name is muhammad ahmed raza"
print(len(a))

# use in word to find word are in string

my_txt = "i am learning python many weeks and now i am practicing string methods"
print("how" in my_txt)

# example of in string

my_txt = "i am learning python many weeks and now i am practicing string methods"
print("how"  not in  my_txt)

# example of in string
my_txt = "i am learning python many weeks and now i am practicing string methods"
print("am" and "i"   in  my_txt)

#example of in string with if condition
my_txt = "i am learning python many weeks and now i am practicing string methods"
if "how " in my_txt:
     print("how string is present  in my_txt variable")
else:
    print("how keyword  are not present in my_txt variable")
    
# now we are going to write code of slicing

my_txt = "i am learning python many weeks and now i am practicing string methods"
print(len(my_txt))
print(my_txt[ 0 :70 ])

my_txt = "i am learning python many weeks and now i am practicing string methods"
print(len(my_txt))
print(my_txt[ 4 :55 ])

my_txt = "i am learning python many weeks and now i am practicing string methods"
print(len(my_txt))
print(my_txt[ 4 : ])

my_txt = "i am learning python many weeks and now i am practicing string methods"
print(len(my_txt))
print(my_txt[  :55 ])

my_txt = "i am learning python many weeks and now i am practicing string methods"
print(len(my_txt))
print(my_txt[ -1 :-55 ])

# upper string
my_txt = "i am learning python many weeks and now i am practicing string methods"
print(my_txt.upper())

my_txt = "i am learning python many weeks and now i am practicing string methods"
b = my_txt.upper()
print(b)

#lower string
txt = " now i am seeking a intenship job of software house to use my skill and increase my ability of learning "
print(txt.lower())

# replace string
name = "my laptop is very rare because it is foreign " 


txt = " now i am seeking a intenship job of software house to use my skill and increase my ability of learning "
print(txt.replace("house", "company"))

txt = txt.replace("seeking", "giving") .replace("my" ,"your") 
print(txt)

# strip string to remove white spaces
txt = " now i am seeking a intenship job of software house to use my skill and increase my ability of learning "
txt = txt.strip()
print(txt)

# split divide string into a list of sub string
txt = "now i am seeking a intenship job of software house to use my skill and increase my ability of learning"
words = txt.split()
print(words)


# f place holder variable and perform operation in curley bracket

cake_price = 1000
price_of_sweet = (f"i was buying a cake and i think the price of cake is {cake_price}")
print(price_of_sweet)

name = "AHMED"
age = 18
formatted_string = f"My name is {name} and I am {age} years old."
print(formatted_string)

