"""
Find the largest palindrome made from the product of two 3-digit numbers which is less than n.
https://www.hackerrank.com/contests/projecteuler/challenges/euler004/problem?isFullScreen=true
"""


def largest_pal(n): 
    palindrome = 0
    
    while palindrome==0:	#run until the required palindrome is found
        n -=1 				#starting from the number 1 less than n (as need to find largest, it better to start from top not bottom)
        if str(n)==str(n)[::-1]: #checking if it is palindrome or not

			#checking if the number can be represented in product of two 3-digit numbers
            for j in range(100, 1000):	#j is a 3 digit number
                f = n/j					#if first of the two number of product is j then the another number is f
                if f%1 == 0 and f <= 999: 	#checking if f is integer and a 3 digit number
										  	#if f is not integer then can know that j is not a factor of n so j can't be the number in the product
												
                    palindrome=n			#if all above conditions satisfied, then they are the one giving product n
											#and thus n is the largest palidrome(largest as we are searching from top)
                    break
    return palindrome

n = int(input("Enter n:))
print(largest_prime_fac(n))
    
