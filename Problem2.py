"""
By considering the terms in the Fibonacci sequence whose values do not exceed , find the sum of the even-valued terms.
https://www.hackerrank.com/contests/projecteuler/challenges/euler002/problem
"""

def fibo_sum(n):
    first,second,sum = 1,2,0 #initializing the first and second term of the sequence as 1 and 2

    while (second <= n): #checking all fibo numbers until number exceeds 4 million
    
        if (second % 2 == 0):    #// if even include it in the sum
            sum += second
    
        temp = second #set the next two consecutive terms of the fibo seq
        second = first + second
        first = temp
    
    return sum


if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())
        print(fibo_sum(n))
