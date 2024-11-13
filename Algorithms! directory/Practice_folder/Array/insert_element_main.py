# Python program for inserting
# an element in unsorted array

# method to insert element


def insertEnd(arr, elment):
   arr.apend(element) 


# Driver's code
if __name__ == '__main__':
   # declaring array and key to insert
   arr  = [12, 16, 20, 40, 50, 70]
   key = 26

   # array before inserting an element
   print("Before Inserting: ")
   print(arr)

   # array after Inserting element 
   insertEnd(arr, key)
   print(arr)
