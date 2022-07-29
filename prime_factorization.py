"""Prime factorization algorithm: Python3"""

# find all numbers that multiply to 1000.
# prime factorize 1000.


prime_dict = {}
factor_this = 1000

def prime_factorization(number, prime_dict):
    """
    Return a prime factorization dictionary containing
    primes (keys) and the exponents (values).
    """
    if number == 1:
        return prime_dict

    for i in range(2, number+1):
        if (number % i) == 0:
            if i in prime_dict:
                prime_dict[i] += 1
            else:
                prime_dict[i] = 1
            new_number = number // i
            break
    return prime_factorization(new_number, prime_dict)


print(prime_factorization(factor_this, prime_dict))
