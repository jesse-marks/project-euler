"""
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.
"""

max_num = 1000 
mult1 = 3
mult2 = 5
sum_naturals = 0

for i in range(1, max_num):
    if (i % mult1 == 0) or (i % mult2 == 0):
        #print(i)
        sum_naturals += i

print(sum_naturals)
