"""
Same as Problem10.py, just optimized it for multiple test cases
"""

"""
When doing this question, I got to a big problem. There were 7 test cases in total. Out of 7, 5 of them were solved but 2 of them exceeded time limit. 
I tried optmizing the code as much as I can but still 6 and 7 never solved. Then seeing the discussion section, I found out the mistake.

The problem was that for every test case I was making a sieve array from start. The efficient way was to find the maximum N among all the test cases
and make a sieve array of that maximum. In this way, ewe can use the same sieve array for all test cases saving time.

As this is the same algorithm problem 7 uses, try understanding by yourself (>ᴗ•) 
"""

def sieve_of_eratosthenes(max_n):
    is_prime = [True] * (max_n + 1)

 
    for i in range(2, int(max_n**0.5) + 1): 
        if is_prime[i]:
            for j in range(i * i, max_n + 1, i):
                is_prime[j] = False  

    return is_prime

def main():

    t = int(input())  # Read number of test cases
    test_cases = [int(input()) for _ in range(t)]  # Read input values
    max_n = max(test_cases)  # Find the maximum n

    
    is_prime = sieve_of_eratosthenes(max_n)
    prime_sums = [0] * (max_n + 1)
    sum_primes = 0

    
    for i in range(2, max_n + 1):
        if is_prime[i]:
            sum_primes += i  
        prime_sums[i] = sum_primes  

    
    
    [print(prime_sums[n]) for n in test_cases]


if __name__ == "__main__":
    main()

