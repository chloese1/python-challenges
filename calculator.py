def add(x, y):

    return x + y




def subtract(x, y):

    return x - y




def multiply(x, y):

    return x * y




def divide(x, y):

    return x / y




print ("Please choose an option that you would like ")

print ("1. add")

print ("2. subtract")

print ("3. multiply")

print ("4. divide")

print ("5. add to pi")

print ("6. subtract from pi")

print ("7. multiply by pi")

print ("8. divide by pi")




while True:

    choice = input("Enter choice(1/2/3/4/5/6/7/8): ")




    if choice in ('1', '2', '3', '4', '5', '6', '7', '8'):

        num1 = float(input("Enter first number: "))

        num2 = float(input("Enter second number or any number if you are to use pi: "))

        

    

        if choice == "1":

            print(num1, "+", num2, "=" , add(num1, num2))




        elif choice == "2":

            print(num1, "-", num2, "=", subtract(num1, num2))




        elif choice == "3":

            print(num1, "*", num2, "=", multiply(num1, num2))




        elif choice == "4":

            print(num1, "/", num2, "=", divide(num1, num2))




        elif choice == "5":

            print(num1, "+", 3.14159265359, "=" , add(num1, 3.14159265359))




        elif choice == "6":

            print(num1, "-", 3.14159265359, "=", subtract(num1, 3.14159265359))




        elif choice == "7":

            print(num1, "*", 3.14159265359, "=", multiply(num1, 3.14159265359))




        elif choice == "8":

            print(num1, "/", 3.14159265359, "=", divide(num1, 3.14159265359))




        next_calculation = input("Let's do next calculation? (yes/no): ")

        if next_calculation == "no":

          break

    

    else:

        print("Invalid Input")
