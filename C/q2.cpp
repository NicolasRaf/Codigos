#include <stdio.h>
#include <string.h>


int MyStrcmp(char *name1, char *name2){
    int i, len = strlen(name1);

    if (strlen(name1) != strlen(name2)){
        return 1;
    }

    for (i = 0; i < len; i++){
        if (name1[i] != name2[i]){
            return 1;
        }
    }
    return 0;
}

int main(){
    char nome1[20];  
    char nome2[20];
    
    scanf("%s", nome1);
    scanf("%s", nome2);

    if (!MyStrcmp(nome1,nome2)){
        puts("São Iguais!");
    } else {
        puts("São Diferentes");
    }

    return 0;
}