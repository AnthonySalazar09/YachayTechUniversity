//Quiz 1_ Exercise 1

#include <stdio.h>
#include <stdlib.h>

int main(void){
  int x;
  int y;
  int z;
  int cont;

  printf("a0: \n");
  scanf("%d", &x);
  printf("a1: \n");
  scanf("%d", &y);
 
  for(int cont=1;cont<=20;cont++){
      z=x+y;
      printf("%d\n",z);
      x=y;
      y=z;
    }
}