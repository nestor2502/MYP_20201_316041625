#include<stdio.h>
#include <stdlib.h>
#include <time.h>


void swap(int *a , int *b){
	int temp = *a;
	*a = *b;
	*b = temp;
}
/**
*Metodo
*
*/
void quicksort(int arr[] , int a, int b){
	if (a < b) {
        int i = a, j = b;
        int pivote = arr[(i + j) / 2];
            do {
                while (arr[i] < pivote)
                	i++;
                while (pivote < arr[j])
                	j--;

                if ( i <= j) {
                	swap(&arr[i], &arr[j]);
                    i++;
                    j--;
                }

            } while (i <= j);

            quicksort(arr, a, j);
            quicksort(arr, i, b);
	}}

void quicksort1(int a[] , int longitud){
	quicksort(a, 0, longitud-1);
	}

int main(){
	int numeros = 0;
	//numero de elementos a ingresar
	scanf("%i", &numeros);
	int i ;
	int j =0;
	int elementos[numeros];
	for(i=0; i<numeros; i++){
		scanf("%i",&j);
		elementos[i]= j;

	}

	quicksort1(elementos, numeros);
	for(i=0; i<numeros; i++){

		printf("%i\n", elementos[i]);

	}

}
