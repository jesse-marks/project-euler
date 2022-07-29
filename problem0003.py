"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""

number = 600851475143
prime_set = set()


def prime_factorization(number, some_set):
    if number == 1:
        return some_set

    for i in range(2, number+1):
        if (number % i) == 0:
            some_set.add(i)
            new_number = number // i
            break
    return prime_factorization(new_number, some_set)



print(prime_factorization(number, prime_set))
print(max(prime_factorization(number, prime_set)))