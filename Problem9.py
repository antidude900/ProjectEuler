"""
https://www.hackerrank.com/contests/projecteuler/challenges/euler009/problem
https://martin-ueding.de/posts/project-euler-solution-9-special-pythagorean-triplet/
"""

def pytho_triplet(n):
    result=-1
    for a in range(1, n//3):
        for b in range(a, n//2 - a//2):
            c = n - a - b
            if a**2 + b**2 == c**2:
                result = max(result,a*b*c)
                
    return result

n = int(input("Enter n"))
print(pytho_triplet(n))
