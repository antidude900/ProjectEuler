def find_numbers(N, K):
    for M in range(2, N + 1):
        total_num = ""
        digit = 1

        while len(total_num) < K:
            num = M * digit
            total_num += str(num)
            digit += 1

        if sorted(total_num) == [str(i) for i in range(1, K+1)]:
            print(M)


if __name__ == "__main__":
    N,K= map(int, input().split())
    find_numbers(N, K)
