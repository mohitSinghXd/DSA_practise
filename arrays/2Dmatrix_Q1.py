def get_transpose(array):
    rows = len(array)
    cols = len(array[0])

    result = [[0] * rows for _ in range(cols)]

    for i in range(rows):
        for j in range(cols):
            result[j][i] = array[i][j]

    print("After transpose")
    for i in range(len(result)):
        for j in range(len(result[0])):
            print(result[i][j], end=" ")
        print()


array = [[1, 2, 3], [4, 5, 6]]

print("Before transpose")
for row in array:
    for num in row:
        print(num, end=" ")
    print()

get_transpose(array)