print("---Simple Python Calculator---")
print("1. Add (+)")
print("2. Subtract(-)")
print("3. Multiply (*)")
print("4. Division")
choice= input("Enter choice 1/2/3/4 ")
num1= float(input("Enter the first number "))
num2= float(input("Enter the second number 1"))
if choice == '1':
    print("Result=",num1+num2)
elif choice =='2':
    print("Result=", num1-num2)
elif choice =='3':
    print("Result=", num1*num2)
elif choice =='4':
    if(num2!=0):
        print("Result=", num1/num2)
    else:
        print("ERROR")
else:
    print("Invalid Choice")




 
