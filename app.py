

def selection_sort(number):
    n = len(number)
    for i in range(n):
        min_index = i 
        for j in range(i+1 , n):
            if number[j] < number[min_index]:
                min_index  = j 
                
        temp = number[min_index]
        number[min_index] = number[i]
        number[i]  = temp
        
    print(number)
number = [13,34,23,52,12,53]
selection_sort(number)