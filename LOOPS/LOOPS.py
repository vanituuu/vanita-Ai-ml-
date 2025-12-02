# While loops

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


