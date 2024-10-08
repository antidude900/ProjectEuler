"""
https://www.hackerrank.com/contests/projecteuler/challenges/euler028/problem
"""


"""
For this question,we find the eqn of the series of all diagonals(uppper right, upper left, lower left, lower right)
For eg: 

For a 7*7 sprial;

  43  44  45  46  47  48  49
  42  21  22  23  24  25  26
  41  20   7   8   9  10  27
  40  19   6   1   2  11  28
  39  18   5   4   3  12  29
  38  17  16  15  14  13  30
  37  36  35  34  33  32  31
  
Here, all of the diagonals dont follow a normal sequence as their difference is also following a sequence of difference 8.
So we cant use normal eqn: a+(n-1)d to find the eqn of the series
For this, we will be assuming a eqn giving the required value when provided the n and finding out its coefficients.

If we take a 1 degree eqn,say An+B=f(n) the coefficients value will come from 2 eqns i.e:
An+B = 9
An+B = 25
If it would have been a simple series, it would have been ok because the difference is constant and thus 9 and 25 are enough to describe the whole eqn for the upper right diagonal

So we atleast need 3 eqns so that we consider 3 different values and thus address the changing differenc. Hence, we take a quadratic eqn(As it needs atleast 3 eqns to be solved):
An^2+Bn+C = 9
An^2+Bn+C = 25
An^2+Bn+C = 49
and the eqn we get from this, we address the changing difference as well.

Here the upper right diagonal follows the eqn:4n^2+4n+1 (1 is not included in this series. As it is common to all the diagonals, including it in series will add multiple 1s)
The upper left diagonal is: 4n^2+2n+1
The lower left diagonal is: 4n^2+1
The lower right diagonal is: 4n^2-2n+1

Adding all of this (as we need sum of all diagonals),we get:16n^2+4n+4
But this will only give the sum of diagonals at a certain level. But as we need total sum of diagonals, we change the nth term to their respective sum.
n^2 sum is n(n+1)(2n+1)/6 and n is n(n+1)/2 and 1(in 4*1) is n

So we get total sum of diagonals as: 16(n(n+1)(2n+1)/6)+4(n(n+1)/2)+4n+1 (adding the 1 at the end)
"""


def sum_of_spiral_diagonal(N):
    n_squared = (N*(N+1)*(2*N+1))//6
    n = (N*(N+1))//2
    s = 16*n_squared+4*n+4*N+1
    

    return s

if __name__ == "__main__":
    
    t = int(input())    
    for _ in range(t):
    
        N = int(input()) // 2 # changing the grid size to layer size
                              # for eg 5=>2 meaning it is 2 layer grid where 9 is in 1st layer and 25 is in 2nd layer
                              # this way it will be easy to find the n value for the eqns 
        print(sum_of_spiral_diagonal(N)% (10**9+7))
