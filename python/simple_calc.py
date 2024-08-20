num1 = int(input("Enter first integer: "))
num2 = int(input("Enter second integer: "))
math = str(input("Enter an operator (+, -, /, or *): "))


if math == "+":
   result = num1 + num2
   print("The Answer is "+str(result))
elif math =="-":
   result = num1 - num2
   print("The Answer is "+str(result))
elif math == "/":
    result = num1/num2
    print("The Answer is "+str(result))
elif math == "*":
   result = num1 * num2
   print("The Answer is " + str(result))
else:
   print("Invalid Operator")


