#frequency map in dictionary 

def get_frequency_of_numbers(my_list):
       my_dict = {} 
       for num in my_list:
           if  num in my_dict:
                my_dict[num] += 1
           else : 
              my_dict[num] = 1 

       return my_dict


my_list = [1,2,4,4,2,2,1,5,6,3,2,1]
result  = get_frequency_of_numbers(my_list) 
print(result) 


"""
Time Complexity: O(n)
Auxiliary Space Complexity: O(n) (worst case) when all the numbers are unique else in average case O(k)
"""