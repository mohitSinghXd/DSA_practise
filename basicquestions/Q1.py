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