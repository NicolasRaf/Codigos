#include <stdio.h>
#include <stdlib.h>

void consoleClear(){
	#if defined(_WIN32) || defined(_WIN64)
		system("cls");
    #else
        system("clear");
	#endif
    
}

void bubbleSort(float *numbers){
	int swapped, i;
	float aux;

	do{
		swapped = 0;

		for (i = 0; i < 9; i++){
			if (numbers[i] < numbers[i + 1]){
				swapped = 1;
				aux = numbers[i];
				numbers[i] = numbers[i + 1];
				numbers[i + 1] = aux;
			}
		}	
		
	} while (swapped);

}

int main(void){
	consoleClear();

	float numbers[10] = {5.6, 4.3, 6.2, 6.4, 7.3, 2.3, 8.3, 9.2, 0.1, 1.9};
	bubbleSort(numbers);
	
	for (int i = 0; i < 10; i++){
		printf("%f\n",numbers[i]);
	}

	return 0;
}	