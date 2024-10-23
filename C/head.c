#include <stdio.h>
#include <stdlib.h>


struct ELEMENT {
 int value;
 struct ELEMENT  *next;
};

int main(){
    system("clear");

    struct ELEMENT *head, *ptr;

    /* the one-way linked list is created here
    we don't know yet how it was done
    we only know that the head points to element #1 */
        ptr = head;
    /* ptr points to the first element now; we will move it
    through all elements until we reach the end */
        while(ptr != NULL) { 
            /* print the value stored in the element */
            printf("value = %d\n", ptr -> value);

            /* move ptr to the next element */
            ptr = ptr -> next;
        }

    printf("done!");
}