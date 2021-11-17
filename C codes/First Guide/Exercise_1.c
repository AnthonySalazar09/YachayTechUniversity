#include <stdio.h>
#include <math.h>

int main(void){

    double x_1;   
    puts("Enter a value for x_1: ");
    scanf("%lf", &x_1);
    double y_1;
    puts("Enter a value for y_1: ");
    scanf("%lf", &y_1);
    double x_2;
    puts("Enter a value for x_2: ");
    scanf("%lf", &x_2);
    double y_2;
    puts("Enter a value for y_2: ");
    scanf("%lf", &y_2);

    //We first start by declaring our values and later add the function scanf
    //so that the user can manually enter and assign
    //the values for x_1,y_1,x_2 and y_2


    int distance_1;  
    int distance_2;

    //Next we declare our values for the distance we are going to use since in this case we
    //are going to use the Euclidean formula in order to calulate the distance between two points, 
    //that will be the first point (x_1.y_1) and the origen (0,0), and we do the same with the
    //second point (x_2,y_2) and the origen (0,0).
    //Previously we implemented the math library so we can use some operations.

    distance_1 = sqrt(((x_1*x_1)-0) + ((y_1*y_1)-0));
    distance_2 = sqrt(((x_2*x_2)-0) + ((y_2*y_2)-0));

    if (distance_1 < distance_2){

        puts("The two-dimensional values (x_1, y_1) are closer to the origen");
    }
    else{

        puts("The two-dimensional values (x_2, y_2) are closer to the origen");
    }

    //Now as we can see, we are going to get the value of the two distances that we calculated
    //and from there with if we see that the distance with the lowest value will be the
    //point that is closest to the origen


}