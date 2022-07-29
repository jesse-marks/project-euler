"""
PROJECT EULER problem 6.
The sum of the squares of the first ten natural numbers is,

1^2 + 2^2 + .  .  .  + 10^2 = 385 

The square of the sum of the first ten natural numbers is,

( 1 + 2 + .  .  .  + 10)^2 = 55^2 = 3025

Hence the difference between the sum of the squares of the first 
ten natural numbers and the square of the sum is 
3025 − 385 = 2640.

Find the difference between the sum of the squares of the first 
one hundred natural numbers and the square of the sum.
"""

def main():
    largest_num = 100
    #sum_of_squares(largest_num)
    #square_of_sum(largest_num)
    difference(largest_num)


def sum_of_squares(largest_num):
    total = 0
    for j in range(largest_num+1):
        total += j**2
    message = "\nThe sum of squares of the first {} natural numbers is: {}".format(largest_num, total)
    print(message)
    return(total)

def square_of_sum(largest_num):
    sum_naturals = 0
    for j in range(largest_num+1):
        sum_naturals += j
    sum_squared = sum_naturals**2
    message = "The square of the sum of the first {} natural numbers is: {}".format(largest_num, sum_squared)
    print(message)
    return sum_squared

def difference(largest_num):
    final_answer =  square_of_sum(largest_num) - sum_of_squares(largest_num)
    message  = "\nThe difference between the square of the sum and the sum of the squares \n \
    of the first {} natural numbers is: {}".format(largest_num, final_answer)
    print(message)

####################################################################################################
if __name__ == "__main__":
    main()