# Merge 2 sorted arrays


def merge_2_sorted_array(array1 ,array2): 
    n = len(array1)
    m = len(array2)
    i = 0 
    j =0
    result = []
     
    while i < n and j < m :
        if array1[i] <= array2[j]:
            if len(result) == 0 or result[-1] != array1[i]:
                result.append(array1[i]) 
            i +=1 
        else:
            if len(result) == 0 or result[-1] != array2[j]:
                result.append(array2[j])
                
            j +=1
                      
        
        
    while i < n :
        if len(result) == 0 or result[-1] != array1[i]:
                result.append(array1[i]) 
        i +=1 
            
    while j < m :
        if len(result) == 0 or result[-1] != array2[j]:
                result.append(array2[j])
                
        j +=1 
        
        
    print(result)
array1  = [1,2,3,3,4,5]
array2 = [2,3,4,6,7,8]  

merge_2_sorted_array(array1 , array2) 