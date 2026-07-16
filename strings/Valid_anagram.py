"""
def valid_anagram(str1,str2):
    n = len(str1)
    m = len(str2)
    if  n != m :
        return False
    my_dict1  = {} 
    my_dict2 = {}
    for i in range(n): 
        my_dict1[str1[i]] = my_dict1.get(str1[i] , 0) +1  
        
    print(my_dict1)
    
    for i in range(m): 
        my_dict2[str2[i]] = my_dict2.get(str2[i] , 0) +1 
   
        
    if my_dict1 == my_dict2 :
        return True
    else :
        return False



str1 = "mohit"
str2 = "ohitm"
ans = valid_anagram(str1 , str2) 
print(ans) 


This is not optimal because here we are taking two dict  , In optimal soln we can do this in only one dict 



""" 


def valid_anagram(str1,str2):
    n = len(str1)
    m = len(str2) 
    is_anagram =True
    if  n != m :
        return False
    my_dict1  = {} 
   
    for i in range(n): 
        my_dict1[str1[i]] = my_dict1.get(str1[i] , 0) +1  
        
    
    for i in range(m): 
        my_dict1[str2[i]] = my_dict1.get(str2[i] , 0) - 1 
   
        
    for k , v in my_dict1.items():
        if v == 0 :
            continue
        else : 
            return False
    return is_anagram


str1 = "mohit"
str2 = "ohitm"
ans = valid_anagram(str1 , str2) 
print(ans)


