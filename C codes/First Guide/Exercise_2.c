#include <stdio.h>

int main(void){
    int A; 
    puts("Enter a value for A: ");
    scanf("%d", &A);
    int B;
    puts("Enter a value for B: ");
    scanf("%d", &B);
    int C;
    puts("Enter a value for C: ");
    scanf("%d", &C);
    
    //We first declare that A, B and C are going to be int numbers and use the scanf function
    //so that the user can assign it's value manually

    if (A < B+C && B < A+C && C < A+B){
        printf("The values given for A B y C can be sides for a triangle");
    }
    else {
        printf("The values given can not be sides for a triangle");
    }
}
   //After the user has assigned the respective values to each letter, we use the if statement
   //so we can say that if each value of the letters given is less than the addition of the other two
   //values, we can than say the the order has been fulfilled and we can say that they can be sides for
   //a triangle and in the case that just one letter doesn't comply with the order than we say that
   //the sides can't be for a triangle.