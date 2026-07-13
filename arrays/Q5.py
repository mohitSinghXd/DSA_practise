# Right rotate an array with 1 position  
#e.g [1,2,3,4,5,6,7,8,9] after rotation [9,1,2,3,4,5,6,7,8]

def Right_rotate(array):
    n = len(array) 
    last_element = array[n-1]
    for i in range(n-2 , -1 , -1): 
        array[i+1]  = array[i]
        

      
    array[0] = last_element
    print(array)


array = [1,2,3,4,5,6,7,8,9]
Right_rotate(array)