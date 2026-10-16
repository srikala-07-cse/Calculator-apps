def add(a,b):
  return a+b
def subtr(act(a,b):
  return a-b
def multiply(a,b):
  return a*b
def divide(a,b):
  if b==0:
    return "error:cannot divide by zero!"
    return a/b
print("select operation:")
print("1.add")
print("2.subtract")
print("3.multiply")
print("4.divide")
choice=input("enter choice(1/2/3/4):")
num1=float(input("enter first number:"))
num2=float(input("enter second number:"))
if choice=='1':
  print("result:",add(num,num2))
elif choice=='2':
  print("result:",subtract(num1,num2))
elif choice=='3':
  print("result:",multiply(num1,num2))
elif choice=='4':
  print("result:",divide(num1,num2))
else:
  print("invalid input")
  
