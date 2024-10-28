"""
https://www.hackerrank.com/contests/projecteuler/challenges/euler037/problem
"""

def isPrime(num): 
    if num<2:
        return False
        
    for i in range(2,int(num**0.5)+1):
        if num%i == 0:
            return False

    return True

def sum_truncatable(N):
    total_sum=0
    for num in range(11,N):
        str_num = str(num) #converting to string so that we can slice it 
       
        if all(isPrime(int(str_num[i:])) for i in range(len(str_num))): #slicing it from left to right and checking if all slices are prime or not
            if all(isPrime(int(str_num[:j])) for j in range(len(str_num),0,-1)): #slicing from right to left and checking if all slices are prime or not
            
                total_sum+=num #if both the above condition satisfy, then add the number to the total_sum
        
    return total_sum

if __name__ == "__main__":
    N = int(input())
    print(sum_truncatable(N))
