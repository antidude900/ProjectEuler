"""
Let's talk about the sequence given before diving in the solution:

The given sequence of number is: 0.123456789101112131415161718192021...

The first 9 digits in the fraction part are single digit number from 1 to 9.
After that, two digit number starts from 10,11,12,13,...,19,20,21,22,...,99.
After that, three digit number starts from 100,101,...,109,110,111,112,...,119,120,121,...,199,200,...,999.
Then similarly four digit number and so on

Here we are changing index to offset and adding to start to give the destination number.
index gives how far we have to go from start to reach the number. index//digit however gives the offset from start(difference between start and the number)

lets understand how. suppose we are at sequence of two digit numbers. After 2 succesive increase in the index, the start changes
i.e if it was 10, after 2 index, we will reach 11. So we check how much increment of 2 does index has by index-1/2 (index-1 to change it to 0 index system) 
suppose index=15 so we get 15/2 saying there is 7 increment of 2 in index. For each increment of 2, the start changes to reach the new number.
So start changes 7 times i.e 11 12 13 14 15 15 16 17. As each change is an increment to start, we can add the total no of changes to start to get the destination number 
i.e desitnation_number = start - total_change where total_change = (index-1)/digit_length. Thus final formula is desitnation_number = start - (index-1)/digit_length.
"""
def find_digit_at(index):
    # Step 1: Determine the range that contains the index
    digit_length = 1   # Start with 1-digit numbers
    start = 1          # The first number in the current range (1, 10, 100, ...)
    count = 9          # Count of numbers in the current range

    # Keep increasing the digit length until we locate the range that contains the index
    while index > digit_length * count:
        index -= digit_length * count
        digit_length += 1
        start *= 10
        count *= 10

    # Step 2: Find the exact number and digit within the number
    # The exact number in the sequence that contains the target digit
    number = start + (index - 1) // digit_length
    # Position of the digit within the number
    digit_index = (index - 1) % digit_length

    # Return the required digit from the target number
    return int(str(number)[digit_index])



for _ in range(int(input())):
    prod=1
    for i in input().split():
        prod*=find_digit_at(int(i))
    print(prod)
    
