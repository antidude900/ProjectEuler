"""
https://www.hackerrank.com/contests/projecteuler/challenges/euler019/problem
"""


"""
Found this solution on HackerRank Discussion and it's very interesting. So using the same solution:

Concept: Every 400 years, the calendar cycle repeats. Therefore, by finding
all sunday-the-firsts (STFs) in any range of 400 years, one can deduce the
number of STFs in any other range.

For convenience, we can calculate the range 2000-1-1 to 2399-12-31 since it
will allow us to find any year's place in the cycle by simply taking the year
mod 400. Herafter "relative year" refers to the year mod 400 for starting years
and start year mod 400 + (end year - start year) for ending years.

The day of the week for any given gregorian calander date can be calculated
using a simple formula (see the weekday(y, m, d) function below). Since we only
care about STFs, we only need to check the first of the month of each month.

The results are stored in "lookup" as a boolean list, where each value represents
a month from relative year 0 (e.g. 2000 or 11804211600) through relative year 399
(e.g. 2799 or 2810399). True indicates the first of the month was
a Sunday.

Since the end date is never more than 1000 years, 12 months and 31 days from the
start year, we can repeat this range by 4 for convenience. Thus, the relative
start and end dates always fall within the range of the lookup list.

The convenience function ym(y, m) takes a relative year and month and returns the
associated index in the lookup list.

Finally, given a start and end date, we simply find the relative years for those
dates, and sum the values of the lookup list between the dates (inclusive).

"""

from math import floor

def weekday(y, m, d):
    """
    y: year
    m: month (1=March - 12=February of following year)
    d: day
    
    return: day of week (0=Sunday - 6=Saturday)
    
    reference: https://cs.uwaterloo.ca/~alopez-o/math-faq/node73.html#:~:text=Here%20is%20a%20standard%20method,the%20day%20of%20the%20month.
    by Alex Lopez-Ortiz
    """
    
    ## adjest the month number, shifting Jan and Feb back one year
    m -= 2
    if m < 1:
        m += 12
        y -= 1
    ## Split the year into the c=Century and y=two digit year
    c, y = divmod(y, 100)
    return (d + floor(2.6*(m) - .2) - 2 * c + y +y//4 +c//4) % 7

def ym(y, m):
    """
    y: year
    m: month
    
    return: index of the year, month in the lookup list
    """
    return 12*y + (m-1)

 
def span_count(y0, m0, y1, m1):
    """
    y0: start year
    m0: start month
    y1: end year
    y2: end month
    
    return: total STFs in the given range
    """
    ## find the distance from y0 to y1
    y1 -= y0
    ## find the relative starting year
    y0 %= 400
    ## find the relative ending year
    y1 += y0
    ## sum the values between the two dates (inclusive)
    return sum(lookup[ym(y0, m0):ym(y1, m1) + 1])



## defining the lookup
global lookup
lookup = []
for y in range(400):
    for m in range(1, 13):
        lookup.append(weekday(y, m, 1) == 0)
## repeat the lookup so that relative start/end years always fall within
## the range of the lookup list
lookup = lookup*4



for i in range(int(input())):
    y0, m0, d0 = [int(n) for n in input().split(' ')]
    y1, m1, d1 = [int(n) for n in input().split(' ')]
    ## if the start date is after the first of the month, we can just start on
    ## the first of the following month
    if d0 > 1:
        m0 += 1
        if m0 == 13:
            m0 = 1
            y0 += 1
    ## find the result
    print(span_count(y0, m0, y1, m1))

