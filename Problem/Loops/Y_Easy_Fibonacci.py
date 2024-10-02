def print_fibonacci(n):
    if n >= 1:
        fib_sequence = [0]
    if n >= 2:
        fib_sequence.append(1)
    
    for i in range(2, n):
        next_fib = fib_sequence[i-1] + fib_sequence[i-2]
        fib_sequence.append(next_fib)
    
    print(" ".join(map(str, fib_sequence)))


n = int(input())

print_fibonacci(n)
