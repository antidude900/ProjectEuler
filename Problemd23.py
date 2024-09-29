"""
https://www.hackerrank.com/contests/projecteuler/challenges/euler023/problem
"""


def sum_of_divisors(n): #this function is same as problem __
    total = 1
    for x in range(2, int(n**0.5) + 1):
        if n % x == 0:
            total += x
            if x != n // x:  
                total += n // x
    return total

def sum_of_two_abundant_nums(N, abundant_nums):
    if N > 28123: #if greater than 28123, for sure can be expressed as sum of two abundant numbers
        return True
    
    if N/2 in abundant_nums: #if any abundant number is half of num, then num can be expressed as the sum of the same abundant number 
        return True
        
    for x in abundant_nums: #if it isnt the sum of the same abundant numbers, it can be sum of different abundant number
        if (x>N): #if x>N, then for sure n cannot have x in its sum
                  #Also as any other abundant numbers in the list after x will be more greater than x i.e also greater than N, its no worth checking 
            break 
            
        if (N - x) in abundant_nums: #If  n=x+y, then y=n-x, now checking if that y is abundant number or not 
            return True
    
    return False

if __name__ == "__main__":
    t = int(input())
    
    inputs = [int(input()) for _ in range(t)]
    
    max_limit = max(inputs)
    

    abundant_nums = [n for n in range(12, max_limit + 1) if sum_of_divisors(n) > n] 
    
    for N in inputs:
        print("YES" if sum_of_two_abundant_nums(N, abundant_nums) else "NO")
