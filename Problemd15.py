import math


def lattice_paths(m,n):
    """for this can use the combination formula : 
    C(m + n, m) = (m + n)! / (m! * n!)
    [Formula of C(N,r) where N is m+n and m is r(Can also take n as r, stil same answer)]
    Thus if a square grid, then formula will be : (2n)! / ( n!)^2
    """

    return math.factorial(m + n) // (math.factorial(m) * math.factorial(n))


t= int(input())

for _ in range(t):
    m, n = map(int, input().split())
    print(lattice_paths(m,n)%(10**9+7)) #to get answer in modulo 10^9+7
