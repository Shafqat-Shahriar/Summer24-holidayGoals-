# Python program for searching in 
# unsorting array


def findElement(arr, n, key):
   for i in range (n):
     if (arr[i] == key):
       return i
   return -1

if __name__ == '__main__':
   arr = [12,34, 10,6,40]
   key = 40
   n = len(arr)
   
   index = findElement(arr,n,key)
   if index != -1:
       print("Element found at position " + str(index + 1))
   else:
       print("Element not found ")
