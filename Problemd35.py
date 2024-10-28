"""
https://www.hackerrank.com/contests/projecteuler/challenges/euler035/problem
"""

"""
The test cases for this problem are poorly designed. 
Though the problem statement has mentioned that the rotations can exceed N, one solution of my which didnt do that still passed all cases.
I got confused and printed answer for both of the algorithms
(one which allows rotations greater than N and the other which didnt(meaning if one of the rotation of a number exceeds N it doesnt consider the number circular prime))
Both algorithms gave different answers for N=198. The first one gave 887 as it included 113,131,197 and the another one gave 446 as it excluded those numbers as their rotation>N

(the second algorithm was made by using sieve_of_eratosthenes which finds primes below N)
"""

def is_prime(n):
    """
	Can also use sieve_of_eratosthenes to find primes but this normal way also passed all test cases so used this.
 	For this sieve_of_eratosthenes, we find primes upto 10**len(str(limit))
    """
    #dont need 'if n<2: return False' statement because we start checking primes through 2 in circular_primes_sum() functiton
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def generate_rotations(num):
	#We can also use permutations from itertools to find rotations
    num_str = str(num)
    rotations = [int(num_str[i:] + num_str[:i]) for i in range(len(num_str))] #adding the letters starting from index i + letters before i produces rotations
    return rotations

def circular_primes_sum(limit):
    circular_primes = []
    for num in range(2, limit):
        if all(is_prime(rot) for rot in generate_rotations(num)): #if all the rotations of a number is prime, then the number is circular prime
            circular_primes.append(num)
    return sum(circular_primes)

if __name__ == "__main__":
	limit = int(input())
	print(circular_primes_sum(limit))
