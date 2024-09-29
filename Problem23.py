def sum_of_divisors(n): 
    total = 1
    for x in range(2, int(n**0.5) + 1):
        if n % x == 0:
            total += x
            if x != n // x:  
                total += n // x
    return total

def sum_of_two_abundant_nums(N, abundant_nums): 
    if N > 28123:
        return True
    
    if N/2 in abundant_nums:
        return True
    for x in abundant_nums:
        if (N - x) in abundant_nums:
            return True
    
    return False

if __name__ == "__main__":
    t = int(input())
    
    inputs = [int(input()) for _ in range(t)]
    
    max_limit = max(inputs)
    

    abundant_nums = [n for n in range(12, max_limit + 1) if sum_of_divisors(n) > n]
    
    for N in inputs:
        print("YES" if sum_of_two_abundant_nums(N, abundant_nums) else "NO")
