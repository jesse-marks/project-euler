"""
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

def is_palindrome(num):
    forward_num = str(num)
    backward_num = forward_num[::-1]
    return forward_num == backward_num

largest_pal = 0
for i in range(100, 999):
    for j in range(100,999):
        possible_pal = i * j
        if possible_pal > largest_pal:
            if is_palindrome(possible_pal):
                largest_pal = possible_pal

print(largest_pal)

