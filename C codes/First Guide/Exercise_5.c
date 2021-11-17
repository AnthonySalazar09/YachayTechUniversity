#include <stdio.h>
#include <math.h>

int main(void){

    float S;
    float n=0;
    int s=-1;

    //Declaring the three variables, "S" will be the final result of the series, "n" will be where
    //the series will be saved and our "s" will be used as a sign.

    for(float i=2; i<=100; i++){
        
        n= n+ (1/(i))*(s);
        s= s*(-1);

        //Our for will be used to travel from 2 to 100 untill it is complete, where our "i" will be the
        //divider, the division will be multiplied by "s" that in this case will be -1.
        //the "s" variable will constantly change starting from -1 to 1, each time the value from "i" changes
        //so that the condition from the series can be given.

    }

    printf("The result of the series is %f\n", n);

    S = 1 + n;

    //We will add plus 1 to the value of the previous series and the final result will be printed

    printf("The result of the series plus 1 is %f", S);
}