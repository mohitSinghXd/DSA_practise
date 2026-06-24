#Check Whether charcter of an array  Exist in string Using Hashing 

def get_answer(char_array , name):
    freq_dict = {}
    for ch in name: 
        if ch in freq_dict:
            freq_dict[ch] += 1 
        else:
            freq_dict[ch]  = 1
    # now check in array 
    result= []
    for element in char_array:
        if element in  freq_dict:
            result.append(1)
        else:
            result.append(0)
    return result

name="mohitsingh"
char_array = ["m" , "o" , "j" , "i" , "t"] 

result = get_answer(char_array  ,name) 
print(result)