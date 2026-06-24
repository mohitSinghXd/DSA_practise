def selection_sort(nums):
    for i in range(len(nums)):
        min_index = i
        for j in range(i + 1, len(nums)):
            if nums[j] < nums[min_index]:
                min_index = j

        temp = nums[i]
        nums[i] = nums[min_index]
        nums[min_index] = temp

    return nums
nums = [6, 8, 2, 26, 3, 34, 35, 23, 64, 323, 34]
print(selection_sort(nums)) 


"""
complexities::

Best Case    : O(n²)
Average Case : O(n²)
Worst Case   : O(n²)
Space         : O(1)
Swaps         : O(n)
"""