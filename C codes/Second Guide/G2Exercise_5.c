//Exercise 5
#include <stdio.h>
#include <string.h>

//We include the library string in order to use the strlen() function

int main(void){

    char str[100]; //We declare our string with 100 characters
    puts("Enter a string: ");
    gets(str); //It prints the string given by the user

    

    for(int i=0; i < strlen(str); i++){
        if (str[i]==' ' && str[i+1]== ' '){
            for (int j=i; j < strlen(str); j++)
            str[j] = str[j+1];
            i--;
        }

        //We use strlen() to get the length of the string and it will travel until the end of the length
        //the if statement will check if there is a space after a space and if it is true than it will
        //travel and check in each loop that if there is an extra space, than it will elimnate a space
        //,the loop will continue until there is only one space

    }

    printf("%s", str);
}