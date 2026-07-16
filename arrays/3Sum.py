

""" 
Brute force with TC-> O(n3)

def Three_Sum(array):
    n = len(array)
    my_set = set()
    for i in range(n):
        for j in range(i+1 , n ):
            for k in range(j+1 , n):
                if array[i] + array[j]+ array[k] ==  0 : 
                    temp  = [array[i] , array[j] ,array[k]]
                    temp.sort()
                    result = tuple(temp)
                    my_set.add(result) 
                    
    return [list(ans) for ans in my_set]   

array =[-1,0,1,2,-1,-4]
ans = Three_Sum(array) 
print(ans)  """


 
 

#Now   we can have a Better approach  by using  only two pointers i and j only for k we will not use loop instead we use simple mathematics k = -(i+j) which will help us to find the exact third required number . And its TC -> O(n2) and SC->O(n) for taking extra set

""" 

def Three_Sum(array):
    n = len(array)
    result_set = set()

    for i in range(n):
        hash_set = set()

        for j in range(i + 1, n):
            third = -(array[i] + array[j])

            if third in hash_set:
                temp = [array[i], array[j], third]
                temp.sort()
                result_set.add(tuple(temp))

            hash_set.add(array[j])

    return [list(ans) for ans in result_set]


array = [-1, 0, 1, 2, -1, -4]
ans = Three_Sum(array)
print(ans)
"""
 
 
# Now we have a more optimal approach 

def threeSum( nums):
        nums.sort()
        n = len(nums)
        result = []

        for i in range(n):

            # Skip duplicate first elements
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left = i + 1
            right = n - 1

            while left < right:

                total = nums[i] + nums[left] + nums[right]

                if total < 0:
                    left += 1

                elif total > 0:
                    right -= 1

                else:
                    result.append([nums[i], nums[left], nums[right]])

                    left += 1
                    right -= 1

                    # Skip duplicate values from the left
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

                    # Skip duplicate values from the right
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

        return result
        
nums = [-1,0,1,2,-1,-4] 
ans = threeSum(nums)
print(ans)


