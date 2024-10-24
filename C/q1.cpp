#include <stdio.h>
#include <string.h>

int main(){
    char nome1[20];  
    char nome2[20];

    scanf("%s", nome1);
    scanf("%s", nome2);

    if (!strcmp(nome1,nome2)){
        puts("São Iguais!");
    } else {
        puts("São Diferentes");
    }

    return 0;
}
