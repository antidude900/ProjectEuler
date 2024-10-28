"""
https://www.hackerrank.com/contests/projecteuler/challenges/euler038/problem
"""

#Here N is the limit of multipliers M and K is the range/length of pandigital number i.e 1-K pandigital number.
def find_numbers(N, K):
    for M in range(2, N + 1): #Looking for multipliers from 2 to N. Not from 1, because in ouput example, 1 was not given though multiplier 1 will always give pandigital
        total_num = "" 
        digit = 1

        while len(total_num) < K: #as we need 1-K pandigital number i.e total length of K, we make the required number until it reaches the K length
            num = M * digit #we multiply M with natural numbers to get the digits of the pandigial number 
            total_num += str(num) 
            digit += 1

        if sorted(total_num) == [str(i) for i in range(1, K+1)]:
            """
            In problem 32, we checked for pandigital using set because we were sure that the number doesnt exceed length of the pandigital number.
            But here, we dont check that. suppose for K=8, we have total_num=152434678, a length of 9.
            Here if we applied the same set way to check for pandigital, we will get 15243678 which will we equal to set of range 1 to 8.
            So if we wanted to still apply the set way, we would also have to check the length of the number as well like this:
            if len(total_num)==K and set(total_num) == set(map(str, range(1, K+1))):
            This first ensures that there are no duplicate numbers and then checks if the given number in pandigital or not
            """
            print(M)


if __name__ == "__main__":
    N,K= map(int, input().split())
    find_numbers(N, K)
