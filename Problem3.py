#!/bin/python3

import math
import time

"""
any number can be written as product of prime i.e its factors can be simply written in only prime factors.
hence prime factors are the building blocks and they are the one who can group up to make a composite factor as well
"""
def largest_prime_fac(n):
    fac=-1
    for i in range(2,int(math.sqrt(n))+1): #if there is no factors below root under n, then n itself is prime

        while(n%i == 0)""" removing all the same prime factors to avoid prime factors from clumping together and making a composite factor
			for eg: if given number 16; if we will have:2*8 and will get largest prime factor as 8 which is wrong
      			but if we do like: 2*2*2*2 and remove all the 2 after we found 2 as prime factor,
	    		then the largest prime factor is 2 which is right
			"""
            fac=i 	
            n//=i
            
            
    if (n > 1):"""suppose for 10 we do root under we get 3 so first loop with 2 is allowed as 2>3 add thus 2 is taken as prime 
    		and we do 10/2 getting 5 whose root is 2 but as 3 is greater than 2, the loop will break. now we come to this if condition
      		and as 5 is greater than 1 we get 5. so the meaning of this if condition is that, if after factorizing still its not fully
		factorized then the remaining number is the last factor left
  		"""
        fac=n
        
    return fac
        
        
n= int((input("Enter n:")))
print(largest_prime_fac(n))

