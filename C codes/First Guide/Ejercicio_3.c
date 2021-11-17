#include <stdio.h>
#include <math.h>

int main(void){

    float S;
    float n=0;

    //We start by declaring our two values, S will be the total of the series we are being asked to do
    //and n will be used to save the total of the addition of the series we are going to do

    for(float i=2; i<=100; i++){
        
        n= n+ 1/i;
    }

    printf("The result of the series is %f\n", n);

    //We use the for statement for in order to start from the number 2 assigned and 
    //make it travel each number until it gets to 100, "i" in this case will be the value that will
    //have those numbers mentioned and will be our divider of "1/i" and each value from the division will
    //be adding up to our "n" value that we have defined earlier

    S = 1 + n;

    printf("The result of the series plus 1 is %f", S);

    //And now from the total of our "n" value given we add the plus 1 and save it in our variable "S"
    //So it can finally print
}