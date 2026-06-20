# Find all the factors of a given number 


"this is the most optimal soln for finding factors of a number having time complexity of O(√n) which is order of root n "
def getallfactors(number):
    num = number 
    nums_list = []
    i = 1
    while i*i <= num:
        if num % i == 0 : 
         nums_list.append(i)
         second_num = num // i
         if i != second_num:
            nums_list.append(second_num)
        i += 1
    return nums_list

number = int(input("enter your number : "))
result = getallfactors(number)
print(result)




""" 
this is brute force approach which has O(n) tc
def getallfactors(numbers):
    factors_list =[]
    for i in range(0, number + 1):
        if number % i == 0:
            factors_list.append(i) 
        
    
    return factors_list


number  = int(input("enter your number : "))

result  = getallfactors(number)
print(result)

""" 


"""

this is good than brute force but not the most optimal 

def getallfactors(numbers):
    factors_list =[]
    for i in range(0, number // 2):
        if number % i == 0:
            factors_list.append(i) 
        
    
    factors_list.append(number)
    return factors_list


number  = int(input("enter your number : "))

result  = getallfactors(number)
print(result)



"""