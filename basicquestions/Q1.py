# return the number of digits in a given number

def  getdigits(number):   
    number = abs(number)
    count = 0  
    if number == 0 :
        return 1 
    while number > 0 : 
        last_digit = number % 10 
        count = count + 1 
        number = number // 10 
    
    return count
    

number = int(input("enter your digit  : ")) 
result = getdigits(number) 
print(result) 


# time complexity = O(log10 n ) because Whenever the input is repeatedly divided by a constant (>1), the time complexity becomes logarithmic. so here in this question we were dividing with 10  , so it becomes log base 10 n 
