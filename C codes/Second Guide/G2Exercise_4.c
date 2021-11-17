//Exercise 4
#include <stdio.h>

int main(void){

    int N;
    puts("Inserte a value for N: ");
    scanf("%d", &N);

    int upper;

    int M[N][N];

    //We declare our N that will be the size of the square matrix of M and we declare
    //the variable upper that will help in the future



    for(int i=0; i<N;i++){
        for(int j=0; j<N;j++){
        printf("Enter the value for row %d:  and column %d: ", i, j);
        scanf("%d", &M[i][j]);
        }
    }
     for(int i=0; i<N;i++){
        for(int j=0; j<N;j++){
        printf("%d ", M[i][j]); 
       
        }
             
        printf("\n");

        //We use the for to travel through the matrix and as it goes first to ask us what value we want to
        //enter and the second for is to travel through every value given and print it in the matrix form
    }
        
        upper = 1;  //We give upper the value of 1

        for(int i=0; i<N; i++){
            for(int j=0; j<N; j++){

                if(j<i && M[i][j] != 0)

                upper = 0;         
        }

        //In this case if the values or elements below the diagonal aren't zero than we can
        //say that they are not upper triangular matrix, so we have j(column)<i(row), and if
        //that is the case than the variable upper will be zero
        

    }
    if (upper == 1)
        printf("The matrix is an upper triangular");

    else
        printf("The matrix is not an upper triangular");

    //To finish we say that if the variable upper is one, than the order complies since it
    //satisfies the conditions.
     

}