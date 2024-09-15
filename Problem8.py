"""
Find the greatest product of k consecutive digits in the n digit number.
https://www.hackerrank.com/contests/projecteuler/challenges/euler008/problem
"""

def greatest_product(num,size,adj):
    g_p=0	#initializing the greatest product to 0 
    
    for i in range(size - adj): 
        """looping till we get to the final index minus number of adjacent number 
	so that we wont exceed the index of the list while running the second  loop """
	    
        p = 1	#initilaizing the initial product to 1 

	"""The reason why p=1 but g_p=0 is that suppose we had g_p=1 and all the consecutive product gives 0 
 	i.e p=0 in all the consecutive products then the g_p will always stay 1 as g_p is greater than p in all case
  	so though our greates_product should have been 0 it gives greatest proudct as 1. So to handle this edge case,
   	we used g_p as 0 so that any product that will come at beginning with be the greatest product"""
	
    
        for j in range(i,i + adj): #looping from a element to 12 more from it(1 +12=13)
            p *= int(num[j]) #multiply all the 13 adjacent elements
            
        
            if (p > g_p and j==i+adj-1): 
                #if greater than the greatest product, it is the  greatest product
                g_p = p

    return g_p
	
num,n,k=int(input("Enter the number, its size and the lenght of consecutive numbers for product"))
print(greatest_product(num,n,k))
