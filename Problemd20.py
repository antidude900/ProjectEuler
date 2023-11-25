product = 1
sum = 0
num = 100

while (num!=1):
	product *= num
	num-=1

tmp = str(product)

for i in tmp:
	sum+=int(i)
print(sum)