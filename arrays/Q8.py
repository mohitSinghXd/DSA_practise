#linear search in a array


def linear_search(array , target):
    for i in range(len(array)):
        if array[i] == target:
            return i 
    return -1

array = [23,5,3,2,53,64,75,76]
target = int(input("enter your target : ")) 
ans = linear_search(array , target) 
if ans :
    print("target found at index , "  , ans) 
else : 
    print("target not found")