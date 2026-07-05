#find the 2nd largest number from an array 
def get_second_largest(arr):
    if len(arr) < 2:
        return None
    largest = float("-inf")
    second_largest = float("-inf")
    for num in arr:
        # Found a new largest
        if num > largest:
            second_largest = largest
            largest = num
        # Update second largest
        elif largest > num and num > second_largest:
            second_largest = num

    if second_largest == float("-inf"):
        return None

    return second_largest


number = [23, 12, 4, 53, 2, 13, 33, 52]
print(get_second_largest(number))