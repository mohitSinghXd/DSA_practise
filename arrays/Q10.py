# Find the missing number from an array 
# e.g  array -> [1,2,6,4,0,5] its length is 6 but missing number is 3  



def find_missing_numbers(array):
    n = len(array) 
    sum_of_n_natural_numbers = (n*(n+1))/2 
    
    total_sum = 0 
    for i in range(n):
        total_sum += array[i] 
        
    return sum_of_n_natural_numbers -  total_sum



array = [1,2,6,3,0,5] 

ans = find_missing_numbers(array)  
print(ans)





"""def find_missing_numbers(array):
    my_dict= {}
    n = len(array)
    for i in range(0, n+1): 
        my_dict[i] = 0 
        
    for i in range(n):
        my_dict[array[i]]   = 1 
        
    
    for k , v in my_dict.items():
        if v == 0 :
            return k 
    print(mydict)

array = [1,2,6,3,0,5] 
ans = find_missing_numbers(array) 
print(ans) """



