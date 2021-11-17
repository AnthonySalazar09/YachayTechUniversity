#include <stdio.h>

int main(void){

    int A;
    puts("Enter a value for A: ");
    scanf("%d", &A);

    int B;
    puts("Enter a value for B: ");
    scanf("%d", &B);

    int C=1;

    //We declare the variables "A" and "B" and put the function scanf, so that the user can
    //enter the values manually and we declare the variable "C" with value 1 because we will use this
    //variable to store the multiplications 


    for(int i=A; i<=B ; i++){

        if ( (i % 8 == 0) && (i % 12 != 0)){

        C = C*i;
        }

        //Here we use the for statement to create a range between "A" and "B", and the "i" variable
        //will travel that range. 
        // Now with the if statement we say that if the value of "i" is a multiple of 8 and is not a
        //multiple of 12, than it will be added in the "C" variable where it will be multiplied with
        //the other values that comply with the condition.
        

    }

    printf("The result of the multplication is: %d", C);
}