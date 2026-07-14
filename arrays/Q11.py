def get_consecutive_ones(array):
    n = len (array)
    highest_count = 0  
    result  = 0 
  
    for i in range(n):
        if array[i] == 1 :
            highest_count +=1  
        elif array[i] != 1 : 
            result = max(highest_count , result)
            highest_count =  0 
            
        
    return max(result , highest_count)
    
        
    
arrays = [1,1,0,1,0,1,1,1,1,0,1,1]

ans = get_consecutive_ones(arrays) 

print(ans)