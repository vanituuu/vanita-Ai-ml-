# Arithmetic Operator
# Variables
a = 15
b = 4

# Addition
print("Addition:", a + b)  

# Subtraction
print("Subtraction:", a - b) 

# Multiplication
print("Multiplication:", a * b)  

# Division
print("Division:", a / b) 

# Floor Division
print("Floor Division:", a // b)  

# Modulus
print("Modulus:", a % b)

# Exponentiation
print("Exponentiation:", a ** b)

# calculate the sum of two number: usinf format string.
num1 = int(input("enter a 1st number:"))
num2 = int(input("enter a 2nd number:"))
sum_1 = num1+num2
print(f"Sum of two number {num1}+{num2} = {sum_1}")


# calculate the sum of two float value:
first_1 = float(input("enter a number:"))
Second_2 = float(input("enter a number:"))
sum_2 = first_1 + Second_2
print(f"Sum of two number {first_1} + {Second_2} = {sum_2}")

# Age calculator.
birth_year = int(input("enter your birth year:"))
current_year = int(input("enter the year."))
age = current_year-birth_year
print("your age is:",age)

# rupee.
inr = float(input("enter the INR:"))
usd = inr / 83
eur = inr / 90
gbp = inr / 100
print("usd",usd)
print("gbp",gbp
print("eur",eur)

#  Resturant bill calculator.
price = int(input("enter the price of item."))
quantity = int(input("enter the quantity. ") )
Total =  price* quantity
gst = Total*0.05
grand_total = Total + gst
if grand_total>1000:
    discount=grand_total*5/100
    grand_total-=discount
print("Final bill",grand_total)

# Movie Ticket:
print("Paytm")
print("_______________________________________________")

movie1 = int(input("enter the movie1 price:"))
movie2 = int(input("enter the movie2  price:"))
Popcorn = int(input("enter the popcorn price:"))
coldDrink_1 = int(input("enter the coldDrink_1 price:"))
Burger = int(input("enter the Burger price:"))
Total = movie1  + Popcorn + coldDrink_1
print("your total bill:",Total)









