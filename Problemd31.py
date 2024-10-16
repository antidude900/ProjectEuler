"""
https://www.hackerrank.com/contests/projecteuler/challenges/euler031/problem
"""

"""
This is a dynamic programming question
"""

"""
Also talk about minimum coins problem
"""

def total_no_of_ways(n):
    results=[0]*(max(n)+1) #storing all the total no of ways all inputs for 2 reasons.
                           #
    results[0]=1 #There are two reasons for setting this up:
                 # 1.Without setting this up, the dynamic programming approach cannot be executed as the value of others should start to stack up from the initial value
                 # 2. The second reason will be explained in line 27-28
    
    coins=[1, 2, 5, 10, 20, 50, 100, 200] #total no of coins available to make other coins

    ### Here we are iterating over the coins array only one time because we store each iteration result in the array
    for i in range(8): #using all the 8 available coins to make the required no of ways 
        for j in range(coins[i], max(n)+1): #iterating from the current coins and giving its contribution to make coins greater than it
            results[j] += results[j-coins[i]] 
        """
        To compute results[j], we use the fact that if we know how many ways we can make j - coins[i], we can use one more coins[i] to form j
        To understand this, lets take an example:
        For making five pennies, we can use any way to make 3 pennnies and then add 2 pennies to make 5 pennies. This way knowing the no of ways to make 3 pennies,
        we can know how to make 5 pennies. 
        
        We get the total no of ways to make N pennies when we have reached coin greater or equal to it.
        (For pennies greater than the max value of coin, we have to iterate through all the coins to get the value of it)
        
        Lets see an example iterating upto i=0,1,2,3 i.e upto coin 10 and have a max(n) of 5

        Step 1: Coin = 1
        We process the coin 1. For each total j from 1 to 5, we update results[j]:

        For j = 1: results[1] += results[1 - 1] → results[1] += results[0] → results[1] = 1
        For j = 2: results[2] += results[2 - 1] → results[2] += results[1] → results[2] = 1
        For j = 3: results[3] += results[3 - 1] → results[3] += results[2] → results[3] = 1
        For j = 4: results[4] += results[4 - 1] → results[4] += results[3] → results[4] = 1
        For j = 5: results[5] += results[5 - 1] → results[5] += results[4] → results[5] = 1

        Here we get the total no of ways for making 1 pennie i.e 1. Here we did results[1] += results[1 - 1] → results[1] += results[0] → results[1] = 1 for the 1 pennie.
        We find how many ways we can make 0 pennnie i.e 0 and then add 1 at the end as said in line 27-28


        Step 2: Coin = 2
        Now, we process the coin 2. For each total j from 2 to 5, we update results[j]:

        For j = 2: results[2] += results[2 - 2] → results[2] += results[0] → results[2] = 2
        For j = 3: results[3] += results[3 - 2] → results[3] += results[1] → results[3] = 2
        For j = 4: results[4] += results[4 - 2] → results[4] += results[2] → results[4] = 3
        For j = 5: results[5] += results[5 - 2] → results[5] += results[3] → results[5] = 3

        Here we get the total no of ways for making 2,3, and 4 pennie as the next coin is greater than 3 and 4.

        For making 2 pennie,we did: results[2] += results[2 - 2] → results[2] += results[0] → results[2] = 2.
        We find how many ways we can make 0 pennie i.e 0 and then add 1 at the end as said in line 27-28
        Then we add the no of ways to make 2 pennie from coin 2 to the total no of ways to make 2 pennie
        (we had found the total no of ways to make 2 pennie from coin 1 in previous step. Now we add the current value to the value from previous step)

        For making 3 pennie, we did: results[3] += results[3 - 2] → results[3] += results[1] → results[3] = 2.
        We find how many ways we can make 1 pennie i.e 1 and 

        Step 3: Coin = 5
        Now, we process the coin 5. For each total j from 5 to 5, we update results[j]:

        For j = 5: results[5] += results[5 - 5] → results[5] += results[0] → results[5] = 4

        Here we get the total no of ways for making  5 pennies. Lets go through each of them well:

        
        """
        
            
    return results
    
if __name__ == "__main__":
    inputs=[int(input()) for x in range(int(input()))]
    results=total_no_of_ways(inputs)
    for x in inputs:
        print(results[x]%(10**9+7))
