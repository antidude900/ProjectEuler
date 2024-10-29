
"""
To first understand the below algorithm, you should know about Euclid's formula.

Euclid's pythagorean triplet algorithm states that for any two positive integers m and n (m > n) where,
- m and n are coprime (they have no common divisor other than 1)
- m and n have opposite parity (one is odd, the other is even)

they will form a Pythagorean triple:(a,b,c) [Pythagorean triple meaning right angled traingle with sides a,b,c] where,
a = m^2 - n^2
b = 2 * m * n
c = m^2 + n^2

and the perimeter is given by;
p = a + b + c = 2 * m^2 + 2 * m * n = 2 * m * (m + n)
"""

def gcd(a, b): #finding the greates common divisor to check if coprime or not
    """
    We use Euclid's division algorithm to find the. It states that for two positive integers a and b;
    By continously dividing a by b and replacing a with b and b with the remainder of the divison until b becomes 0, we get the gcd which is 'a' when b becomes 0
    """
    while b != 0:
        a, b = b, a % b,
    return a

def max_ways_perimeter_upto_N(N):
    perimeter_ways = [0] * (N + 1) # we find all the perimeters upto N(p<=N) so that we dont have to recompute for each test cases
                                         # perimeter ways stores the no of ways to make each perimeters and each index number is the perimeter itself
    
    for m in range(1, int((N/2)**0.5)): #as perimeter should be less or equal to N, the 2m^2 term should be less than N meaning m<sqrt(N/2)
                             #this is just an apporximation assuming m >> n so neglecting n and finding limit of m. In reality, m value will be more less than 1581 if we consider n also 
        for n in range(1, m): 
            if (m + n) % 2 and gcd(m, n) == 1: #checking if of opposite parity and coprimer
                p = 2 * m * (m + n) 
                if p > N: #though we found m value for p<=N, still adding up n might lead to p>N. so handling that edge case
                    continue
                perimeter_ways[p] += 1
                i = 2
                while i * p <= N: 
                    """
                       the multiples of the perimeter p subsets the no of ways of p i.e if p is made from (a,b,c), 2*p will be made from(2*a,2*b,2*c)
                       so increase the no of ways of 2p as well for the solution (2*a,2*b,2*c) when we find solution of p as (a,b,c). 
                       Also because of the m and n nature of coprime and opposite polarity, it avoids genertaing m and n which generates same solution (2*a,2*b,2*c) for 2p
                       Thus there is no risk of duplicates
                    """
                    perimeter_ways[i * p] += 1
                    i += 1
    
    max_perimeter_upto = [0] * (N+1) # this array stores the perimeter having the maximum no of ways among the perimeters upto given index number
    
    
    for perimeter in range(1, N+1):
    
        max_perimeter = max_perimeter_upto[perimeter-1] #We take the current perimeter with the maximum no of ways
    
        # and then compare it to the the no of ways of the next perimeter
        if perimeter_ways[perimeter] > perimeter_ways[max_perimeter]: #if that next perimeter has more no of ways than the current perimeter with max no of ways
            max_perimeter_upto[perimeter] = perimeter #we update that the max no of ways upto that next perimeter is of the nextperimeter itself
          
        else: #but if that next perimeter has less no of ways than the current perimeter with max no of ways
            max_perimeter_upto[perimeter] = max_perimeter #then the max no of ways upto that next perimeter is still of the previous one
    
    return max_perimeter_upto
    
if __name__ == "__main__":
    T = int(input())
    N = [int(input()) for _ in range(T)]
    max_N  = max(N)
    max_perimeter_upto = max_ways_perimeter_upto_N(max_N)

    [print(max_perimeter_upto[n]) for n in N]

