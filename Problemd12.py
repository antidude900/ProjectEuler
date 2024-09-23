#see https://www.youtube.com/watch?v=9WX8_qluq7I&t=491s upto 2:46 to understand algorithm
def no_of_factors(n) :

    i = 2;
    p = 1

    while (i <= n) :  #same prime factor process as in question 3
        c = 1         #saving the no of times the number divides it(set it 1 at first for the +1 we have to do at the end)
        while (n % i == 0):
            n//= i
            c+=1

        i+=1
        p*= c    

    return p


n = 1    #nth term
num = 1    #the traingular number

while (no_of_factors(num) <= 500) : #saying over 500 dividers so <=
    n+=1    #as next term,increasing the nth term
    num+= n   #the traingular number increases by nth term(1+2+3+4+5+6+7+8 = 28 as said in the question)

print(num)
