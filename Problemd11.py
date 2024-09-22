"""
https://www.hackerrank.com/contests/projecteuler/challenges/euler011/problem
"""

def product_of_four(lst): #for carrying out product part of the adjacent numbers
	
    max_product = 0
    for i in range(len(lst) - 3):
        product = lst[i] * lst[i + 1] * lst[i + 2] * lst[i + 3]
        if product > max_product:
            max_product = product
    return max_product


    
def greatest_product(grid):
	
    max_product = 0
    n = len(grid)
    
    # Check horizontal and vertical products
    for i in range(n):
        # Horizontal
        max_product = max(max_product, product_of_four(grid[i]))
                                       #sending a row to find the greatest product of four adjacent numbers of the row
                    
        # Vertical
        col = [grid[j][i] for j in range(n)] #making the column constant and row changing to find all the numbers of the row
        max_product = max(max_product, product_of_four(col))
                                       #sending a column to find the greatest product of four adjacent numbers of the column

    # Check diagonal products
    for i in range(n - 3):
        for j in range(n - 3):
            # Top-left to bottom-right
            diag1 = [grid[i + k][j + k] for k in range(4)] #increasing both row and column linearly to get diagonal starting from (i,j) to (i+3,j+3)
            max_product = max(max_product, product_of_four(diag1))

            # Bottom-left to top-right
            diag2 = [grid[i + 3 - k][j + k] for k in range(4)] #here the point i won't be the starting point of the diagonal but the starting point of the square 
							       #which extends horizontally towards right and vertically downwards making a 4*4 square. 
							       #Then we take the diagonal of the square from bottom left to top-right
            max_product = max(max_product, product_of_four(diag2))

    return max_product


if __name__ == '__main__':
    grid = []

    for _ in range(20):
        grid.append(list(map(int, input().rstrip().split())))
    print(greatest_product(grid))

"""
if given the string of numbers in a single input:
num=input().strip()
num = list(map(int, num))

size = 20
grid = [num[i * size:(i + 1) * size] for i in range(size)]
	#slicing num from starting point i*size to (i+1)*size thus making a sublist of length "size"
print(greatest_product(grid))
"""
