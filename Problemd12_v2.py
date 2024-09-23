"""
Same as Problem12.py, just optimized it for multiple test cases
"""

def count_divisors(n):
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
    
def highly_divisible_triangular(threshold, triangular_numbers, divisors_count):
    n = len(triangular_numbers) + 1
    while True:
        triangular_number = n * (n + 1) // 2
        divisor_count = count_divisors(triangular_number)
        
        triangular_numbers.append(triangular_number)
        divisors_count.append(divisor_count)
        
        if divisor_count > threshold:
            return triangular_number
        n += 1

def main():

   
    import sys
    input = sys.stdin.read
    data = input().split()
    
    t = int(data[0])  # Number of test cases
    test_cases = [int(data[i]) for i in range(1, t + 1)]  # Extract all test cases
    
    triangular_numbers = []
    divisors_count = []
    
    results = []
    
    for threshold in test_cases:
        for i in range(len(divisors_count)):
            if divisors_count[i] > threshold:
                results.append(str(triangular_numbers[i]))
                break
        else:
            results.append(str(highly_divisible_triangular(threshold, triangular_numbers, divisors_count)))

    print("\n".join(results))

if __name__ == "__main__":
    main()
