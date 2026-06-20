#check weather a number is palindrome or not 

def check_palindrome(number):
    if number < 0 :
        return False
    num = number  
    result = 0 
    while num != 0 :
        id  = num % 10  
        result = (result*10)+ id 
        num = num//10
    print(result)
    return result == number
number = int(input("enter  your number : "))
result = check_palindrome(number) 
if result == True:
    print("palindrome")

else : 
    print("not palindrome") 
 


# time complexity = o(log 10 (n))  where n = number of digit  
#---------------------------------------------------------------------------------------------------------------------------------------------------------



"""" 
this is also a way but not optimal it takes almost o(n)


def check_palindrome(number): 
    num = number
    reversed_string = "" 
    for i in range(len(num)):
        reversed_string  = num[i] + reversed_string 
    return reversed_string  == num


number = input("enter your number : " )

result = check_palindrome(number) 
print(result)

"""