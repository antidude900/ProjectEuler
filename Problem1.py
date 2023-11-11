sum = 0

for i in range(1000):	# checking all numbers less than 1000
	if (i%3==0 or i% 5 == 0):	# if divisible by either 3 or 5, then include it in the sum
		sum += i

print(sum)