while True:
    print("""
    1)        Power
    2)        Volume
    3)        Channel
    4)        Brighten
    5)        Exit
    """)
    Option=int(input("Enter Option: "))

    if Option==1:
        ans = input("Turn on TV?")
        if ans == "Yes":
            print("TV successfully turned on")
        else:
            print("TV hasn't been turned on")
        break

    if Option==2:
        ans1 = input("What would you like to do? (Up, Down or Mute)")
        if ans1 == "Up":
            print("Volume level raised")

            
    if ans1 == "Down":
        print("Volume level lowered")
    if ans1 == "Mute":
        print("Volume muted")

    if Option==5:
        exit()
