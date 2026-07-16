# Find the largest number in an array 


def get_largest_number(number): 
    if len(number) == 0 :
        return
    largest = number[0]
    for i in range( 1, len(number)): 
        if largest < number[i]:
            largest = number[i] 


    print(largest)
        


number = [23,3,5,31,25,53,223 , -500] 
get_largest_number(number)