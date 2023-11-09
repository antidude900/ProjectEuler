#include <stdio.h>

int main(){

    long int n1 = 1,n2 = 2,temp = 0,sum = 0;    // temp for exchanging variables between n1 and n2

    while (n2 <= 4000000){  // checking all fibo numbers until number exceeds 4 million
        if (n2%2 == 0)      // if even include it in the sum
            sum += n2;
        temp = n2;          // see the next two consecutive terms of the fibo seq
        n2 = n1 + n2;
        n1 = temp;

    }
    printf("%d",sum);



}
