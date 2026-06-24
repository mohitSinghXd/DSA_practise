#Print name n times using recursion 

number_of_times= int(input("enter your number  : "))
name = input("enter your name: ") 

def recursive_function(number_of_times , name):
     if number_of_times ==  0:
         return
     else:
         print("hii sir , {}".format(name)); 
         recursive_function(number_of_times-1 , name)

recursive_function(number_of_times  , name)