num1 = float(input("Enter a number here: "))
num2 = float(input("Enter another number here: "))

print("1. Addition\n")
print("2. Subtraction\n")
print("3. Multiplication\n")
print("4. Division\n")

choice = int(input("enter a number between 1-4: "))

if choice == 1:
    sum = num1+num2
    print ("the addition of the given two numbers is",sum)
elif choice == 2:
    print ("The subtraction of the given two numbers is",num1-num2)
elif choice == 3:
    print ("The multiplication of the given two numbers is",num1*num2)
elif choice == 4:
    print ("The division of the given two numbers is",num1/num2)
else:
    print ("Invalid Input from the User")