#alogrithm to find prime factors
num,factor = 600851475143,2;	# starting with number 2 to check all prime factors of num

while (factor<=num):	#we will have factors until the number we divide with exceeds the number itself
	if (num%factor == 0):	#while if it is a factor
		num /=factor	#factor decrease the num by factor so the num goes on shrinking until the numb is not divisible by the factor


	factor+=1	#if not a factor go to another number for checking
#the factor we get at the end is the highest prime factor

factor -= 1 #as we add 1 at the end of loop above no matter what, it gets added to the final result we require too. So removing that 1
print(factor)
