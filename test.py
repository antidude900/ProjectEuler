def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def consecutive_primes(a, b):
    n = 0
    while is_prime(n**2 + a*n + b):
        n += 1
    return n


max_primes = 0
coefficients = None

for a in range(-999, 1001):
    for b in range(2, 1001):
        if is_prime(b): #another property is that the one producing the highest consecutive
                        #no of prime has a prime b
                        #it just only saves 0.3 second
                        
            num_primes = consecutive_primes(a, b)
            if num_primes > max_primes:
                max_primes = num_primes
                coefficients = (a, b)

product = coefficients[0] * coefficients[1]

print("Coefficients:", coefficients)
print("Product:", product)
