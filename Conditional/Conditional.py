# Conditional statments: if,else,elif,nested if:
# if contion always run.any thing in if it will provide always a statment.
# elif it will run only when if condition getting wrong..If if contion getting true so it will not run.
light = input("choose a color in small letter :")

if(light == "red"):
    print("stop")
elif(light == "yellow"):
    print("ready")
elif(light == "green"):
    print("go")
else:
    print("write suiteble color.")
  
#Nested if:
age = 32
if(age>=18): 
    if(age>=80):
        print("you cannot drive.")    
    else:
        print("you can drive")                                            
else:
    print("you cannot:")

# Calculator
num1= int(input("enter a number."))
num2= int(input("enter a number."))
operator = input("enter the sign (+,^,&,*,%,/,-,|):")
if (operator == '+') :
    print("Addition of two no. ",num1 + num2)
elif (operator == '-') :
    print("subtraction of two no. ",num1 - num2)
elif (operator == '*') :
    print("Multiplication of two no. ",num1 * num2)
elif (operator == '/') :
    if (num2 != 0):
        print("Divison of two no. ",num1 / num2)
    else:
        print("cannot divide by zero:")
elif (operator == '%') :
    print("Modulus of two no. ",num1 % num2)
elif (operator == '^') :
    print("Bitwise and of two no. ",num1 ^ num2)
elif (operator == '|') :
    print("bitwise or of two no. ",num1 | num2)
else:
    print("Invalid operator.")
  
# Range
num = int(input("enter the number:"))

if num >=10 and num <=50:

    print("the number is between 10 to 50")
   
else:
    print("No is outside the range.")
  
# divisible by 2 and 5. 
num = int(input("enter a number:"))

if num%2 == 0:
    if num%5 == 0:
        print("no is even and divisible by 5.")
    else:
        print("no is not divisible by 5.")
else:
    print("this number is neither even nor divisible by 5")

# Find number between.
num1 = int(input("enter a number:"))

if -9 <= num1 <= 9:
    print("The number is single digit:")

elif -99 <= num1 <= 99:
    print("The number is double digit:")
    
elif -999 <= num1 <= 999:
    print("The number is triple digit:")
    
elif -9999 <= num1 <= 9999:
    print("The number is four digit:")
else:
    print("invalid syntax.")


#  Nested if:
age = 8

nationality = "american"

if age>=18:

    if nationality == "indian":
        print("person is eligible for vote.")
    else:
        print("you are not eligible.Because you are not indian ")
else:
    print("Person is not eligible for vote.You are underage.")


# leap year.
year = int(input("enter the year."))
if year%4==0 and year%100!=0 or year%400 == 0:
  print("This is leap year.")
else:
  print("This is not a leap year.")


# nested if.
year = int(input("enter a number."))
if year %4==0:
  if year%100==0:
     if year%400==0:
      print("This is leap year.")
     else:
      print("this is not a leap year.")
  else:
    print("This is a leap year")
else:
  print("This is not a leap year.")

#  control flow.
Gender = input("Enter the gender:") #Male,Female
Age = int(input("Enter the Age."))
if Gender == "Male":
  if Age>=30 and Age<=60:
    print("you are going to bulding1 of Hotel A.")
  else:
    print("You are going to bulding2 of Hotel A.")
elif Gender == "Female":
  if Age>=30 and Age<=60:
    print("You are going to bulding1 of Hotel B. ")
  else:
    print("You are going to bulding2 of Hotel B.")
else:
  print("invalid..")


# simple intrest .
principle_amount = float(input("enter the principle amount"))
Rate = float(input("enter the rate:"))
year = int(input("enter the year."))
Month = int(input("enter the month."))
Months = input("enter the month name.")
days_input = int(input("enter the days."))


if Months=="January" or Months=="March" or Months=="May"or Months=="July" or Months=="August" or Months =="Octuber" or Months=="Decmber":
  Months_days = 31
elif Months =="February":
  if year%4==0 and year%100!=0 or year%400==0:
    Months_days = 29
  else:
    Months_days = 28
else:
  Months_days = 30


SI = (principle_amount*Rate*Month )/100 + (principle_amount*Rate*Days/Months_days)/100
print("Simple intrest",SI)
Total_amount = principle_amount+SI
print("Total amount is",Total_amount)


