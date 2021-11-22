import array as arr
a = arr.array('i', [apple, banana, cherry, kiwi, mango])

reversed = input("type 1 if you want to revese, press enter if you don't")

if(reversed == ""):

    print("First element:", a[apple])
    print("Second element:", a[banana])
    print("Third element:", a[cherry])
    print("Fourth element:", a[kiwi])
    print("Fifth element:", a[mango])

if(reversed == "1"):
    print("Fifth element:", a[mango])
    print("Fourth element:", a[kiwi])
    print("Third element:", a[cherry])
    print("Second element:", a[banana])
    print("First element:", a[apple])
