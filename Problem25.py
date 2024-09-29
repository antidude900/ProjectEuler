def compute_fibonacci_terms(max_n):
    fib_digits = {}
    a, b = 1, 1
    index = 2
    
    current_digits = 1
    fib_digits[1] = 1
    
    while current_digits <= max_n:
        a, b = b, a + b
        index += 1
        if len(str(b)) > current_digits:
            current_digits = len(str(b))
            fib_digits[current_digits] = index
    
    return fib_digits

def main():
    t = int(input())
    inputs = [int(input()) for _ in range(t)]
    
    max_n = max(inputs)
    fib_digits = compute_fibonacci_terms(max_n)
    
    for n in inputs:
        print(fib_digits[n])

if __name__ == "__main__":
    main()
