"""
Find the sum of all the primes not greater than given N.
https://www.hackerrank.com/contests/projecteuler/challenges/euler010/problem
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
    import sys
    input = sys.stdin.read
    data = input().split()
    
    t = int(data[0])  
    test_cases = [int(data[i]) for i in range(1, t + 1)]
    max_n = max(test_cases)  # Find the maximum n

    
    is_prime = sieve_of_eratosthenes(max_n)
    prime_sums = [0] * (max_n + 1)
    sum_primes = 0

    
    for i in range(2, max_n + 1):
        if is_prime[i]:
            sum_primes += i  
        prime_sums[i] = sum_primes  

    
    results = [str(prime_sums[n]) for n in test_cases]
    print("\n".join(results))

if __name__ == "__main__":
    main()

