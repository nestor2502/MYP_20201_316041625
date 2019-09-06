#include<stdio.h>
/**
*Metodo que intercambia dos valores en el arreglo
*/
void swap(int *a , int *b){
	int temp = *a;
	*a = *b;
	*b = temp;
}
/**
*Metodo quicksort
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
