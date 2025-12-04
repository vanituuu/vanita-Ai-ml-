# String  
str1 = "Vanshika"
print(str1[0])
print(str1[4])
print(str1[0:3:2])
print(str1[-5:-1])
print(str1[-1:-5])
print(str1[-5:])#if want last no. include.if we add last index it will not gave a last number:
print(str1[::-2])#it wil take 2,2 gap from last.

# palindrome.
num = 12344321
num1 = str(num)
reverse = (num1[::-1])
if num1==reverse:
  print("This is palidrome.")
  Average =num/2
  print("average",Average)
else:
  print("this is not palidrome")

# string1
str1 = "Vanshika"
reverse = (str1[::-1])
if str1 == reverse:
  print("This is palindome",reverse)
else:
  print("This is not ")
  
# Reverse
name = "vanita"
reverse = ""
for char in name:
  reverse = char+reverse
print(reverse)

# Count total number of a character
name = "vanita"
x ="a"
count = 0
for char in name:
  if char==x:
    count+=1
print(count)

# string strip.
name = " Hello World "
print(name)
print(name.strip())
print(name.replace(" ",""))
print(name.replace("Hel","Goo"))

print(name.startswith("H"))
print(name.endswith("z"))





