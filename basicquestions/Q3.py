# Check weather the number is armstrong number or not 
def check_armstrong(number): 
    count =  0 
    num = number 
    if num == 0:
     return true
    total = 0 
    while num!= 0:
        count = count+1 
        num  = num //10 
    newnum = number
    while newnum != 0:
        last_digit = newnum % 10 
        calculated_value  = last_digit ** count
        total = total + calculated_value 
        newnum = newnum //10
    return total == number
number = int(input("enter your number : "))
result = check_armstrong(number)  
print(result)
if result == True :
    print("yes its armstrong")
else :
    print("no its not armstrong number")

"""
its time complexity becomes O(n) because sequential loops gets added O(n) + O(n) = O(2n) which is O(n)
"""
