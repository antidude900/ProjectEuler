"""
https://www.hackerrank.com/contests/projecteuler/challenges/euler018/problem
"""

"""
Before going through this program, lets understand the algorithm:

We are given a traingle like this:

3
7 4
2 4 6
8 5 9 3

This is changed to a 2d array. Thus 3 is at (0,0). 
The first coordinate denotes the level of the traingle and the second coordinate denotes the index of the number at that level.
If we want to go the left we just increase the level without changing the index
If we want to go to the right we increase both the level and index
as the deeper level has always a index more than the adjacent upper level, increasing index is always safer and there is not risk of going out of bound

We can move to the lowest level going left and right(for eg: left right right or left right left)
Supoose we went left right and now we are in (2,1). from here we can go left and right i.e ton 8 or 9.
we go to both and take sum with the parent node 4 i.e 4+5 =9 and 4+9=13. We take the max of the sum and store 13 as the max_sum of 4 upto the lowest level
Now lets go one level up so we have 7 (1,0)(left right).
Here we have the max sum of the right branch but we need of left too. 
So we go left i,e (2,0) and reach 2. We carry same process as of 4 and find max sum of 2 which 2+8 = 10
Now we go back to 7 and now we have both the left and right branch max_sum. we find max among them i.e 13(out of 10 and 13) and thus max sum of 7 is 20(13+7)

Here, you can seen for the max sum of 7, we went so deep down both right and left and then after one gets its value, it again goes back up.
This is the process known as recursion in we recurse our way deep inside until we get the values needed.

Now, after getting the max sum of 7, we get the max sum of left branch of 3 i.e 20(20+3).
So now we do the same process of recursion for the right branch also.
Notice that while recursing on the right branch of 3, if we go right left we get to (2,1).
But we had already calculated the max_sum of (2,1) while recursing the left branch of 3.
This is why we save this results in a 2d list so that we can use it later if the same path is taken next time too. 

"""


def max_sum(triangle, level, index, max_sums):

	#lets take example of (2,1) for understanding process
	
    # If reached the bottom of the traingle, give the value there (as the max_sum of the number at bottom will be the number itself)
	#[If goes left gives 5 and if goes right gives 9]
    if level == len(triangle) - 1:
        return triangle[level][index]
	    
    # If already calculated the max_sum of (length,index), use that
	#[same condition when (1,1) uses (2,1)]
    if max_sums[level][index] != -1:  #we have defaulted every sum to -1 to denote that we haven't got the max_sum of that (length,index)
        return max_sums[level][index]
    
    # go both left and right of (level,index) 
	# we went to (3,1) and (3,2)
    left_path_sum = max_sum(triangle, level + 1, index, max_sums)
    right_path_sum = max_sum(triangle, level + 1, index + 1, max_sums)
    
    # Add the max sum among the left and right with the parent node to get the max sum of the parent node
	#for (1,0) we added 13(max among 9 and 13) and added to 7 and got 20
    max_sums[level][index] = triangle[level][index] + max(left_path_sum, right_path_sum)
    
    return max_sums[level][index]

# Driver code for multiple test cases
for _ in range(int(input())):
    triangle = []
    levels =  int(input())
    
    for i in range(levels):
        triangle.append(list(map(int, input().split()))) #for eg we get "2 4 6" so spliting we get ["2","4","6"] and then change them to int and append to the traingle 
    
    max_sums = [[-1] * (i + 1) for i in range(levels)]
    # The maximum path sum starts from the top of the triangle (level 0, index 0)
    result = max_sum(triangle, 0, 0, max_sums) #finding maximum sum of top
    
    print(result)





"""
#If given traingle in this form:

traingle = """75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23"""

#handle it like this:

traingle =  [x.split() for x in traingle.split("\n")]
path = []
for x in traingle:
	path.append([int(y) for y in x])
"""
