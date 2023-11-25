
steps = [0,1]     #starting from 0 so that each index represents the respective number 
                #and the value in that index shows the terms involved to reach 1


for num in range(2,1000000):#check for all values under 1 million

    temp = num
    length = 0
    while True:
        if temp % 2 == 0:#if even do this
            temp = temp//2

        else:#if odd do this
            temp = 3*temp+1

        length += 1 #as an term added increase the length

        if temp < num:    #if temp is less than the num of 6, it means we have already gone through that number
            steps.append(length + steps[temp])  #so that number already exists in the steps list so add that value for remaining length
                                            #and append the sum for record                                
            break                           #as found the total length break the loop and for another number(num)

print(steps.index(max(steps)))    #print the index of the element with maximum value in the steps list
