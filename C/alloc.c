#include <stdio.h>
#include <stdlib.h>

void consoleClear(){
    #ifdef _WIN32 || _WIN64
        system("cls");
    #else
        system("clear");
    #endif  
}

int main(){
    consoleClear();



}