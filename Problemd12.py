"""
What is the value of the first triangle number to have over N divisors?
https://www.hackerrank.com/contests/projecteuler/challenges/euler012/problem
"""

"""
This solution doesn't solve the problem of repeititive process for every single test cases. For that, see the v2 version
"""


# Function to count the number of divisors
def count_divisors(n):

    i = 2;
    p = 1

    while (i <= n) :  #same prime factor process as in question 3
        c = 1         #saving the no of times the number divides it(set it 1 at first for the +1 we have to do at the end)
        while (n % i == 0):
            n//= i
            c+=1

        i+=1
        p*= c    

    return p


def nth_divisible_triangular(threshold):
    n = 1 
    triangular_number = 0
    while True:
        triangular_number = n * (n + 1) // 2 #using the sum of natural numbers formulato take sum of n numbers
        if count_divisors(triangular_number) > threshold:
            return triangular_number
        n += 1
        
if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())
        print (nth_divisible_triangular(n))
