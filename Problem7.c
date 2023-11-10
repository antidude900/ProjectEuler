#include <stdio.h>
#include <math.h>

int main(){
    int n=1,num =2; //setting 2 as the 1st term
    while (n !=10001)
    {
        num++;  //going to another number for checking
        int isPrime = 1;
        for (int i = 2;i <=sqrt(num); i++)  //checking
        {

            if (num%i == 0){
                isPrime = 0;
                break;
            }
        }

        if (isPrime){   //if true then we found another term so increase the nth term by 1
            n++;
        }



    }
    printf("%d\n",num);



}
