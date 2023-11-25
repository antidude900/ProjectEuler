
product,sum=1,0

for i in range(1000):
	product *= 2

num = str(product)

for i in range(len(num)):
	sum+=int(num[i])
print(sum)