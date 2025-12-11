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

