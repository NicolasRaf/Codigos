#include <stdio.h> 
#include <iostream> 

using namespace std; 
 
typedef struct no { 
    int item; 
    struct no *prox; 
}No; 
 
int main(){ 
    int qtd;
    cout << "Insira o tamanho desejado de itens: ";
    cin >> qtd;
    No v[qtd]; 
    int i;

    for(i = 0; i < qtd; i++){
        if(i < qtd-1){
        cout << "Insira o " << i+1 << "º número: ";
        cin >> v[i].item;
        v[i].prox = v+(i+1);
        }
        else{
            cout << "Insira o " << i+1 << "º número: ";
            cin >> v[i].item;
            v[i].prox = NULL;
        }
    }

    for (No *p = v+0; p; p = p -> prox) 
        cout << "Valor de P: " << p -> item << "\n";    
  
    return 0;
}