//Quiz 1_ Exercise 2
#include <time.h>
#include <stdlib.h>
#include <stdio.h>

int main(void){

    int n, r1,r2,r3;      // Returns a pseudo-random integer between 0 and RAND_MAX.
    time_t t;
    while (1){
        srand((unsigned) time(&t));   // Initialization, should only be called once.
        n = rand() % 900 + 100;
        r1 = (int)(n/10) % 10;
        r2 = (int)(n/100);
        r3 = n % 10; 
        printf("%d\n", n);
        if(r2+r3 == r1){
            break;
        }
    }
    
}
