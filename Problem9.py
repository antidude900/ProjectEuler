"""
https://www.hackerrank.com/contests/projecteuler/challenges/euler009/problem
"""

def pytho_triplet(n):
    result=-1
    for a in range(1, n//3): #any number can't be bigger than one third of the number as we have to express the number in sum of three
        for b in range(a, ((n-a)//2)+1)): #We know that c>b>a, and c=n−a−b. We can combine these into n−a−b>b, or n−a>2b or (n-a)/2>b
                                
            c = n - a - b
            if a**2 + b**2 == c**2:
                result = max(result,a*b*c)
                
    return result

if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())
        print(pytho_triplet(n))
