#include <stdio.h>
#include <stdlib.h>

int main(void) {
	union {
		int a;
		char b;
	} Data;

	scanf("%d", &Data.a);
	printf("\n%c\n", Data.b);
	return 0;
}