import numpy as np

grid = np.full((21,21), 1,dtype=np.int64)


for i in range(1,21):
	for j in range(1,21):
		grid[i][j] = grid[i-1][j]+grid[i][j-1]

print(grid[20][20])