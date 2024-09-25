"""
https://www.hackerrank.com/contests/projecteuler/challenges/euler014/problem
"""

def length_of_sequence_nth(num, lengths):
    """Calculate the length of sequence for a given number num."""
    temp = num
    length = 0
    
    while temp >= num: 
        if temp % 2 == 0:  # If even
            temp //= 2
        else:  # If odd
            temp = 3 * temp + 1
        length += 1
    
    """
    if temp<num i.e while finding numbers of the sequence, we got a number such that it is less than the number whose length is being evaluated
    as we are finding sequence length of all numbers in increasing order, we will already have the sequence of that lesser number.
    So we just add its length on the current length of the sequence to find the full length
    """
    
    length += lengths[temp]
    return length


def length_of_sequence_all(max_val):
    """Calculate the length of sequence of all numbers upto max_val"""
    lengths = [0, 1]  # stores the length of each number(index represent respective number)
    max_length = 0   # stores track of the longest length 
    longest_len_nums = [0] * (max_val + 1)  #stores the number which has the longest length among the n(index represents n) numbers
    longest_len_nums[1] = 1 #as 1 is already 1, we dont have to find the sequence and its length is in default 1
    
    for num in range(2, max_val + 1): 
        length = length_of_sequence_nth(num, lengths) #finding length of number from 2 to max_val(0 and 1 are already predetermined]
        lengths.append(length) #append the length of the respective num
        
        """
        To explain the below code, lets first take an example:
        Lets us write the first 7 values(0 to 6) of longest_len_nums array and then explain it:
        longest_len_nums = [0, 1, 2, 3, 3, 3, 6]
        
        Collatz sequence is only possible for natural numbers. So using 0 only to make index correspond to the respective number
        
        Here 1 has collatz sequence 1. So its length is 1. 
        As among the numbers upto 1, the one with the longest length is 1. So longest_len_nums[1] is set to 1 in default.
        
        Here 2 has collatz sequence 2→1. So its length is 2.
        As among the numbers upto 2, the one with the longest number is 2. So longest len_num[2] is set to 2

        Here 3 has collatz sequence 3→10→5→16→8→4→2→1. So its length is 8.
        As among the numbers upto 3, the one with the longest number is 3. So longest len_num[3] is set to 3.

        Here 4 has collatz sequence 4→2→1. So its length is 3.
        As among the numbers upto 4, the one with the longest number is 3. So longest len_num[4] is set to 3.

        Here 5 has collatz sequence 5→16→8→4→2→1. So its length is 6.
        As among the numbers upto 5, the one with the longest number is 3. So longest len_num[5] is set to 3.

        Here 6 has collatz sequence 6→3→10→5→16→8→4→2→1. So its length is 9.
        As among the numbers upto 6, the one with the longest number is 6. So longest len_num[5] is set to 6.       
        """

        #the below code does the same thing as explained aboved
        if length >= max_length: 
            max_length = length
            longest_len_nums[num] = num
            max_length_num = num

       
        longest_len_nums[num] = max_length_num
        
     #if would have been a single test question, then would have return max_length_num instead of longest_len_nums
    return longest_len_nums


# Call the main function
if __name__ == "__main__":
    t = int(input())
    test_cases = [int(input()) for _ in range(t)]

    """taking maximum value among all test_cases 
    so that the longest_len_nums array we create upto that maximum value will also contain the limit value of each test case"""
    
    max_val = max(test_cases)
    longest_len_nums = length_of_sequence_all(max_val)
    
    # Print the result for each test case
    for num in test_cases:
        print(longest_len_nums[num])

