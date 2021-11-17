//Exercise 3
#include <stdio.h>

int main(void){

    int M[3][5]; //We declare the matrix with row 3 and column 5

    int max; //We declare max that will be used ahead

    for(int i=0; i<3;i++){
        for(int j=0; j<5; j++){
        printf("Insert row %d and col %d: ", i ,j);
        scanf("%d", &M[i][j]);
        }
    }
    
        for(int i=0; i<3; i++){
            for(int j=0; j<5; j++){

            printf("%d ", M[i][j]);
        }
        printf("\n");

        //So first we will make the user enter the values for each row and column and then 
        //with the other for it will travel through and print those values in a matrix
    }

    for(int i=0; i<3;i++){
        for(int j=0;j<5; j++){
            if (M[i][j] > max)
            max = M[i][j];

        }

        //In this case what we do is assume that the first value will be the largest element
        //and it will travel and compare with the other values and see if those are bigger than
        //the current one given, if so it will be declared the new max
    }
    printf("The larges element of the matrix is: %d\n", max);

    for(int i=0; i<3;i++){
        for(int j=0;j<5; j++){
            if (M[i][j] == max){
                printf("The postions of the larges elements are: (%d %d)\n",i,j );
            }
         
           //In here we will travel the matrix and search for the values that are declared max, which
            //are the largest values, it will print out the position of the largest element and if there
            //is more than one, it will also print the position of it
        }
    }






}