def findDuplicate( nums):
        n = len (nums)
        mydict = {}
        for i in range(0,n):
            mydict[nums[i]] = mydict.get(nums[i] , 0  ) + 1

        for k, v in mydict.items():
            if v >1 :
                return k 
           
           
           
           
           
array = [1,3,2,4,5,3]  
ans = findDuplicate(array)
print(ans)