def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def generate_rotations(num):
    num_str = str(num)
    rotations = [int(num_str[i:] + num_str[:i]) for i in range(len(num_str))]
    return rotations

def circular_primes_sum(limit):
    circular_primes = []
    for num in range(2, limit):
        if all(is_prime(rot) for rot in generate_rotations(num)):
            circular_primes.append(num)
    return sum(circular_primes)


limit = int(input())
print(circular_primes_sum(limit))
