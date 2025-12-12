# Function 
def EvenOdd(x):
  if x%2==0:
    return "Even"
  else:
    return "Odd"

print(EvenOdd(16))
print(EvenOdd(5))

# sum of square of first n natural number:
def square_no(num):
    num = int(input("Enter the number:"))
    if num<0:
        raise ValueError("num not ne non-nehative")
    return(num*(num+1)*(2*num+1))//6
print(square_no("num"))

# sum of number.
def sum():
    sum =0
    n = int(input("enter the number:"))
    for i in range(1,n+1):
        sum+=i
    return(sum)
result = sum()   
print(result)

# sum.
def findSum(n):
    # Using mathematical formula to compute
    # sum of first n natural numbers
    return n * (n + 1) // 2
if __name__ == "__main__":
    n = 5
    print(findSum(n))
  
# perfect number:
def is_perfect(num):
    total = 0
    for i in range(1, num):
        if n % i == 0:   # i is a divisor
            total += i
    return total == num

num = int(input("Enter a number: "))
if is_perfect(num):
    print(num, "is a Perfect Number")
else:
    print(num, "is NOT a Perfect Number")

# Armstrong number.
def is_armstrong(num):
    digits = str(num)              # Convert to string to count digits easily
    power = len(digits)          # number of digits
    total = 0
    for d in digits:
        total += int(d) ** power   # raise each digit to 'power'
    return total == num


num = int(input("Enter a number: "))
if is_armstrong(num):
    print(num, "is an Armstrong Number")
else:
    print(num, "is NOT an Armstrong Number")
  
# strong number.
def strong_num(num):
    original_num = num
    sum = 0
    while num>0:
        digit = num%10
        sum+=math.factorial(digit)
        num=num//10
    return sum == original_num
num = int(input("Enter the number:"))
if strong_num(num):
    print(num,"is a strong no.")
else:
    print(num,"this is not")

# automorphic.
def is_automorphic(num):
    square = num * num
    return str(square).endswith(str(num))  # check if square ends with n

num = int(input("Enter a number: "))
if is_automorphic(num):
    print(num, "is an Automorphic Number")
else:
    print(num, "is NOT an Automorphic Number")
# Hardhed no.
def is_harshad(num):
    digit_sum = sum(int(d) for d in str(n))   # sum of digits
    return n % digit_sum == 0

n = int(input("Enter a number: "))
if is_harshad(n):
    print(n, "is a Harshad Number")
else:
    print(n, "is NOT a Harshad Number")
