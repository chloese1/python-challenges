import array as arr
a = arr.array('i', [2, 4, 6, 8, 10, 12, 12])

reversed = input("type 1 if you want to revese, press enter if you don't")

if(reversed == ""):

    print("First element:", a[0])
    print("Second element:", a[1])
    print("Third element:", a[2])
    print("Fourth element:", a[3])
    print("Fifth element:", a[4])
    print("Last element:", a[5])

if(reversed == "1"):
    print("Last element:", a[5])
    print("Fifth element:", a[4])
    print("Fourth element:", a[3])
    print("Third element:", a[2])
    print("Second element:", a[1])
    print("First element:", a[0])
