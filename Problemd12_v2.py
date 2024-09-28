"""
Same as Problem12.py, just optimized it for multiple test cases
"""

"""
Note: 
As you have got familiar with the questions with multiple test cases where the result from the previous test case can be used in others too,
it is clear that the different is those single case and multiple case solution was that we used a array to store the results which could be used by all test cases
So from now on, I will only be writing multiple case solutions if exists
and to change it into single case solution, just remove the shared array and directly give the required result
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
    
    t = int(input())  # Read number of test cases
    test_cases = [int(input()) for _ in range(t)]  # Read input values
    
    triangular_numbers = []
    divisors_count = []
    
    results = []
    
    for threshold in test_cases:
        for i in range(len(divisors_count)):
            if divisors_count[i] > threshold:
                print(triangular_numbers[i])
                break
        else:
            print(highly_divisible_triangular(threshold, triangular_numbers, divisors_count))

if __name__ == "__main__":
    main()
