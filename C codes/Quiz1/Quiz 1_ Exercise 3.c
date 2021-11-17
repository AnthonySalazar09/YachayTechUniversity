//Quiz 1_ Exercise 3

#include <stdio.h>

int main(void){

    int arr[8] = {4, 8, 8, 8, 10, 15, 15, 19};
    int arr1[8] ={};
    int nelems = sizeof(arr) / sizeof(arr[0]);
    int add;
    int cont = 0;

    for (int i=0; i<nelems;i++){
        add = 1;
        for (int j=0;j<cont;j++){
            if(arr[i] == arr1[j]){
                add = 0;
                break;
            }
        }
        if(add){
            arr1[cont] = (arr[i]);
            cont++;
        }
    }
    printf("There are %d numbers that are different", cont);
}
