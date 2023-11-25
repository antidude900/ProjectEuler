def tau(num) :

    n = num;
    i = 2;
    p = 1

    while (i <= n) :
        c = 1
        while (n % i == 0):
            n//= i
            c+=1

        i+=1
        p*= c

    return p

def solution(x):
    n = 1
    d = 1

    while (tau(d) <= x) :
        n+=1
        d+= n
   
    return d

print(solution(500))