from math import factorial

if __name__ =="__main__":
    N = int(input())
    total_sum=0
    
    for i in range(10,N): #Single digits are not considered as sum, so starting from 10
        sum_of_digits = sum([factorial(int(digit)) for digit in str(i)])
      
        if sum_of_digits%i ==0:
            total_sum+=i
            
    print(total_sum)
