# remove the duplicate elements from an array 


"""def get_result(num):
    mydict = {}

    for x in num:
        if x not in mydict:
            mydict[x] = 1

    unique = list(mydict.keys())

    # In-place overwrite
    for i in range(len(unique)):
        num[i] = unique[i]

    # Remaining positions ko 0 se fill karo
    for i in range(len(unique), len(num)):
        num[i] = 0

    print(num)

num = [1,2,3,3,4,5,5,5,6,7,7,8]
get_result(num) """
 
 
 
 
 
# we have one more optimal approach 


def remove_duplicates(nums):
    if len(nums) == 0:
        return 0

    i = 0

    for j in range(1, len(nums)):
        if nums[i] != nums[j]:
            i += 1
            nums[i] = nums[j]

    return i + 1


nums = [1, 1, 2, 3, 4, 5, 5, 6, 7, 7, 8]

k = remove_duplicates(nums)

print(k)
print(nums)
