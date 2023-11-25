#alogirthm to find prime factors of a number

num,factor = 600851475143,2;	# starting with number 2 to check all prime factors of num

while (num>=factor):	#we will have factors until the factor exceeds the number its dividing
	if (num%factor == 0):	#if it is a factor
		num /=factor	#factor decrease the num by division so the num goes on shrinking until the numb is not divisible by the factor
	else:
		factor+=1	#if not a factor go to another number for checking
	
print(factor);
