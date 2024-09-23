"""
Work out the first ten digits of the sum of N 50-digit numbers.
https://www.hackerrank.com/contests/projecteuler/challenges/euler013/problem
"""

N = int(input())
total_sum = 0

for _ in range(N):
    n = int(input())
    total_sum += n

print(str(total_sum)[:10])
