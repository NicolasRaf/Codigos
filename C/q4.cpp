#include <stdio.h> 
#include <string.h> 
#include <iostream> 

using namespace std; 
 
typedef struct { 
    char valor[10]; 
} Str; 
 
 
int main(){ 
    char valor[3] = {"um"}; 
  
    Str v = {"123"}; 

  
    int i = 0; 
    while (i <= strlen(v.valor)) { 
        cout << i << "--" << v.valor[i] << endl; 
        i++; 
    } 
  
    cout<<"---------\n"; 
  
    int j = 0; 
    while (valor[j]){ 
        cout << "j = " <<j<<" - "<<valor[j]<<endl;   
        j++; 
    } 
  
    cout << "\nValor de J: " << j << ""; 
    cout << "\nValor de I: " << i << "\n"; 
} 