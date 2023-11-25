def main(n):
    lst = [0,1,2]
    
    for num in range(3,n):
        temp = num
        length = 0
        while True:
            if temp % 2 == 0:
                temp = temp//2
            else:
                temp = 3*temp+1
            length += 1

            if temp < num:
                lst.append(length + lst[temp])
                break

    return lst.index(max(lst))

print(main(1000000))