#move 0s to the end of the array 


def move_zeroes(array):
    j = 0  # Position where the next non-zero element should be placed 
    

    for i in range(len(array)):
        if array[i] != 0:
            array[i], array[j] = array[j], array[i]
            j += 1
 
 
    print(array)

array = [2, 43, 0, 3, 0, 23, 0, 43, 0, 3, 23, 0]
move_zeroes(array)









"""
def move_zeroes(array):
    result = []

    for i in range(len(array)):
        if array[i] != 0:
            result.append(array[i])

    for i in range(len(array)):
        if i < len(result):
            array[i] = result[i]
        else:
            array[i] = 0

    print(array)


array = [2,43,0,3,0,23,0,43,0,3,23,0]
move_zeroes(array)

"""