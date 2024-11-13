# python Program to Insert an element
# at a specific position in an Array


def insertElement(arr, n, x, pos) :
    
    # shift elements to the right
    # which are on the right side of pos
    for i in range(n-1,pos-1,-1) :
        arr[i + 1] = arr[i]
        
    arr[pos] = x

# Driver's code
if __name__ == '__main__':
    # Declaring array and key to delete
    # here -1 is for empty space
    arr = [2, 4, 1, 8, 5, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]
    n = 5
    
    print("Before insertion : ")
    for i in range(0,n) :
        print(arr[i],end=' ')

    print("\n")

    x = 10;
    pos = 2;
  
    # Function call
    insertElement(arr, n, x, pos);
    n+=1

    print("After insertion : ")
    for i in range(0,n) :
        print(arr[i],end=' ')


"""
#####################################################################################
                      Using dynamic listing
#####################################################################################

# Python program to insert an element at a specific position in a list

def insert_element(arr, x, pos):
    # Check if position is valid
    if pos < 0 or pos > len(arr):
        print("Error: Position out of range")
        return arr
    
    # Insert the element at the specified position
    arr.insert(pos, x)
    return arr

# Driver code
if __name__ == '__main__':
    arr = [2, 4, 1, 8, 5]  # Initial array
    x = 10  # Element to insert
    pos = 2  # Position at which to insert the element
    
    print("Before insertion:", arr)
    arr = insert_element(arr, x, pos)
    print("After insertion:", arr)


"""

"""

################################

When to Use Each Approach

################################


Original Code (Fixed-Size Array with Manual Shifting):

Suitable for scenarios where memory is constrained or needs to be pre-allocated.
Useful in low-level programming languages (e.g., C/C++) that lack dynamic resizing.
Better if you need to control exactly where each element is stored in memory.



Revised Code (Dynamic List Using insert()):

Ideal for general-purpose applications in Python where ease of use and readability are priorities.
Excellent when working with dynamic lists, as Python handles memory allocation and resizing.
Recommended if you’re prioritizing code readability and error handling over manual memory control.


In summary, the revised code is more suited to Python’s strengths, making it more robust, readable, 
and flexible for typical use cases. The original code style is less Pythonic and may be more appropriate 
for low-level programming, but it doesn’t take full advantage of Python’s capabilities.

""""
