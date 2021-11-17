//Exercise 2
#include<stdio.h>
#include<math.h> 

int main(void){
    int N;
    puts("Inserte a value for N: ");
    scanf("%d", &N); 

    float arr[abs(N)];
    //We let the user enter the value of N which will be the size of the array
    //And we put abs(N) so if we put a negative value, it will accept it

    printf("The array is: \n");
    if (N < 0 ){
        for (int i = 0; i < abs(N) ; i++){ //We put abs(N) so it accepts the negative value and run the loop
            arr[i] = 1/pow(2,i);
            printf("%f \n", arr[i]);
        }
    }
    //The if statement says if N<0 than the 2 power of i that will increase untill it reaches N 
    //we put 1/pow(2,i) since it's the same as (2)^(-n)
    else {
        for (int i = 0; i < N ; i++){
            arr[i] = pow(2,i);
            printf("%f \n", arr[i]);
        }
    }
    //And if the first condition doesn't comply than it automatically will be that N>0, so in 
    //this case the pow(2,i) is the same as (2)^(n), and the i will keep increasing untill 
    //it reaches N
}