password = "1324"

for i in range (3, 0, -1):
    attempt = input("Enter password:")
    if attempt == password:
        break
    else:
        print("Incorrect password")

if i == 1:
    print("You have been denied access")
else:
    print("You have been given access")

print ("""

    1. Register guest arrival

    2. Register a car in the car park

    0.Exit

    """)

ans=input ("what would you like to do ")

if ans=="1":

        item1 = input ("what do you wanna call said item ")

        print (item1+" has been sucefully added ")

elif ans=="2":

        item1 = input ("what is the cars registration plate ")

        print (item1+" has been sucefully added ")

elif ans== "0":

        finish = print("Goodbye")
