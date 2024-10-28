def isPrime(n):
    num = int(n)
    
    if num<2:
        return False
        
    for i in range(2,int(num**0.5)+1):
        if num%i == 0:
            return False

    return True

def sum_truncatable(N):
    total_sum=0
    for num in range(11,N):
        str_num = str(num)
       
        
        if all(isPrime(str_num[i:]) for i in range(len(str_num))):
            if all(isPrime(str_num[:j]) for j in range(len(str_num),0,-1)):
            
                total_sum+=num
        
    return total_sum

if __name__ == "__main__":
    N = int(input())
    print(sum_truncatable(N))
