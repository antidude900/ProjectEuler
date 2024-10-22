"""
https://www.hackerrank.com/contests/projecteuler/challenges/euler029/problem
"""

def distinct_terms(N):
    count = 0
    tested = [0]*(N+1)
    
    for i in range(2, N+1):
        if tested[i]: 
            continue
            
        overlapped = set()
        power = 2
        
        while (i**power <= N):
            tested[i**power] = True
            s = [j*power for j in range(2, N+1) if j*power > N]

            overlapped.update(s)
           
            power += 1

        count += len(overlapped) + N - 1

    return count
    
if __name__ == "__main__":
    N = int(input())      
    print(distinct_terms(N))
    
