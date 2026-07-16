def strStr( haystack, needle):
        n  =len (heystack)
        m = len (needle)  
        i = 0 
        j  =0 
        k = 0 
        while i<n and j < m :
             if heystack[k] == needle[j]:
                  K +=1
                  j +=1 
             elif heystack[k] != needle[j]: 
                   k +=1 
             
             i +=1
                  
                  
heystack = "sadbutsad"
needle = "sad"
ans = strStr(heystack , needle)
print(ans) 



"""
Its TC can still be optimized 

"""