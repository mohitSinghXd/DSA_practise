
def longest_substring_without_repeating(string):
    n = len(string) 
    maxi = 1 
    for i in range(n): 
        
        myset = set()
        for j in range(i , n):
            
            if string[j] in myset:
                break
            else: 
                maxi = max (maxi , j - i +1) 
                myset.add(string[j]) 
                
    return maxi
                
                
string  = "CADBZABCD" 
result  = longest_substring_without_repeating(string)  
print(result)
