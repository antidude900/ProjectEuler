def find_recurring_cycle_length(d):
    """Returns the length of the recurring cycle in the decimal part of 1/d."""
    remainders = {}
    value = 1
    position = 0
    
    while value != 0:
        if value in remainders:
            return position - remainders[value]  # Length of the recurring cycle
        remainders[value] = position
        value = (value * 10) % d
        position += 1
        
    return 0  # No recurring cycle (terminating decimal)

def precompute_longest_cycle(limit):
    """Precomputes the smallest d for each N < limit where 1/d has the longest cycle."""
    longest_d = 0
    max_cycle_length = 0
    results = [0] * (limit + 1)
    
    for d in range(2, limit):
        cycle_length = find_recurring_cycle_length(d)
        if cycle_length > max_cycle_length:
            max_cycle_length = cycle_length
            longest_d = d
        results[d] = longest_d
    
    return results

# Read input and solve for each test case
def solve():
    # Precompute the longest recurring cycle for all values of d < 10001
    limit = 10001
    precomputed_results = precompute_longest_cycle(limit)
    
    T = int(input())  # Number of test cases
    for _ in range(T):
        N = int(input())
        print(precomputed_results[N - 1])

# Example Usage:
solve()
