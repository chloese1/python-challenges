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

from array import *
array_num = array('i', [2, 4, 6, 8, 10, 12, 12])
print("Original array: "+str(array_num))
print("Number of occurrences of the number 12 in the array: "+str(array_num.count(12)))

from array import *
array_num = array('i', [2, 4, 6, 8, 10, 12, 12])
print("Original array: "+str(array_num))
print("Remove the third item form the array:")
array_num.pop(2)
print("New array: "+str(array_num))

from array import *
array_num = array('i', [2, 4, 6, 8, 10, 12, 12])
print("Original array: "+str(array_num))
print("Current memory address and the length in elements of the buffer: "+str(array_num.buffer_info()))
print("The size of the memory buffer in bytes: "+str(array_num.buffer_info()[1] * array_num.itemsize))
