"""
https://www.hackerrank.com/contests/projecteuler/challenges/euler031/problem
"""

"""
Explanation Tomorrow for sure, I promise
"""

"""
Also talk about minimum coins problem
"""

def total_no_of_ways(n):
    results=[0]*(max(n)+1)
    results[0]=1
    
    coins=[1, 2, 5, 10, 20, 50, 100, 200]
    for i in range(8):
        for j in range(coins[i], max(n)+1):
            results[j] += results[j-coins[i]]
            
    return results
    
if __name__ == "__main__":
    inputs=[int(input()) for x in range(int(input()))]
    results=total_no_of_ways(inputs)
    for x in inputs:
        print(results[x]%(10**9+7))
