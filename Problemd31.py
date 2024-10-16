"""
https://www.hackerrank.com/contests/projecteuler/challenges/euler031/problem
"""

"""
This is a dynamic programming question
"""

"""
There is another question similar to it called minimum coin problem where we have to make the certain amount of money using the given coins.
"""

def total_no_of_ways(N):
    results=[0]*(N+1) #storing all the total no of ways of all inputs upto max_input
                           
    results[0]=1 #When doing results[j-coins[i]] in the below nested loop, when j = coins[i] we get results[0]
                 #meaning we are using the same coin as the required pennie. Thus we only have one way to make the pennie i.e using the single same coin.  
    
    coins=[1, 2, 5, 10, 20, 50, 100, 200] #total no of coins available to make other coins

    ### Here we are iterating over the coins array only one time because we store each iteration result in the array
    for i in range(8): #using all the 8 available coins to make the required no of ways 
        for j in range(coins[i], N+1): #iterating from the current coins and giving its contribution to make coins greater than it
            results[j] += results[j-coins[i]] 
        """
        To compute results[j], we use the fact that if we know how many ways we can make j - coins[i], we can use one more coins[i] to form j
        To understand this, lets take an example:
        For making five pennies, we can use any way to make 3 pennnies and then add 2 coin to make 5 pennies. Also we can use any way to make 4 pennies adn then add 1 coin.
        The first one will give us ways to make 5 pennie from 2 coin(meaning the way includes using one or more 2 coin) and the second one from 1 coin.
        The final one will be using the 5 coin itself.  
        
        We get the total no of ways to make N pennies when we have reached coin greater or equal to it. 
        (For pennies greater than the max value of coin, we have to iterate through all the coins to get the value of it)
        
        Lets see an example iterating upto i=0,1,2,3 i.e upto coin 10 and have a max(n) of 5

        Step 1: Coin = 1
        We process the coin 1. For each j from 1 to 5, we update results[j]:

        For j = 1: results[1] += results[1 - 1] → results[1] += results[0] → results[1] = 1
        For j = 2: results[2] += results[2 - 1] → results[2] += results[1] → results[2] = 1
        For j = 3: results[3] += results[3 - 1] → results[3] += results[2] → results[3] = 1
        For j = 4: results[4] += results[4 - 1] → results[4] += results[3] → results[4] = 1
        For j = 5: results[5] += results[5 - 1] → results[5] += results[4] → results[5] = 1

        Here we get the total no of ways for making 1 pennie i.e 1. We did results[1] += results[1 - 1] → results[1] += results[0] → results[1] = 1.
        It shows making the 1 pennie from the single 1 coin.


        Step 2: Coin = 2
        Now, we process the coin 2. For each j from 2 to 5, we update results[j]:

        For j = 2: results[2] += results[2 - 2] → results[2] += results[0] → results[2] = 2
        For j = 3: results[3] += results[3 - 2] → results[3] += results[1] → results[3] = 2
        For j = 4: results[4] += results[4 - 2] → results[4] += results[2] → results[4] = 3
        For j = 5: results[5] += results[5 - 2] → results[5] += results[3] → results[5] = 3

        Here we get the total no of ways for making 2,3, and 4 pennie as the next coin is greater than 3 and 4.

        For making 2 pennie,we did: results[2] += results[2 - 2] → results[2] += results[0] → results[2] = 2.
    
        Then we add the no of ways to make 2 pennie from coin 2 to the total no of ways to make 2 pennie
        (we had found the total no of ways to make 2 pennie from coin 1 in previous step. Now we add the current value to the value from previous step)

        For making 3 pennie, we did: results[3] += results[3 - 2] → results[3] += results[1] → results[3] = 2.
        Thus we got the total no of ways of making 1 pennie i.e making 3 pennie from 2 coin and then added it with making 3 pennie from 1 coin.
        Similarly for 4 pennie....
        

        Step 3: Coin = 5
        Now, we process the coin 5. For each j from 5 to 5, we update results[j]:

        For j = 5: results[5] += results[5 - 5] → results[5] += results[0] → results[5] = 4

        Here we get the total no of ways for making  5 pennies. Lets go through each of them well:
        In the step 3, we got no of ways to make 5 pennies from 5 coin. We added that with no of ways to make 5 pennies from 1 and 2 coin which we got from step 1 and 2 respectively.
        """
        
            
    return results
    
if __name__ == "__main__":
    inputs=[int(input()) for x in range(int(input()))]
    results=total_no_of_ways(max(inputs))
    for x in inputs:
        print(results[x]%(10**9+7))
