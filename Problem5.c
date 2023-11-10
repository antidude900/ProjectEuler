#include <stdio.h>

int main(){
    int i =1,isResult = 1;
    while (1)   //running forever loop
    {
        isResult = 1;
        for (int j=1;j<=20;j++){    //dividing by numbers 1 to 20
            if (i%j !=0){
                isResult = 0;   // if a single divider fails to evenly divide then go to new number
                break;
            }

        }

        if (isResult)   //if found the result the number then stop
            break;
        i++;

    }
    printf("%d",i);



}
