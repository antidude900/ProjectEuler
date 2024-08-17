"""
Find the absolute difference between the sum of the squares of the first n natural numbers and the square of the sum.
"""


def abs_diff(n):

    sum_square = n*(n+1)*(2*n+1)//6;	#formula for sum we read in sequence and series
                                		#fun fact: I came up with this idea instead of looping in first thought!
    square_sum = n*(n+1)//2;

    square_sum = square_sum*square_sum;
    return square_sum - sum_square

n = int(input("Enter n:"))
print(abs_diff(n))
