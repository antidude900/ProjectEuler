#"" parts are remaning parts to be explained and will explain them after exam ends
def general_sum(n,k):
    p = n//k ""
    return k*p*(p+1)//2 ""
"""
    if done /2; though only an integer value,it will give .0 value and changing it into int by int() will make some precision issue and might not solve some edge cases 
    (for me, case 2 and 3 didn't work when doing from hackerrank: https://www.hackerrank.com/contests/projecteuler/challenges/euler001/problem)
    so best way to change to floating point to integer is by // and not int()
"""


def sum_multiple(n):
    #sum of

    multiple_3 = general_sum(n,3)
    multiple_5 =general_sum(n,5)
    multiple_15 =general_sum(n,15)
    
    multiple_3_or_5= multiple_3+multiple_5-multiple_15 ""
    return multiple_3_or_5
    

n= int((input("Enter n:")))
print(sum_multiple(n-1))    
    
