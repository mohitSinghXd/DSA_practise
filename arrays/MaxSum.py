# Max subarray sum (kadane's algorithm)


def get_max_sum(array):
    n = len(array) 
    maxi = float("-inf")
    total = 0
    for i in range(n): 
        total = total + array[i]
        maxi = max(total , maxi)
        
        if total < 0 :
            total = 0 
            
    return maxi

array = [-2,1,3,4,-1,2,1,-5,4]
ans = get_max_sum(array)
print(ans)