"""
This first prints the numbers divisible by 7 and 3
"""

"""
num_range is the range of numbers between 1 and 100
You can set it to be any range num_range = 200, 1000. 
"""

def divisible_seven_three(num_range):
    print("Those divisible by 7 and 3 are:")    
    for num in range(num_range):
        # checks for numbers divisible by 7 and 3
        if num % 3 == 0 and num % 7 == 0:
            print(num)
        else:
            pass 

def divisible_seven(num_range):
    print("Those divisible by 7 alone are:")    
    for num in range(num_range):      
        # checks for numbers divisible by 7 but not 3
        if num % 7 == 0 and num % 3 != 0:
            print(num)
        else:
            pass

def odd_divisible_seven(num_range):
    print("Those odds numbers divisible by 7 but not 3 are:")    
    for num in range(num_range): 
        # checks for odd numbers divisible by 7 but not 3   

        if (num%2) != 0  and num % 7 == 0 and num % 3 != 0:
            print(num)
        else:
            pass

def divisible_digits_sum(num_range):
    print("The numbers that are divisible by the sum of their digits are:")
    sum_digits = 0
    for num in range(1,num_range):
        temp = num
        while num>0:
            digit = num % 10
            sum_digits += digit
            num = num // 10
        if (sum_digits % temp == 0):
            print(temp)
        else:
            pass
"""
numbers that are equal to the square of the sum of its digits are called happy numbers.
For example if we have 13, the sum of the square of the digits is:
Sum of digits is 1 + 3 = 4
square of sum of digits = 4^2 = 16
13 is not equal to 16
"""

def number_square_sum_digits(num_range):
    print("The numbers that are divisible by the sum of their digits are:")
    square_sum_digits = 0
    sum_digits = 0
    for num in range(1,num_range):
        temp = num
        while num>0:
            digit = num % 10
            sum_digits += digit
            num = num // 10
        square_sum_digits = sum_digits*sum_digits
        # print(square_sum_digits)
        if (square_sum_digits == temp):
            print(temp)
        else:
            pass
    


# define the range and call the functions

if __name__ == "__main__":
    num_range = 1000
    # divisible_seven_three(num_range=num_range)
    # divisible_seven(num_range=num_range)
    # odd_divisible_seven(num_range=num_range)
    # divisible_digits_sum(num_range=num_range)
    number_square_sum_digits(num_range=num_range)

