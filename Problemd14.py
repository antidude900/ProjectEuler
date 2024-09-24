def calculate_collatz_sequence_length(num, steps):
    """Calculate the length of the Collatz sequence for a given number."""
    temp = num
    length = 0
    
    while temp >= num:
        if temp % 2 == 0:  # If even
            temp //= 2
        else:  # If odd
            temp = 3 * temp + 1
        length += 1
    
    # Add precomputed steps if the number becomes smaller than the initial num
    length += steps[temp]
    return length


def precompute_collatz_steps(max_val):
    """Precompute the longest Collatz sequence for numbers up to max_val."""
    steps = [0, 0]  # Base cases: steps[0] and steps[1] are 0
    max_state = 0
    ans = [0] * (max_val + 1)
    
    for num in range(2, max_val + 1):
        length = calculate_collatz_sequence_length(num, steps)
        steps.append(length)
        
        # Track the number with the maximum sequence length so far
        if length >= max_state:
            max_state = length
            ans[num] = num
        else:
            ans[num] = ans[num - 1]
    
    return ans



    # Read the number of test cases


# Call the main function
if __name__ == "__main__":
    t = int(input())
    test_cases = [int(input()) for _ in range(t)]
    
    # Precompute results up to the maximum test case value
    max_val = max(test_cases)
    ans = precompute_collatz_steps(max_val)
    
    # Print the result for each test case
    for num in test_cases:
        print(ans[num])

