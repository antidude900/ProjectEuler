
"""
length of recurring cycle is simply the no of digits of the number which is recurring
For eg:

1/6 = 0.16666... [Here 6 is the number that is recurring, So length of recurring cycle is 1]
1/7 = 0.142857142857.... [Here 142857 is the number that is reccuring, So length of recurring cycle is 6]

From this example, we might feel that if a number comes back in the quotient, we get a recurring cycle
But take example of this:1/34 = 0.0294117647, Here 1 reoccured but there was no cycle formed
Each number in quotient are simply to subtract the remainder with the product of divider.
Say if divider is n: one 1 can subract say 20 i.e 20-1*n = x and another 1 can subract say 30 i.e 30-1*n=y
As they give different remainder x and y, the sequence of quotients that will be subtracting them wont be the same, So no recurring cycle

Thus to find reccuring cycle, we have to find a remainder that comes back because for the same remainder,the sequence in which it subtracted will always be same
And thus a reccuring cycle is formed.

"""

def find_recurring_cycle_length(d):
    remainders = {}    #storing the remainders and its position in which it occured
    remainder = 1 #starting to divide from 1
    position = 0 #keeping track of position to know the length
    
    while remainder != 0:
        if remainder in remainders: 
            return position - remainders[remainder]  #doing "current position minus position in which remainder occured first" to know the length of recurring cycle
            
        remainders[remainder] = position #store the remainder and its position
        remainder = (remainder * 10) % d #finding the remainder(for decimal points in quotient, we always multiply tne remainder by 10. For eg doign 1/0.2 is equivalent to 10/2
        position += 1 #increment the position
        
    return 0  # No recurring cycle (terminating decimal)

def precompute_longest_cycle(limit): 
    """Precomputes the smallest d for each N < limit where 1/d has the longest cycle."""
    longest_d = 0
    max_cycle_length = 0
    results = [0] * (limit + 1)
    
    for d in range(2, limit): #same as we did in Problem 14
                              #(There we stored the Longest collatz sequence among numbers from 0 to n and here we do the same but for longest recurring cycle)
        cycle_length = find_recurring_cycle_length(d) 
        if cycle_length > max_cycle_length:
            max_cycle_length = cycle_length
            longest_d = d
        results[d] = longest_d
    
    return results
    

if __name__=="__main__":
    # Precompute the longest recurring cycle for all values of d <= 10000
    limit = 10001
    precomputed_results = precompute_longest_cycle(limit)
    
    T = int(input())  
    for _ in range(T):
        N = int(input())
        print(precomputed_results[N - 1]) #question asking ford d less than N. So finding the longest reoccuring cycle upto N-1


