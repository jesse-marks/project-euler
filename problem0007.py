"""
PROJECT EULER problem 7
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10,001st prime number?
"""

# I could check every number up to the 10,001 prime to see if it is a prime. Create a prime list
# and see if each number is divisible by one of the primes. If no then conclude it is a prime
# and add it to the list.

target = 10001
prime_list = [2,3]

increment = 5
while len(prime_list) < target:
    test = [increment % prime == 0 for prime in prime_list if (prime < increment ** (1/2))]

    if not any(test):
        prime_list.append(increment)
    increment += 2

print(prime_list[-1])

