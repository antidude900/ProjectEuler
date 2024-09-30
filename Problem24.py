import math

def nth_lexicographic_permutation(n):
    
    letters = list("abcdefghijklm")
    result = []
    n -= 1  # Since index starts from 0 but N is 1-based
    
    for i in range(12, -1, -1):
        # Find the index of the next letter to add
        idx, n = divmod(n, math.factorial(i))
        result.append(letters.pop(idx))
    
    return ''.join(result)

# Input Handling
T = int(input())  # Number of test cases
for _ in range(T):
    N = int(input())
    print(nth_lexicographic_permutation(N))
