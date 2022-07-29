""" PROJECT EULER problem 10: Python3 """
# sum of all primes below 2million. Use the Sieve of Eratosthenes

def main():
    """Create a bytearray and use the Sieve of Eratosthenes to find all of the primes"""
    target = 2_000_000
    p_squared = int(target**(1/2)) # don't have to check numbers off beyond this

    prime_list = [0,1] # one is not prime and 2 is
    prime_list += [1] * (target - 2) # a bytearray where each 1 is a prime
    print(len(prime_list))

    for i in range(2, target):
        prime_list = zero_multiples(i, prime_list)
    #print(prime_list)

    prime_sum = 0
    for i in range(len(prime_list)):
        if prime_list[i] == 1:
            prime_sum += (i+1)

    print(prime_sum)



def zero_multiples(factor, prime_list):
    """ Make all multiples of <factor> zero in the bytearray """

    for i in range(factor**2, len(prime_list)+1, factor):
        prime_list[(i-1)] = 0
    return prime_list

####################################################################################################
if __name__ == "__main__":
    main()
