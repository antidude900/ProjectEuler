#combination formula(to understand more go https://www.youtube.com/watch?v=ivYXjESJ_zE)
from math import factorial

total = factorial(40)//(factorial(20)*factorial(40-20)) 
print(total)


#but what if not a square grid?
#then use this algorithm below(https://www.youtube.com/watch?v=ZEYG4tpI4U4)

#import numpy as np
#
#grid = np.full((21,21), 1,dtype=np.int64) #need to make it one size for both rows and column
#
#
#for i in range(1,21):
#	for j in range(1,21):
#		grid[i][j] = grid[i-1][j]+grid[i][j-1]
#
#print(grid[20][20])
