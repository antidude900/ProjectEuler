#include <stdio.h>

int main(){

    int sum = 0;

    for (int i = 1;i<1000;i++){ // checking all numbers less than 1000
        if (i%3==0 || i%5==0)   // if divisible by either 3 or 5, then include it in the sum
            sum+=i;
    }
    printf("%d",sum);
}
