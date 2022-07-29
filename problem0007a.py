"""
PROJECT EULER problem 7
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10,001st prime number?
"""
# Sieve of Eratosthenes

# I could check every number up to the 10,001 prime to see if it is a prime. Create a prime list
# and see if each number is divisible by one of the primes. If no then conclude it is a prime
# and add it to the list.

def main():
    target = 100000
    increment = 4

    primes_found = 0
    while primes_found < target:
        s = increment * target
        prime_list = [0,1] # one is not prime and 2 is
        prime_list += [1] * s # a bytearray where each 1 is a prime

        for i in range(2, len(prime_list)):
            prime_list = zero_multiples(i, prime_list)

        increment *= 2
        primes_found = sum(prime_list)

    primes_found = 0
    for j in range(len(prime_list)):
        primes_found += prime_list[j]
        if primes_found == target:
            print(j+1)
            break


def zero_multiples(factor, prime_list):
    """
    Make all multiples of <factor> zero in the bytearray
    """
    for i in range(factor**2, len(prime_list)+1, factor):
        prime_list[(i-1)] = 0
    return prime_list

####################################################################################################
if __name__ == "__main__":
    main()
