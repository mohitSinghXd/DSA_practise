# Rearrange Array  element by Sign 
def rearrangeArray(self, nums):

        size = len(nums)
        result = [0] * size

        m = 0
        n = 1

        for i in range(size):
            if nums[i] > 0:
                result[m] = nums[i]
                m += 2
            elif nums[i] < 0:
                result[n] = nums[i]
                n += 2

        return result


array = [5, 10, -3, -2, -10, 6]


ans = rearrangeArray(array)

print(ans)