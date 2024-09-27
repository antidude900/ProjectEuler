
import math

def sum_factorial(n):
    factorial = str(math.factorial(n))
    sum  = 0
    for i in range(len(factorial)):
        sum+= int(factorial[i])
    return sum
        


if __name__ == "__main__":
    t=int(input())
    
    for _ in range(t):
        N = int(input())
        print(sum_factorial(N))
