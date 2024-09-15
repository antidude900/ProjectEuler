"""
Find the absolute difference between the sum of the squares of the first n natural numbers and the square of the sum.
https://www.hackerrank.com/contests/projecteuler/challenges/euler006/problem
"""


def abs_diff(n):

    sum_square = n*(n+1)*(2*n+1)//6;	#formula for sum we read in sequence and series
                                		
    square_sum = n*(n+1)//2;

    square_sum = square_sum*square_sum;
    return square_sum - sum_square

n = int(input("Enter n:"))
print(abs_diff(n))
