"""
https://www.hackerrank.com/contests/projecteuler/challenges/euler014/problem
"""

def numState(num):
    num_state = 0
    while num != 1:
        if num % 2 == 0:
            num //= 2
        else:
            num = 3 * num + 1
        num_state += 1
    return num_state

def main():
    t = int(input())  # Read number of test cases
    test_cases = [int(input()) for _ in range(t)]  # Read input values
    
    max_val = max(test_cases)  # Find the maximum number in the input list
    
    # Initialize a list to store answers, with index representing the number
    ans = [0] * (max_val + 1)
    
    max_state = 0
    steps = 0
    
    # Calculate the longest sequence for numbers up to max_val
    for j in range(1, max_val + 1):
        num_state = numState(j)
        if num_state >= max_state:
            max_state = num_state
            steps = j
        ans[j] = steps  # Store the number that has the max sequence
    
    # Print the result for each test case
    for num in arr_input:
        print(ans[num])

# Call the main function
if __name__ == "__main__":
    main()


