#Right rotate and array with k position 

def Right_rotate(array , position):
    n = len(array) 
    for i in range(0 , position):
        last_element = array[n-1]
        for j in range(n-2 , -1 ,-1):  
            array[j+1] = array[j]
             
        array[0] = last_element
    print(array)        
 
   

array = [1,2,3,4,5,6,7,8,9]
position = int(input("enter kth value : ")) 
Right_rotate(array , position)
 
# Optimal approach is 
"""
def reverse(arr, start, end):
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1


def right_rotate(arr, k):
    n = len(arr)
    k = k % n

    # Reverse entire array
    reverse(arr, 0, n - 1)

    # Reverse first k elements
    reverse(arr, 0, k - 1)

    # Reverse remaining elements
    reverse(arr, k, n - 1)

    print(arr)


array = [1,2,3,4,5,6,7,8,9]
k = int(input("Enter k: "))
right_rotate(array, k)
"""