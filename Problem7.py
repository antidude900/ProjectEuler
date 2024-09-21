"""

Leave for now

"""

"""
See this video first to undersand sieve first: https://www.youtube.com/watch?v=nDPo9hsDNvU&list=PLfqMhTWNBTe0b2nM6JHVCnAkhQRGiZMSJ

In the video, 0 is used to mark as prime and 1 is used to mark as not prime in a prime array which is so confusing.
(should have been 1 for prime and 0 for not prime)
so let us use True to denote that it is prime and False to say it is not prime
"""

import math

def estimate_limit(n):
    return int(n * (math.log(n + 1) + math.log(math.log(n + 1))) + 5) #this formula helps us to estimate a limit(range) to find the nth prime
    
def prime_sieve(n):
    limit = estimate_limit(n)  
    prime = [True] * (limit + 1) 
    count = 0  

    # Sieve of Eratosthenes
    for i in range(2, limit + 1):
        if prime[i]:  
            count += 1  
            if count == n:  
                return i
            
            for j in range(i * i, limit + 1, i):
                prime[j] = False


if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())
        print(prime_sieve(n))
