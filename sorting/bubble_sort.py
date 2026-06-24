def bubble_sort(nums):
    n = len(nums)
    for i in range(n):
        for j in range(0, n - i - 1):
            if nums[j] > nums[j + 1]:
                temp = nums[j]
                nums[j] = nums[j + 1]
                nums[j + 1] = temp

    print(nums)
nums = [12, 24, 1, 4, 2, 52, 23, 234]
bubble_sort(nums) 




"""

| Case                 | Time Complexity                |
| -------------------- | ------------------------------ |
| **Best Case**        | **O(n)** *(with optimization)* |
| **Average Case**     | **O(n²)**                      |
| **Worst Case**       | **O(n²)**                      |
| **Space Complexity** | **O(1)**                       |


"""