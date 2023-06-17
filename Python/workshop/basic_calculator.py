# Take input from user - num1, num2, operator
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operator = input("Enter operator. available: +, -. *, /:\n")

#if statement for operator 
if operator == "+":
    print(num1 + num2)
elif operator == "-":
    print(num1 - num2)
elif operator == "*":
    print(num1 * num2)
elif operator == "/":
    if num2 !=0:
        print(num1 / num2)
    else:
        print("Error! division by zero is not allowed")
else:
    print("INVALID Operator")
  

