# Sort colors
#given that [0,1,0,1,2,2,1,0,1,0,2]-> [0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 2]

def get_soln(array):
    n = len(array)
    start = 0 
    middle  = 0 
    end = n - 1 
    while middle <= end:
        if array[middle] == 2 :
            array[middle] , array[end] = array[end] , array[middle]
            end -= 1
        elif array[middle] == 0 :
            array[middle] ,array[start] = array[start]  , array[middle]  
            middle +=1 
            start +=1
            
        elif array[middle] == 1:
            middle +=1

   
    print(array)



array = [0,1,0,1,2,2,1,0,1,0,2]
get_soln(array)

""" 
This one is Brute force its also taking O(n) TC  but its talking extraspace for dict


def get_soln(array):
    n = len (array)
    my_dict  = {}
    for i in range(n):
        my_dict[array[i]]  = my_dict.get(array[i] , 0) + 1
    
    for i in range(0 , my_dict[0]):
        array[i]  = 0
        
    for i in range(my_dict[0]  , my_dict[0]+ my_dict[1]):
        array[i] = 1
        
    for j in range(my_dict[0] + my_dict[1] , n ):
         array[j]  = 2
         
    print(array)

array = [0,1,0,1,2,2,1,0,1,0,2]
get_soln(array)"""