"""
https://www.hackerrank.com/contests/projecteuler/challenges/euler029/problem
"""

"""
Let's see the the niave approach first:

"
distict_terms = set()
for a in range(2,N):
    for b in range(2,N):
        distinct_terms.add(a**b)
print(len(distinct_items))
"

The problem with this approach is that we are recalculating the overlapped values between the number and the powers of the number.
For eg: 2 and its power upto 10 exponents
2: 2, 4 , 8 , 16 , 32 , 64 , 128 , 256 , 512 , 1024
4(2^2): 4 , 16 , 64 , 256 , 1024 , 4096 , 16384 , 65536 , 262144 , 1048576
8(2^3): 8 , 64 , 512 , 4096 , 32768 , 262144 , 2097152 , 16777216 , 134217728 , 1073741824
and so on.

Here you can see that the powers of 4 upto 5 terms(10//2) are overlapped by 2 and power of 8 upto 3 terms(10//3) are overlapped by 2.
Similarly for 16(2^4), 2 terms(10//4) are overlapped by 2.
Thus for 2^n, 10//n terms are overlapped by 2.

So, by calculating the powers of its powers in the same time, we can prevent recalculating overlapped values
"""

def distinct_terms(N):
    count = 0
    tested = [0]*(N+1)
    
    for base in range(2, N+1): # Iterating through all values for base: 2<=a<=N(Given)
        if tested[base]: # If the number is already seen when iterating through powers of a given number, then it will be analyzed there already. So no need to analyze it again
            continue
            
        extras = set() # Storing the extra terms(terms of the number besides the overlapping ones) for counting purpose
        exponent = 2 # To start iterating through all values of exponent from 2
					 # The upper limit of exponent i.e N(2<=b<=N) will be handled later in a single line while calculating the count				
        
        while (base**exponent <= N):
			"""
			This while condition is for calculating the overlapped terms of the powers. We make sure that the power donot exceed N because because the base should stay under N
   			As the powers are considered as base and their powers are calculated(The powers we get of the power of say "x" overlapp with powers of x as explained earlier)
			"""
			
            tested[base**exponent] = True # recording that the number equal to base**exponent is tested
		
            extra = [new_base*exponent for new_base in range(2, N+1) if new_base*exponent > N]
			"""
			This is a bit confusing one so let us go through a simple version of the above line of code:
   
            new_base=base**exponent
            extra = [new_base**new_exponent for new_exponent in range((N//exponent)+1, N+1)]

   			As we now have to find the powers of a certain power, the power itself is the base say new_base and now to find its power,
			we start iterating after (N//exponent)th term of new_base(The numbers upto (N/exponent)th term are overlapped and already contained by the parent base as explained in line 25)
   			to get the non-overlapped terms of the new_base and thus we find the total distinct terms of the new_base as well
   			"""

            extras.update(extra)
           
            exponent += 1

        count += len(extras) + N - 1

    return count
    
if __name__ == "__main__":
    N = int(input())      
    print(distinct_terms(N))
    
