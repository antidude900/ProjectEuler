"""
What is the sum of the digits of the number 2^^n?
https://www.hackerrank.com/contests/projecteuler/challenges/euler016/problem
"""
def sum_of_pow_2(n):    
    sum=0
    
    num=str(pow(2,n)) #for 2 to the power 1000
                    #and changing into string so that we can iterate through it

    for i in range(len(num)):
        sum+=int(num[i]) #adding all the digits
    return sum
	
    
if __name__ == "__main__":
    t=int(input())
    
    for _ in range(t):
        n = int(input())
        print(sum_of_pow_2(n))
