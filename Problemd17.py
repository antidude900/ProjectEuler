singles = ["","one","two","three","four","five","six","seven","eight","nine",]
doubles = ["","","twenty","thirty","forty","fifty","sixty","seventy","eighty","ninety"]
one_doubles = ["ten","eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen"]

sum = 0

def one_d_num(num):

	return len(singles[num[0]])

def two_d_num(num):
	if num[0] == 1:
		return len(one_doubles[num[1]])
	else:
		return len(doubles[num[0]]) + len(singles[num[1]])

def three_d_num(num):
	sum=one_d_num(num[:1])+len("hundred")

	second_part = two_d_num(num[1:])
	if (second_part != 0):
		sum+=len("and")

	sum+=second_part
	return sum


for i in range(1,1001):
	ind_sum = 0
	num = [int(j) for j in str(i)]
	size = len(num)
	
	if (size == 1):
		sum +=one_d_num(num)
		ind_sum += one_d_num(num)
	
	if (size == 2):
		sum += two_d_num(num)
		ind_sum += two_d_num(num)

	if (size == 3):
		sum += three_d_num(num)
		ind_sum += three_d_num(num)

	if (size == 4):
		sum+=len("onethousand")
		ind_sum += len("onethousand")

		print(sum)
print(sum)