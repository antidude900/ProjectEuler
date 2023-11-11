first,second,sum = 1,2,0 #initializing the first and second term of the sequence as 1 and 2

while (second <= 4000000): #checking all fibo numbers until number exceeds 4 million

	if (second % 2 == 0):	#// if even include it in the sum
		sum += second

	temp = second #set the next two consecutive terms of the fibo seq
	second = first + second
	first = temp

print(sum)

