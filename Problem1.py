"""
Find the sum of all the multiples of 3 or 5  below  n.
https://www.hackerrank.com/contests/projecteuler/challenges/euler001/problem?isFullScreen=true
"""

def general_sum(n,k):
    p = n//k '''finding how many multiples of k is there upto n numbers. so did n/k
              for eg:upto 40 numbers, finding how many multiple of 15, then 40/15 gives 2.66
              here the 0.66 is representing the multiple that is going to come soon i.e 45
              but as we need only the multiple that have come i.e 15 and 30, we only care abou the integer part
              i.e 2 representing that 2 multiples are present while going upto 40
              and after we found how many multiples k has upto n number say p
              then we make a natural series of p numbers and multiply by k to get series of mutliple of k as done below'''
    
    return k*p*(p+1)//2 '''The general formula for first n natural number is n(n+1)/2
                            and as we need mutliple of k, multiplying it by k
                            For eg: series of multiple of 15 upto 40 is: 15+30 i.e 1*15+2*15
                            or,15*(1+2) and sum of (1+2) is n(n+1)/2 where n=2(total items in the series)
                            and thus of 15*(1+2) is 15*n(n+1)/2 where n=2'''
    
'''
    if done /2; though only an integer value,it will give .0 value and changing it into int by int() will make some precision issue and might not solve some edge cases 
    (for me, case 2 and 3 didn't work when doing from hackerrank: https://www.hackerrank.com/contests/projecteuler/challenges/euler001/problem)
    so best way to change to floating point to integer is by // and not int()
'''


def sum_multiple(n):
    #sum of

    multiple_3 = general_sum(n,3)
    multiple_5 =general_sum(n,5)
    multiple_15 =general_sum(n,15)
    
    multiple_3_or_5= multiple_3+multiple_5-multiple_15 '''while adding mutliple of 3 and 5, we add the common multiple 2 times 
                                                          i.e as 30 is multiple of both 3 and 5, we do 30+30
                                                          so subrtacting multiple of both 3 and 5 i.e multiple of 15,
                                                          we remove the extra multiple i.e 30+30-30
                                                          and we are left with only one mutliple i.e 30'''
    return multiple_3_or_5
    
#Read the ReadMe's HackeRank Input Format to understand the below code
if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())
        print(sum_multiple(n-1)) #as said below n
    
