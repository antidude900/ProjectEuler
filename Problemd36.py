"""
https://www.hackerrank.com/contests/projecteuler/challenges/euler036/problem
"""

"""
For converting a natural number i.e base 10 to any other base say K, we have to divide the number by K until 0. 
For every division, we record the remainder and the combined remainder from bottom to top is the number in base K.
"""

def convert(num,base):
    if num == 0: #if num = 0, the while loop below wont even run thus returning a empty string. To avoid that, we manually return 0 
        return "0"
        
    combined_remainder=''
    
    while num>0: 
        remainder = num % base
        num = int(num / base)
        #could have directly done num,remainder = divmod(num,base)
       
        combined_remainder = str(remainder) + combined_remainder #as the later remainder should be at beginning, we add the previous remainder back of the current remainder
        
    return combined_remainder    
    
    
 
if __name__ == "__main__":    
    N,K=map(int,input().split())

    total_sum = 0

    for num in range(1,N):    
        converted_num = convert(num,K)
        if str(num) == str(num)[::-1] and converted_num == converted_num[::-1]:
            #for slicing we have [start:stop:step]. If done [::step], it means we go through the whole string.
            total_sum+=num
    print(total_sum)
