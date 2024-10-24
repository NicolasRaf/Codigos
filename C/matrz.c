#include <stdio.h>
#include <stdlib.h>

void consoleClear(){
    #ifdef _WIN32 || _WIN64
        system("cls");
    #else
        system("clear");
    #endif  
}

int main(void){
    consoleClear();

	int size;
	scanf("%d", &size);

	if(size>200){
		puts("Matrix too big.");
	}
    else{

		int **matrix = (int**)malloc(sizeof(int *) * size);
		int i, j;
		for (i=0; i < size ; i++)
		{
			matrix[i] = (int*)malloc(sizeof(int) * size);
		}

		for (i = 0; i<size; i++)
		{
			for (j = 0; j<size; j++)
			{
				matrix[i][j] = (i + 1)*(j + 1);
			}
		}
		printf("%4c", ' ');
		for (j = 0; j<size; j++)
		{
			printf("%4d", j+1);
		}
		printf("\n");
		for (i = 0; i<size; i++)
		{
			printf("%4d", i+1);
			for (j = 0; j<size; j++)
			{
				printf("%4d", matrix[i][j]);
			}
			printf("\n");
		}
		for (i = 0; i < size; i++)
		{
			free(matrix[i]);
		}
		free(matrix);

	}
	return 0;
}