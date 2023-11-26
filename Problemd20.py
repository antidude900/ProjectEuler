product = 1
sum = 0
num = 100

while (num!=1):#finding 100 factorial
	product *= num
	num-=1

tmp = str(product)#changing into string to iterate

for i in tmp:#adding all the digits
	sum+=int(i)
print(sum)