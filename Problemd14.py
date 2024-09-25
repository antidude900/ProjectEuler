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

        #the below code does the same thing as explained aboved
        if length >= max_length: 
            max_length = length
            longest_len_nums[num] = num
            max_length_num = num
        
        longest_len_nums[num] = max_length_num
    
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

