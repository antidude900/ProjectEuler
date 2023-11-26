sum=0

n=pow(2,1000) #for 2 to the power 1000

num = str(n) #so that we can iterate throught the number

for i in range(len(num)):
	sum+=int(num[i]) #adding all the digits
print(sum)