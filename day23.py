import math

def summ(x, y) :
    print (x + y)

def mul(x, y) :
    print (x*y)

def div(x, y) :
    if y == 0 :
        print("No division by zero could happen")
    else:
        print (x/y)

def minus(x,y) :
    print (x-y)

def pow(x,y) :
    print (x^y)

def fact(x) :
    print (math.factorial(x))
while 1 :

    cont = input("Do you want to continue ?")
    if cont == 'end' :
        exit()
    else:

        num1 = int (input("Please enter the first number :"))
        num2 = int (input("Please enter the second number :"))

        operator = input("Enter the operation symbol")

        if operator == '+' :
            summ(num1, num2)

        elif operator == '-' :
            minus(num1, num2)

        elif operator == '*' :
            mul(num1, num2)

        elif operator == '/' :
            div(num1, num2)

        elif operator == '^' :
            pow(num1, num2)

        elif operator == '!' :
            fact(num1)











