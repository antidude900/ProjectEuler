"""
https://www.hackerrank.com/contests/projecteuler/challenges/euler030
"""

#seeing the example in the question, you might get confused thinking that the length of the number should also be equal to N but it doesnt have to
#for eg:194979 also satisfies the condition for N=5 and this result is accepted though len(194979)>5
def sum_of_N_power_equal_to_num(N):
    total_sum = 0 #to take sum of all the numbers satisfying the given condition

    #as we need sum of digits raised to power B, we should have atleast 2 digits for the sum(otherwise a single digit cant be considered as a sum)
    #So starting with 10 and taking a upper limit which will be sufficient i.e 10^6
    for num in range(10, 10**6):
        temp = num
        sum = 0

        #taking out each digit of the number from back by using the remainder by 10 method, powering it with N and then adding to the sum
        while temp > 0:
            last_digit = temp % 10
            sum += last_digit**N
            temp = temp // 10

        #then checking if the sum is equal to its respective number
        if sum == num:
            total_sum += num

    return total_sum

if __name__ == "__main__":
    N = int(input())
    print(sum_of_N_power_equal_to_num(N))
