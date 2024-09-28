"""
https://www.hackerrank.com/contests/projecteuler/challenges/euler022/problem
"""

if __name__ == "__main__":
    # for mapping alphabet with their position value [here position valus is given by index but as index starts from 0, need to add 1 to index value to get true positional value]
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" 

    t= int(input())
    names  = sorted(input() for _ in range(t)) #sorting namesin alphabetical order as per question
    
    t = int(input()) #taking input for the Q queries
    for i in range(t):
        name = input()
        total = sum(alphabet.index(x)+1 for x in name)  #adding positional value of each alphabet
        total *=names.index(name)+1 #multiplying by the positional value of the given name in the list of names 
        print(total)
        
