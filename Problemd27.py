"""
https://www.hackerrank.com/contests/projecteuler/challenges/euler027/problem
"""

import math

#Checking whether the result generated is prime or not
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

#Calculating total no of consecutive primes of the eqn : n**2 + a*n + b
def consecutive_primes(a, b):
    n = 0
    while is_prime(n**2 + a*n + b):
        n += 1
    return n

# Ranging a and b from -N to N as |a|<=N and |b|<=N, Then finding the eqn which produces most no of consecutive primes
def find_best_coefficients(limit):
    max_primes = 0
    product_of_coefficients = 0

    for a in range(-limit + 1, limit+1):
        for b in range(-limit, limit + 1):
            primes_count = consecutive_primes(a, b)
            if primes_count > max_primes:
                max_primes = primes_count
                max_a,max_b = a ,b

    return max_a,max_b

if __name__=="__main__":
    limit = int(input())
    a,b=find_best_coefficients(int(input()))
    print(a,b)

