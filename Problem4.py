l = 0

for i in range (1,1000):	#loop to form numbers from two 3 digit numbers
	for j in range (1,1000):
		p = i*j	

		if (str(p) == str(p)[::-1] and p>l):	
		#first converting number to string as numbers as we cant iterate through each digit of number by index
		#but we can iterate through each character of number through index
		#now p[::-1] gives p in reverse form 
			l = p;
print(l)
