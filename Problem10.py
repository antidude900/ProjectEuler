"""
Find the sum of all the primes not greater than given N.
https://www.hackerrank.com/contests/projecteuler/challenges/euler010/problem
"""

"""
This solution doesn't solve the problem of repeititive process for every single test cases. For that, see the v2 version
"""


def prime_sieve(n):
    if n<2:
        return 0
    
    prime = [True] * (n+1) #as index starts from 0, we increase limit size by 1 (otherwise the index will be from 0 to limit-1 thus excluding limit)
    sum = 0  

    # Sieve of Eratosthenes
    for i in range(2, n+1):
        if prime[i]:  
            sum+=i
            for j in range(i * i, n+1, i):
                prime[j] = False
    return sum


if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())
        print(prime_sieve(n))
