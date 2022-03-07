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

balance=2400

while True:
    print("    CASH MACHINE    ")
    print("""
    1)        Balance
    2)        Withdraw
    3)        Deposit
    4)        Quit


    """)
    Option=int(input("Enter Option: "))

    if Option==1:
        print("Balance  £ ",balance)


    if Option==2:
        print("Balance  £  ",balance)
        Withdraw=float(input("Enter Withdraw amount £ "))
        if Withdraw>0:
            balance=(balance-Withdraw)
            print("Balance  £ ",balance)
        if Withdraw>balance:
            print("insufficent funds in account")
        else:
            print("None withdraw made")

    if Option==3:
        print("Balance  £ ",balance)
        Deposit=float(input("Enter deposit amount £ "))
        if Deposit>0:
            balance=(balance+Deposit)
            print("balance  £ ",balance)
        else:
            print("No deposit made")


    if Option==4:
        exit()


