"""PROJECT EULER Problem 14: Python"""
#Longest Collatz sequence

def collatz(n):
    if n % 2 == 0:
        return n // 2
    return int(3 * n + 1)

def sequence_length(n):
    seq_length = 1
    start_num = n
    while n != 1:
        n = collatz(n)
        seq_length += 1
    return seq_length, start_num
#print(sequence_length(3)[0])


longest_sequence = 0
longest_number = 0

for j in range(1,1_000_000):
    new_seq = sequence_length(j)[0]
    new_num = sequence_length(j)[1]
    if new_seq > longest_sequence:
        longest_sequence = new_seq
        longest_number = new_num
    if j % 50_000 == 0:
        print(j)

print(longest_number, longest_sequence)
