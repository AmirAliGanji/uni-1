n = int(input("Enter the number of terms in the Fibonacci sequence: "))
sequence = [0, 1]
for i in range(2, n):
    next_number = sequence[i-1] + sequence[i-2]
    sequence.append(next_number)
print(sequence)