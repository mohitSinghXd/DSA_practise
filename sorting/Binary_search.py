def binary_search(array , target) :
    n= len(array)
    low = 0 
    high = n -1 
    while low < high:
        mid = (low + high)//2 
        if array[mid] == target : 
           return mid
        elif array[mid] < target: 
            low =mid +1 
        else :
            high = mid -1
    return  -1


array = [1,4,6,8,9,23,43,56,77]
ans = binary_search(array ,56) 
print(ans)
