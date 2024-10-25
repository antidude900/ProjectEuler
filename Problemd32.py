"""
https://www.hackerrank.com/contests/projecteuler/challenges/euler032/problem
"""

#Here a and b represents the two numbers multiplying to give product
def is_pandigital(a, b, product, N):
    digits = str(a) + str(b) + str(product)
    return set(digits) == set(map(str, range(1, N+1))) 
	""" 
 	map(str,range(1,N+1)) represents the string containing numbers from 1 to N,
 	then checking if the set of digits contains all the digits from 1 to N
  	Here set is only being used to compare if both have same elements as in set, sets having same elements though in different arrangement are still considered to be same 
    Other ways to compare could be done by: return sorted(digits) == [str(i) for i in range(1, N + 1)] or,
											return ''.join(sorted(digits)) == ''.join(map(str, range(1, N+1)))
   	"""

def pandigital_products_sum(N):
    products = set()
    max_a = 10 ** (N // 2)
	"""
 	Setting the upper bound of a to be half of the total length of N. For eg if We have N=4, we get N//2=, i.e it only handles upto 2 digits of the total 4 digits.
	10**(N/2) helps in changing into digit will corresonding length. 10**(N/2) = 100, as it is kept as upper bound in the for in range(), 
	we go upto 99 thus the upper limit is only upto 2 digits
  	"""
	
    for a in range(1, max_a):
        max_b = 10 ** (N - len(str(a)))
		"""
		The another number(b) will have the length equal to the digits left by the first number. 
  		In the first iteration of a, its length will be 1 so another number length will be 3(say N=4)
		Thus the another number will be higher length(len(a)<N//2) or of equal length(len(a)==N/2) to the first number
		"""
        for b in range(1, max_b):
            product = a * b #Finding their product
            if len(str(a) + str(b) + str(product)) > N: #If their total length is already greater than N, then it cant have excatly one of all digit from 1 to N
                break
            if is_pandigital(a, b, product, N): #Checing if pandigitial or not
                products.add(product)	#If yes, add to the set

    return sum(products) #returning the sum of the set to find the sum of all unique prouduct satisfying the pandigital property with its multiplicand and multiplier

if __name__ == "__main__":
	N = int(input())
	print(pandigital_products_sum(N))

