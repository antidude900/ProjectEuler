n = 100

sum_square = n*(n+1)*(2*n+1)/6; #formula for sum we read in sequence and series
								#fun fact: I came up with this idea instead of looping in first thought!
square_sum = n*(n+1)/2;

square_sum = square_sum*square_sum;
print(square_sum - sum_square);
