def linearsearch(arr, x):
   for i in range(len(arr)):
      if arr[i] == x:
         return i
   return -1
arr = [1,2,3,4,5,6,7,8]
x = 4
print("element found at index "+str(linearsearch(arr,x)))


def find_index(elements,value):
    for index, element in enumerate(elements):
        if element == value:
            return index
