#Create a tuple with different data types
tuplex = ("tuple", False, 3.2, 1)
print(tuplex)

tup = ('e', 'x', 'e', 'r', 'c', 'i', 's', 'e', 's')
str =  ''.join(tup)
print(str)

tuplex = ("w", 3, "r", "e", "s", "o", "u", "r", "c", "e")
print("r" in tuplex)
print(5 in tuplex)

values = input("Input some comma seprated numbers : ")
list = values.split(",")
tuple = tuple(list)
print('List : ',list)
print('Tuple : ',tuple)
