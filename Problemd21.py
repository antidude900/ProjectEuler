
def sum_of_divisors(n):
    total = 1
    
    """
    If x is proper divisor of n and if n/x = y, then both x and y are proper divisors of n
    For eg: 6/2=3. Here both 3 and 2 are proper divisors as 6/3=2 (Thus If n/x = y, then n/y=x (Simply multiplying both sides by x/y))
    Thus we add both x and n//x in total
    """
    for x in range(2, int(n**0.5) + 1):
        if n % x == 0:
            total += x
            if x != n // x:  #for avoiding edge case of perfect square number. for eg: 36/6=6. This leads to adding 6 two times
                total += n // x
    return total

def sum_of_amicable_numbers(limit):
    total = []
    for a in range(limit + 1):
        b = sum_of_divisors(a)
        if a == sum_of_divisors(b) and a != b:
            total.append(a)
    return total

if __name__ == "__main__":
    t = int(input())
    
    inputs = []
    for _ in range(t):
        inputs.append(int(input()))
    
    max_limit = max(inputs)  
    
    # Finding amicable numbers upto max_limit
    amicable_numbers = sum_of_amicable_numbers(max_limit) 

    # For each input, calculate the sum of amicable numbers upto the respective limit
    for n in inputs:
        print(sum(x for x in amicable_numbers if x <= n))
