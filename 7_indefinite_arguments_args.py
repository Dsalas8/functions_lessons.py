#1
def tea_order(customer_name, tea_type, **kwargs):
    print(customer_name , "ordered a" , tea_type, "tea")
    for key, value in kwargs.items():
        print("  - Add", key, ":", value)


print(tea_order("Alice", "chamomile"))
print(tea_order("Bob", "Black", milk="oat"))
print(tea_order("Tony", "black", milk="oat", sweetener="honey"))
# -- - -- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -  - - - - - - - - - - - - - 
#THIS USES ARGS AND KWARGS AT THE SAME TIME 

def tea_order(customer_name, tea_type, *args, **kwargs):
    print(customer_name , "ordered a" , tea_type, "tea")
    for key, value in kwargs.items():
        print("  - Add", key, ":", value)


print(tea_order("Alice", "chamomile"))
print(tea_order("Bob", "Black", milk="oat"))
print(tea_order("Tony", "black", "oat", sweetener="honey"))






# Indefinite Arguments (*args) Practice #1
# Create a function called sum_squares that takes any number of numeric arguments, and returns the sum of their values squared.

# For example for the arguments sum_squares(1,2,3) it should return 14 (1+4+9).
def sum_squares(*args):   
    sum = 0                 #Initialize sum at 0 
    for num in args:        # Iterate through each arguement 
        sum+= num ** 2      # square the number and add it to the sum 

    return sum 
print(sum_squares(1,2,3))

# Indefinite Arguments (*args) Practice #2
# Create a function called absolute_sum, which takes any number of arguments, and returns the sum of their absolute values (that is, it takes the non-negative values and adds them together, in other words, considers them all - negative and positive - as positive).
def absolute_sum(*args):
    total = 0 
    for num in args: #Iterate through each arguement 
        total += abs(num) # Add the absolute value of the numbers
    return total 
print(absolute_sum(-1, -2, -3))
# Indefinite Arguments (*args) Practice #3
# Create a function called personal_numbers that receives, as its first argument, a name, and then an indefinite number of values.

# The function should return the following message:

# "{name}, the sum of your numbers is {sum_numbers}"
name = john
def personal_numbers(name, *args):
    total = 0 
    for num in args:
        sum += num 
    return args
print({name}, "the sum of your numbers is" sum)