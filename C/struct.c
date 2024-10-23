#include <stdio.h>
#include <stdlib.h>

struct SCHOOLS {
    char name[100];
    float average;
    char UF[3];
};

int main() {
    int max;

    printf("Digite o número de escolas: ");
    scanf("%d", &max);

    // Alocação dinâmica
    struct SCHOOLS *school = malloc(max * sizeof(struct SCHOOLS));
    printf("Sizeof: %zu\n", sizeof(school));

    if (school == NULL) {
        printf("Erro na alocação de memória.\n");
        return 1; // Sai do programa com erro
    }

    // Aqui você pode coletar e trabalhar com os dados das escolas

    // Liberando a memória
    free(school);
    return 0;
}
