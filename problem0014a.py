"""PROJECT EULER Problem 14: Python"""
#Longest Collatz sequence

keep = {}
longest = 0
chief = 0

collatz = list(range(1, 10**6 + 1))
#collatz = list(range(1, 13 + 1))
for j in collatz:
    num = j
    count = 1
    while num != 1:
        if num % 2 == 0:
            num /= 2
        else:
            num = (3 * num) + 1
        if num < j:
            count += keep[num]
            break
        count += 1
    keep[j] = count
    if count > longest:
        longest  = count
        chief = j
    if j % 50_000 == 0:
        print(j)

print(chief, longest)
