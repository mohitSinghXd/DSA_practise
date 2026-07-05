#check weather the array  is sorted or not 

def checkArray(num):  
    is_sorted= True 
    if len(num) ==1:
        return True
    n = len (num)
    for i in range(n-1):
        if num[i] > num[i+1]:
            return False
            
    return is_sorted
    
num = [1,2,4,5,6,8,26,109]
ans = checkArray(num)
print(ans)