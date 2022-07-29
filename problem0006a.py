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

def difference(largest_num):

    sum_squares = largest_num * (largest_num + 1) * (2*largest_num + 1) / 6
    square_sums = (largest_num**2)*((largest_num + 1)**2) / 4
    final_answer =  square_sums - sum_squares
    message  = "\nThe difference between the square of the sum and the sum of the squares \n \
    of the first {} natural numbers is: {}".format(largest_num, final_answer)
    print(message)

####################################################################################################
if __name__ == "__main__":
    main()
