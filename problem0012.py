"""
PROJECT EULER Problem 12: Python3
"""

def main():

    num_divisors = 0
    nth = 1
    while num_divisors < 500:
        nth += 1
        triangle = nth * (nth + 1) / 2
        num_divisors = count_divisors(triangle)

    print(int(triangle))

def count_divisors(number):
    """O(sqrt(n))"""

    num_divisors = 0
    sqroot = int(number ** (1/2))
    for i in range(1, sqroot+1):
        if number % i == 0:
            if i*i == number: # don't add sqroot twice
                num_divisors += 1
            else:
                num_divisors += 2
    return num_divisors

####################################################################################################
if __name__ == "__main__":
    main()
