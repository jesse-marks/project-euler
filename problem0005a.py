"""
2520 is the smallest number that can be divided by each of the
numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible
by all of the numbers from 1 to 20?
"""
def main():
    print("jese")
    top_check = 20
    #prime_list = prime_factorization(top_check,[])
    #greatest_power(prime_list)
    fact_list = factorization_list(top_check)
    final_dict = highest_exponent(fact_list)
    print(multiply_primes(final_dict))


def prime_factorization(number, prime_list):
    """
    start with an empty list
    """
    if number == 1:
        return prime_list

    for i in range(2, number+1):
        if (number % i) == 0:
            prime_list.append(i)
            new_number = number // i
            break
    return prime_factorization(new_number, prime_list)


def greatest_power(prime_list):
    """
    Take a list of primes and return a dictionary of primes raised to their greatest power.
    e.g., [2,2,3] returns {2:2, 3:1}
    """
    prime_dict = {}
    for prime in prime_list:
        if prime not in prime_dict:
            prime_dict[prime] = 1
        else:
            prime_dict[prime] += 1
    return prime_dict


def factorization_list(largest_num):
    """
    Prime factorize every number up to the largest number
    and return a list of each prime factorization

    input = 5
    output = [ {2:1}, {3:1}, {2:2}, {5,1} ]
    """

    prime_list = []
    for i in range(2,largest_num+1):
        prime_dict = greatest_power(prime_factorization(i, []))
        prime_list.append(prime_dict)

    return prime_list

#print(factorization_list(top_check))
# [{2: 1}, {3: 1}, {2: 2}, {5: 1}, {2: 1, 3: 1}, {7: 1}, {2: 3}, {3: 2}, {2: 1, 5: 1}, {11: 1}, {2: 2, 3: 1}, {13: 1}, {2: 1, 7: 1}, {3: 1, 5: 1}, {2: 4}, {17: 1}, {2: 1, 3: 2}, {19: 1}, {2: 2, 5: 1}]


def highest_exponent(prime_diclist):
    """
    take a list of dictionaries and find the dictionary key:value pair that translates to the
    largest prime:exponent pair. Return a final dictionary.
    e.g.,
    input: [{2: 1}, {3: 1}, {2: 2}, {3: 3}]
    output: {2: 2, 3: 3}
    """

    final_dict = {}
    for adict in prime_diclist:
        for key in adict:
            if key not in final_dict:
                final_dict[key] = adict[key]
            elif (final_dict[key] < adict[key]):
                final_dict[key] = adict[key]
    return final_dict


def multiply_primes(final_dict):
    final_product = 1
    for key in final_dict:
        final_product *= (key ** final_dict[key])
    return final_product

##########################################################################
if __name__ == "__main__":
    main()
