#include<stdio.h>
#include <stdlib.h>
#include <time.h>

void quicksort(int arr[] , int a, int b){
	if (a < b) {
        int i = a, j = b;
        int x = arr[(i + j) / 2];
            do {
                while (arr[i] < x) 
                	i++;
                while (x < arr[j])   
                	j--;

                if ( i <= j) {
                    int tmp = arr[i];
                    arr[i] = arr[j];
                    arr[j] = tmp;
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
/**
Funcions que genra un numero aleatorio para el pivote
*/
int generaRandom(int inicio, int final){
	int numero, i;
	int limite_superior = final+1;
	int limite_inferior = inicio;
	int intervalo = limite_superior - limite_inferior;
	srand(time(NULL));
	for(i = 1; i<100; i++){
		numero = 1 + rand() % (intervalo);

	}
	return numero;
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