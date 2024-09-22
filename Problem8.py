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
	
    
        for j in range(i,i + adj): #looping from a element to (adj-1) more from it
				   #(one less than adj because including the starting number, it will be upto no of adj )
            p *= int(num[j]) #multiply all the adjacent elements
            
        
            if (p > g_p and j==i+adj-1): 
                #if greater than the greatest product, it is the  greatest product
                g_p = p

    return g_p
	
if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        k = int(first_multiple_input[1])

        num = input()
        
        print(greatest_product(num,n,k))
        
