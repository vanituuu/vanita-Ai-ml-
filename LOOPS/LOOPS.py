# While loops
# 1. While loops
n=1
while n<11:
  n+=1
  print(n)

# 2. unit digit question
sum = 0
num = 46442
while num>0:
  digit = num%10
  sum +=digit
  num = num//10   # // is used for remove the decimal
print(sum)

# 3. reverse a number.
num = int(input("Enter the number:"))
reverse = 0
while num>0:
  digit = num%10
  reverse= reverse*10 +digit
  num = num//10
print(reverse)

# 4. palindrome number.
# why we compare it with temp_num.because when we used loop the num variable will be empty .
#So we take a temp var to comapre it wih last.
num = int(input("Enter the number:"))
temp_num = num
reverse =0
while num>0:
  digit=num%10

  reverse = reverse*10+digit
  num=num//10
print(reverse)

if reverse ==temp_num:
  print("Number is palindrome")
else:
  print("Number is not palindrome")

# 5. Armstrong number.
num_str = input("Enter the number:") # Get input as string
num = int(num_str) # Convert to integer for calculations
length = len(num_str) # Get length from the string
print(length)

sum = 0
original_num = num # Store the original number to compare later
while num > 0:
  digit = num % 10
  sum += digit ** length
  num = num // 10
print(sum)

if sum == original_num: # Compare the sum with the original number
    print("This is an Armstrong number.")
else:
    print("This is not an Armstrong number.")


# 6. LCM using while loop.
num1 = int(input("Enter the  number:"))
num2 = int(input("Enter the number:"))
Greater = 0
Multiplication = num1*num2

if num1>num2:
  Greater = num1
else:
  Greater = num2

i = Greater
while i<= Multiplication:
    if i%num1==0 and i%num2==0:
      LCM = i
    i+=1
print(i)

# 7.count the digit
num = int(input("Enter the number:"))
count = 0
while num>0:
  digit = num%10
  count=count+1
  num = num//10
print(count)

# 8 find all the factor of the number.
import math

def printDivisor(n):
    divisors = []
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n // i)
    for d in sorted(divisors):
        print(d)
# 9. Factorial.
num = int(input("Enter a number:"))
mul = 1
while num>0:
    mul*=num
    num-=1
print(mul)

# 10. single digit .
num = int(input("enter the number:"))
count = 0
while num>0:
    digit = num%10
    num=num//10
    count = digit
    print(count)
 # 11. sum of 1 to 50.
i = 1
sum = 0
while i <=50:
    sum+=i
    i+=1
    print(sum)
# 12. Multiplication.
num = int(input("Enter the number:"))
i = 1
while i<=10:
    print(num,"X",i,"=",num*i)
    i+=1
# 13. 1 to 20.
i = 1
while i<=20:
    if (i%2==0):
        print("Even number 1 to 20:",i)
    i+=1
