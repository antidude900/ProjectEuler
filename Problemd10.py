from math import sqrt

sum = 0
for i in range(2,2000000): #taking all numbers below 2 million
							#not 0 and 1 are they are niether prime nor composite
	isPrime = 1
	for j in range (2,int(sqrt(i))+1):	#test the number is prime or not
		if (i%j == 0): #if evenly divisble by a number not 1 or itself, then not prime
						#so stop the loop saying its composite
						#if completes the whole loop, then no numbers that evely divides it so prime 
			isPrime = 0
			break

	if isPrime:
		sum+=i
print(sum)
