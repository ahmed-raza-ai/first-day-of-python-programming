# with the help of loop we can put the items of dictionary and then check it the values of dic is expensive or not


products = {}
num = int(input("enter the number of product you can enter in this dictionary "))
for i in range(num):
   product = input("enter the  product :")
   prices = int(input("enter the prices of product ;"))

   products[product] = prices

for product,prices in products.items():
    if prices > 50000:
        print( product ," is expensive :")
    else:
        print( product ," is affordable :")

total_prices = 0   
for product in products:

    total_prices += products[product]  

print("the total price is " ,total_prices )