def convert(num,base):
    if num==0:
        return 0
        
    combined_remainder=''
    while num>0: 
        remainder=num%base
        num=int(num/base)
       
        combined_remainder=str(remainder)+combined_remainder
    return combined_remainder    
    
    
 
if __name__ == "__main__":    
    N,K=map(int,input().split())

    total_sum = 0

    for num in range(1,N):    
        converted_num = convert(num,K)
        if str(num) == str(num)[::-1] and converted_num == converted_num[::-1]: 
            total_sum+=num
    print(total_sum)
