#Find the sum of N natural number using  recursion 

def print_sum_of_num(number):
    if number == 1:
        return 1
    return number * print_sum_of_num(number-1)
number = int(input("enter your nth number : "))
result = print_sum_of_num(number)
print(result)