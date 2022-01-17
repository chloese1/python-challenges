while True:
    print("""
        1. Power Tools
        2. Power Tools Accessories
        3. Hand Tools
        4. Tool Storage
        5. Measuring Tools
        6. Testing Equipment
        7. Heating and Plumbing
        8. Electrical and Lighting

        """)

    ans=input ("What would you like to buy ")
    if ans=="1":
            item1 = print("""
                A.Drill £24.99         1234567  8
                B.Sanding belt £199.99 2345678  1
                C.Circular Saw £199.99 3456789  3
                D.Exit
                """)
            item1=input ("Which power tool would you like to buy ")
            if item1=="A":
                print ("You have succefully purchased a "+item1)
            elif item1=="B":
                print ("You have succefully purchased a "+item1)
            elif item1=="C":
                print ("You have succefully purchased a "+item1)
    elif ans=="2":
            print("""
                A.Drill bit £24.99         0467890  8
                B.Sanding belt 12 grain belt £199.99 2345678  1
                C.Circular Saw Blade £199.99 3456789  3
                D.Exit
                """)
            ans=input ("Which power tool would you like to buy ")
            if ans=="A":
                    ans = input ("You have succefully purchased a drill bit -£24.99 ")

            if ans=="B":
                    ans = input ("You have succefully purchased a sanding belt 12 grain belt -£199.99 ")

            if ans=="C":
                    ans = input ("You have succefully purchased a circular saw blade -£199.99 ")



    elif ans=="3":
            print("""
                A.Wrench                      £24.99         0467890  8
                B.Screwdriver                 £199.99        2345678  1
                C.Hammer                      £199.99        3456789  3
                D.Exit
                """)
            ans=input ("Which power tool accessories would you like to buy ")
            if ans=="A":
                    print ("You have succefully purchased a Wrench")
            elif ans=="B":
                    print ("You have succefully purchased a Screwdriver")
            elif ans=="C":
                    print ("You have succefully purchased a Hammer")
            elif ans=="D":
                break


    elif ans=="4":
            print("""
                A.Tool box                    £24.99         0467890  8
                B.Tool drawer                 £199.99        2345678  1
                C.Tool cupboard               £199.99        3456789  3
                D.Exit
                """)
            ans=input ("Which power tool accessories would you like to buy ")
            if ans=="A":
                    print ("You have succefully purchased a Tool box")
            elif ans=="B":
                    print ("You have succefully purchased a Tool drawer")
            elif ans=="C":
                    print ("You have succefully purchased a Tool cupboard")
            elif ans=="D":
                break


    elif ans=="5":
            print("""
                A.Ruler                      £24.99         0467890  8
                B.level checker              £199.99        2345678  1
                C.Tape measure               £199.99        3456789  3
                D.Exit
                """)
            ans=input ("Which power tool accessories would you like to buy ")
            if ans=="A":
                    print ("You have succefully purchased a Ruler")
            elif ans=="B":
                    print ("You have succefully purchased a Level Checker")
            elif ans=="C":
                    print ("You have succefully purchased a Tape measure")
            elif ans=="D":
                break
    elif ans=="6":
            print("""
                A.Circuit detector           £24.99         0467890  8
                B.Metal detector             £199.99        2345678  1
                C.Motion detector            £199.99        3456789  3
                D.Exit
                """)
            ans=input ("Which power tool accessories would you like to buy ")
            if ans=="A":
                    print ("You have succefully purchased a Circuit detector")
            elif ans=="B":
                    print ("You have succefully purchased a Metal detector")
            elif ans=="C":
                    print ("You have succefully purchased a Motion detector")
            elif ans=="D":
                break
    elif ans=="7":
            print("""
                A.Plunger                    £24.99         0467890  8
                B.Thermometor                £199.99        2345678  1
                C.U bend pipe                £199.99        3456789  3
                D.Exit
                """)
            ans=input ("Which power tool accessories would you like to buy ")
            if ans=="A":
                    print ("You have succefully purchased a Plunger")
            elif ans=="B":
                    print ("You have succefully purchased a Thermometor")
            elif ans=="C":
                    print ("You have succefully purchased a U bend pipe")
            elif ans=="D":
                break
    elif ans=="8":
            print("""
                A.Wires                       £24.99         0467890  8
                B.Square light                £199.99        2345678  1
                C.3 inch screw                £199.99        3456789  3
                D.Exit
                """)
            ans=input ("Which power tool accessories would you like to buy ")
            if ans=="A":
                    print ("You have succefully purchased a Wires")
            elif ans=="B":
                    print ("You have succefully purchased a Square light")
            elif ans=="C":
                    print ("You have succefully purchased a 3 inch screw")
            elif ans=="D":
                break




