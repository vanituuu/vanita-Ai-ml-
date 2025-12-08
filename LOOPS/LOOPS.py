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
