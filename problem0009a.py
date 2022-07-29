"""Problem 9 PROJECT EULER: Python3"""

# Use Euclid's formula to find Pythagorean triple where a + b + c = 1000
# m > n > 0
# a=m**2 - n**2,   b=2mn,   ,c=m**2 + n**2
# a + b + c = 1000 ==> m**2 + mn = 500



for i in range(500):
    for j in range(500):
        m = i
        n = j
        rules = [ m**2 + m*n == 500,
                  m > n
                ]
        if all(rules):
            a = m**2 - n**2
            b = 2*m*n
            c = m**2 + n**2
            break

answer = a * b * c
message = "The product of abc is: {}".format(answer)
print(message)
