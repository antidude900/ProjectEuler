"""
https://www.hackerrank.com/contests/projecteuler/challenges/euler034/problem
"""

from math import factorial

if __name__ =="__main__":
    N = int(input())
    total_sum=0
    
    for i in range(10,N): #Single digits are not considered as sum, so starting from 10
        sum_of_digits = sum([factorial(int(digit)) for digit in str(i)])

        """
        First we change the number into string so that we can iterate through it. We then find the factorial of all the numbers and then sum all of them
        """
        
        if sum_of_digits%i ==0: #If the sum is divisible by the corresponding number, then add it to the total sum
            total_sum+=i
            
    print(total_sum)
