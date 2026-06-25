def get_sorted_merge_array(array1, array2):
    result = []
    i = 0
    j = 0

    while i < len(array1) and j < len(array2):
        if array1[i] <= array2[j]:
            result.append(array1[i])
            i += 1
        else:
            result.append(array2[j])
            j += 1

    # Remaining elements of array1
    while i < len(array1):
        result.append(array1[i])
        i += 1

    # Remaining elements of array2
    while j < len(array2):
        result.append(array2[j])
        j += 1

    return result


array1 = [2, 3, 5, 7, 8, 9, 12]
array2 = [4, 7, 10, 12, 32, 64, 77]

print(get_sorted_merge_array(array1, array2))