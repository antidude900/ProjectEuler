#include <stdio.h>

int main(){

    long long int num = 600851475143, i =2;// starting with number 2 to check all prime factors of num


    while (i <= num){   //we will have factors until the number we divide with exceeds the number itself
        if (num%i == 0) // checking if it is a factor
            num /= i;   // if factor decrease the num by factor so the num goes on shrinking until the numb is not divisible by the factor
        else
            i += 1; //if not a factor go to another number for checking
    }
    printf("%lld",i);


}
