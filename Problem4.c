#include <stdio.h>

int palindrome(long int num)    //Checks if palindrome or not
{
    long int rev = 0, temp = num;

    while(temp != 0)
    {
        rev =rev*10+(temp%10);
        temp = temp/10;
    }
    if (num  == rev)
        return 1;
    else
        return 0;

}


int main(){
    long int largest = 0, num =0;

    for (int i=100;i<=999;i++)    //loop to form numbers from two 3 digit numbers
    {
        for (int j = 100;j<=999;j++)
        {
            num = i*j;

            if (palindrome(num) && num > largest) //if palindrome and the largest till now update it as the largest palidrome
                largest = num;

        }

    }
    printf("%ld",largest);



}
