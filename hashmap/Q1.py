# Check Whether Elements of One Array Exist in Another Using Hashing

m = [1,2,4,2,6,4,5,7,8,9,7,6,5,4,3,2,4]
n = [3,23,53,52,23,2,4,2,32,3,5,53,53,6,46,4,26,45,33,645,6,43,54,44,454,664]
def getsoln(m, n):
    freq_dict = {}
    # Build frequency dictionary
    for num in m:
        if num in  freq_dict :
          freq_dict [num] += 1
        else:
            freq_dict [num] = 1
    result = []
    # Check whether each element of n is present in m
    for num in n:
        if num in     freq_dict :
            result.append(1)
        else:
            result.append(0)

    return result


result = getsoln(m, n)
print(result)