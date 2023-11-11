from math import sqrt

triplet = []
isResult = False

for i in range(1,1000): #taking random a and b for the triplet
	for j in range(1,1000):

		k = sqrt((i*i)+(j*j)) #making c for the triplet

		if (i+j+k == 1000):	#checking if they fulfill condition a+b+c =1000
			#if yes then stop looping as we got our triplet
			isResult = True
			product = i*j*k
			break
	if isResult:
		break;

print(product)
