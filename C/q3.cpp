#include <iostream>
#include <string.h>

using namespace std;

int main(){
    string nome1;
    string nome2;

    cout << "Primeiro Nome: ";
    cin >> nome1;
    cout << "Segundo Nome: ";
    cin >> nome2;

    if (nome1 == nome2){
        cout << "São Iguais!" << endl;
    } else {
        cout << "São Diferentes!" << endl;
    }

    return 0;
}