'''
The smallest multiple between an interval is the lcm of the interval so we find the lcm of the interval

Here instead of finding lcm of the whole part itself we divide it into smaller parts, a pair of two and find the pair's lcm
and then making pair of the lcm of the previous pair and the another number, we find lcm of that pair too
Its like the sum thing too, to find sum from 1 to 4 we can do 1+2 i.e 3 and then add 3+3 i.e 6 then 6+4 we get 10
also to find lcm we know the formula lcm(a,b) = a*b/gcd(a,b)
so in the first iteration taking lcm of LCM ie 1 and i ie 2, we do lcm = 1*2/gcd(1,2) giving lcm of 1 and 2 i.e 2
and then in second iteration taking lcm of LCM i.e 2 and i i.e 3, we do lcm = 2*3/gcd(2,3)
giving us the lcm of lcm(1,2) with 3 and then that with 4 and so on till 20

'''


from math import gcd
LCM =1

for i in range (2,21):
	LCM = int((LCM*i) / gcd(LCM,i))

print(LCM)

'''
If wont let use other library such as math make your own gcd function like this:
(but theres a high chance they will let us use math function for functions like sqrt)

def gcd(x, y):

   if (x == 0):
      return y
   

   return gcd(y % x, x)

or this 

while(n1!=n2):

    if(n1 > n2):
        n1 -= n2
    else:
        n2 -= n1

gcd = n1

Note: the second one is abit faster than first one

'''
