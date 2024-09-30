"""
https://www.hackerrank.com/contests/projecteuler/challenges/euler024/problem
"""
import math

def nth_lexicographic_permutation(n):

    #making the list from the string so that we can apply function of list like pop(which removes the item of the given index)
    #string though are array-like, can't use array functions like append and pop
    letters = list("abcdefghijklm")
    result = [] #for storing the required nth permutation
    n -= 1  #We are n in 1 based but as list use 0-index, changing into it

    """
    We have total 13 letters so 13! permutation in total. 
    Also, 13! = 13*12! meaning each of the 13 characters can make 12! permutation for itself(itself at first while others are doing permutation among them)
    So while n<12!, 'a' is at first of the permutation and after n>12!, any other letter after 'a'comes at first. 
    for eg: if n=12!+1, 'b' comes at first of permutation as the permutations of a has ended
    Thus what comes at first can be determined by doing n/12! 
    Now we remove 'a' and thus so we have 12 letters and thus 11! for each. 
    By updating n' = n%12!, we will know how much up it was from 12! which will help us to find the first letter of the n' permutation of the remainaing string
    which is subsequently the second letter of the n! permutation.
    
    [Permutation of a number can be divided in these steps: (Lets take example of 4 digit number to find nth permutation)
    First, the permutation of the whole number is carried from which the 1st number for the nth permutation is picked 
    and then the permutation is broken to the permutation between the remaning 3
    Second, the permutation of the remaning 3 is carried from which the 2nd number for the nth permutation is picked  
    and then the permutation is broken to the permutation between the remaning 2
    Third, the permutation of the remaning 2 is carried from which the 3rd number for the nth permutation is picked  
    and then the permutation is broken to the permutation between the remaning 1
    Finally, the remaning one is the last number of the nth permutation
    """
    
    for i in range(12, -1, -1): 
        
        selected, n = divmod(n, math.factorial(i)) #divmod(n,math.factorial(i)) gives n/math.factorial(i) and n%math.factorial(i)
        result.append(letters.pop(selected)) #the selected one is removed and stored in the result array
    
    return ''.join(result) #the list is converted to string 


T = int(input()) 
for _ in range(T):
    N = int(input())
    print(nth_lexicographic_permutation(N))
