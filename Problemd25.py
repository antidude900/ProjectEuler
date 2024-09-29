"""
https://www.hackerrank.com/contests/projecteuler/challenges/euler025/problem
"""

def compute_fibonacci_terms(max_n): #computing all the nth terms of all cases together so that we dont have to start from first for all questions
    fib_digits = {} 
    a, b = 1, 1
    term = 2 #we are at 2nd term
    
    current_digits = 1
    fib_digits[1] = 1

    while current_digits <= max_n:
        a, b = b, a + b
        term += 1
        if len(str(b)) > current_digits:
            current_digits = len(str(b))
            fib_digits[current_digits] = term
    
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
