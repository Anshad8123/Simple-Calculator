print("Select any operation to perform: ")
print("1. ADD")
print("2. SUBTRACT")
print("3. MULTIPLY")
print("4. DIVIDE")
operation = input()

if operation == "1":
     num1 = input("Enter first number: ")
     num2 = input("Enter second number: ")
     print("The sum is " + str(int(num1) + int(num2)))

elif operation == "2":
     num1 = input("Enter first number: ")
     num2 = input("Enter second number: ")
     print("The Difference is " + str(int(num1) - int(num2)))
elif operation == "3":
     num1 = input("Enter first number: ")
     num2 = input("Enter second number: ")
     print("The Product is " + str(int(num1) * int(num2)))
elif operation == "4":
     num1 = input("Enter first number: ")
     num2 = input("Enter second number: ")
     print("The Result is " + str(int(num1) / int(num2)))
else:
     print("Invalid Entry")