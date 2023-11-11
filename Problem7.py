from math import sqrt

n ,num =1,2	#declaring the 1st prime number as 2

while (n != 10001): #looping until we get to 10001th prime number
	num += 1	#testing the next number if prime or not

	isPrime = 1
	for i in range (2,int(sqrt(num))+1):	#looping to test if prime or not
											#Any num1 greater than the square root of num2 cant evenly divide num2
		if (num%i == 0):	#if evenly divides cant be prime so stop prime testing loop
			isPrime = 0
			break

	if (isPrime): #if prime then update the number of prime numbers we found4
		
		n+=1
print(num)