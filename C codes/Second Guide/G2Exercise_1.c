//Exercise 1 
#include <stdio.h>
#include <math.h> //We include math for some operations ahead

int main(void){

    float arr[10];
    float sum=0;
    float sum1=0;
    float avg;
    float variance;
    float std;

    //We declare the array with a value of 10, the two sums we will use, the average, the variance
    //in order to be able to calculate the standard deviation, all of these as floats

    for (int i=0; i<10; i++){
        puts("Enter a float value: ");
        scanf("%f", &arr[i]);
    }
    printf("The values of the array are: \n");
    for(int i=0; i<10; i++)
    printf("%f\n", arr[i]);

    //We have the user enter the 10 float values we are going to use to calculate what is asked, and then
    //we will print the values of the arrays that are inserted
    for(int i=0; i<10; i++)
    sum = sum + arr[i];

    printf("The sum of the 10 float numbers is: %f\n", sum);

    //This for travels through the array, it starts to add each value untill it has traveled and added
    //the 10 values given

    avg = sum/10.0;
    printf("The average of the numbers is: %f\n", avg);

    //Here we calculate the average with the total of the sum and divide by the total of numbers
    //which in this case is 10
    for (int i=0;i<10;i++){
        sum1 = sum1 + pow((arr[i]-avg),2);
    }

    variance = sum1/10.0;

    std= sqrt(variance);

    //In order to calculate the standard deviation we start by using the for to travel through the array
    // and start to add the values minus their avg to the power of two ((arr[i]-10)^2)
    //Now to calculate the variance, we divide the total of the addition of sum1 and divide it by 10
    //and to get the value of the std we take the square root of the variance.

    printf("The standard deviation is: %f", std);
}
