def two_sum(array , target):
    n  = len(array)
    my_dict = {}
    
    for i in range(n):
        remaining  = target  - array[i]
        if remaining in my_dict:
            return [my_dict[remaining] , i] 
        else :
            my_dict[array[i]] = i 

array  = [5,9,1,2,4,15,6,3]  
target = 13
ans = two_sum(array , target)
print(ans)