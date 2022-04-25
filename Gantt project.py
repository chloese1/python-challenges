

def main_menu():
    while True:
        print("""
            1.	Enter new Contract
            2.	Display Summary of Contracts
            3.	Display Summary of Contracts for Selected Month
            4.	Find and display Contract
            0.	Exit
            """)

        ans = int(input("What would you like to do? "))
        if ans==1:
            new_contract()
            break

        if ans==2:
            f = open("I:/Documents/contracts.txt", "r")
            print(f.read())
            break
       
        if ans==3:
            print("""
                Contract 1
                Contract 2
                Contract 3
                Contract 4
                       """)
            test = input("0. Go back")
            break

        if ans==0:
            exit()
            break

def new_contract():
    global first_name, package, bundle_type, reference, contract_length, international_calls

    first_name = input("Please enter your name: ")
    package = input("Please enter your package: ")
    bundle_type = input("Please enter your data bundle: ")
    reference = input("Please enter your reference: ")
    contract_length = input("How long do you want this contract: ")
    international_calls = input("Would you like international calls: ")
    print("Contract successfully created")

def top_bottom():
    print("+-----------------------------------------------+")

def blank_line():
    print("|						|")

def display_contract(first_name):
    top_bottom()
    blank_line()
    print("|Customer: " , first_name , "			|")
    print("|Package: " , package , "			|")
    print("|Bundle Type: " , bundle_type , "			|")
    print("|Reference: " , reference , "			|")
    print("|Contract Length: " , contract_length , "			|")
    print("|International Calls: " , international_calls , "			|")
    blank_line()
    top_bottom()

    appent_to_file = first_name , "\t"  , package
    file.write(append_to_file)
    main_menu()


new_contract()
display_contract(first_name)

#main_menu()

def write():
    with open('Contracts.txt', 'a') as file:
        file.write(data + '\n')
        file.close()
