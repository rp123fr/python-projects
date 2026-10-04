def add(num1,num2):
    a=num1+num2
    print(f"sum:{a}")
    
def sub(num1,num2):
    if num1>num2:
        s=num1-num2
        print(f"difference:{s}")
    else:
        s=num2-num1
        print(f"difference:{s}")

def multiply(num1,num2):
    m=num1*num2
    print(f"multiply:{m}")   

def divide(num1,num2):
    d=num1/num2
    print(f"ouotient:{d}")

num1=int(input("enter a number1:"))
num2=int(input("enter a number2:"))
o=input("operations:1.add 2.subtract 3.multiply 4.divide :")

if o=="1":
    add(num1,num2)
elif o=="2":
    sub(num1,num2)
elif o=="3":
    multiply(num1,num2)
elif o=="4":
    divide(num1,num2)
else:
    print("enter from the choices given!")