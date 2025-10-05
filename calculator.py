print("First project of making a calculator"
      "using python programming language")
# Calculator
while True:
    print("Enter 'q' to quit")
    print("Enter 'c' to continue")
    user_input=input("Enter your choice:")
    if user_input=='q':
        print("Exiting the calculator")
        break
    elif user_input=='c':
        print("Continuing the calculator")
        break
a=int(input("Enter first number:")) # 17
b=int(input("Enter second number:")) # 4            
print("Enter 1 for addition")
print("Enter 2 for subtraction")            
print("Enter 3 for multiplication")
print("Enter 4 for division")
print("Enter 5 for modulus")
operation=int(input("Enter your operation:")) # 3
if operation==1:
    print("The addition is:", a+b)      
elif operation==2:
    print("The subtraction is:", a-b)
elif operation==3:
    print("The multiplication is:", a*b)
elif operation==4:
    print("The division is:", a/b)  
elif operation==5:
    print("The modulus is:", a%b)
else:
    print("Invalid operation")

            

