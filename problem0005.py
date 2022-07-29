"""
2520 is the smallest number that can be divided by each of the
numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible
by all of the numbers from 1 to 20?
"""

def divisible_byall(possible_num, check_nums):
    """
    take a large number (possible_num)
    and see if a range of numbers (check_nums)
    can divide the larger number without any remainder
    """

    for j in range(check_nums):
        if possible_num % j:
            return False
    return True

top_check = 20
start_num = top_check * (top_check - 1)
keep_going = True
while keep_going:
    start_num += 1
    keep_going = not divisible_byall(start_num, top_check)

print(start_num)
