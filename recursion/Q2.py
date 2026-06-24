#fibonacci using recursion 
 
def fibonacci_series(first_number, second_number, target):
    if target == 0:
        return []
    return [first_number] + fibonacci_series(second_number,first_number + second_number, target - 1)


first_number = int(input("Enter your 1st number: "))
second_number = int(input("Enter your 2nd number: "))
target = int(input("Enter your target: "))

print(fibonacci_series(first_number, second_number, target))