def main():


    
    for num in range(2,max_val+1):#check for all values under 1 million
    
        temp = num
        length = 0
        while True:
            if temp % 2 == 0:#if even do this
                temp = temp//2
    
            else:#if odd do this
                temp = 3*temp+1
    
            length += 1 #as an term added increase the length
    
            if temp < num:    #if temp is less than the num of 6, it means we   have already gone through that number
                length+=steps[temp]
                steps.append(length)  #so that number already     exists in the steps list so add that value for remaining length
                                                #and append the sum for     record                                
                break                           #as found the total length  break the loop and for another number(num)
            
        num_state = length
        if num_state >= max_state:
            max_state = num_state
            step = num
        ans[num] = step  # Store the number that has the max sequence
    
        
    
    # Print the result for each test case
    for num in test_cases:
        print(ans[num])

# Call the main function
if __name__ == "__main__":
    t = int(input())  # Read number of test cases
    test_cases = [int(input()) for _ in range(t)]  # Read input values
    
    
    max_val = max(test_cases)  # Find the maximum number in the input list
    
    
    steps = [0,0]     #starting from 0 so that each index represents the    respective number 
                    #and the value in that index shows the terms involved to    reach 1
    max_val = max(test_cases)  # Find the maximum number in the input list
    
    # Initialize a list to store answers, with index representing the number
    ans = [0] * (max_val + 1)
    max_state = 0
    

    


