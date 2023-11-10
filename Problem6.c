#include <stdio.h>

int main(){
    int n =100;
    long int sum_square = 0,square_sum =0;

    sum_square = n*(n+1)*(2*n+1)/6; //formula for sum we read in sequence and series
    square_sum = n*(n+1)/2;

    square_sum = square_sum*square_sum;
    printf("%ld",square_sum - sum_square);



}
