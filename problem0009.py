"""Problem 9 PROJECT EULER: Python3"""

# find all numbers that add to 1000. 

possible_triplets = []
sum_to = 1000

def is_whole(n):
    return n % 1 == 0

for i in range(sum_to):
    for j in range(sum_to):
        a = i
        b = j
        c = (a**2 + b**2)**(1/2)

        rules = [a < b,
                 b < c,
                 is_whole(c),
                 a + b + int(c) == sum_to]
        if all(rules):
            c = int(c)
            possible_triplets.append((a,b,c))

print(possible_triplets)

def largest_product(tuple_list):
    largest_product = 0
    for mytuple in tuple_list:
        print(mytuple)
        tuple_product = 1
        for element in mytuple:
            tuple_product *= element
        if tuple_product > largest_product:
            largest_product = tuple_product

    message = "The product of the Pythagorean triplet is: {}".format(largest_product)
    print(message)
    return largest_product

largest_product(possible_triplets)
