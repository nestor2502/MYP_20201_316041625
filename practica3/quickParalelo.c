#include<stdio.h>
#include <stdlib.h>
#include <time.h>
#include <omp.h>
#include "quicksort.c"
#define SIZE 10000000

/**
*Llena un arreglo con numeros aleatorios
*/
void llenaArreglo(int *arreglo, int size)
{
  srand(time(NULL));
  for(int i = 0; i< size; i++){
    int r = rand();
    arreglo[i]= r;
  }
}

/**
*devuelve 1 si esta ordenado 0 si no
*/
int isSorted(int *arreglo, int size)
{
  int last = arreglo[0];
  for(int i = 1; i< size; i++){
    if(last > arreglo[i]) return 0;
  }
  return 1;
}

/**
*Metodo que ordena dos arreglos ordenados
*/
void merge(int s[], int sub[][2])
{
  int tamano = sub[1][1]+1;//longitud del arreglo
  //int arr[tamano]; //arreglo donde se almacenara el numero ordenado
  int *arr = malloc(tamano*sizeof(int));
  int i = sub[0][0]; //inicio sub arreglo 1
  int j = sub[1][0]; //inicio sub arreglo 2
  int limite_superior1 = sub[0][1]; //cota sup del  sub arreglo 1
  int limite_superior2 = sub[1][1]; //cota sup del  sub arreglo 2
  int l = 0; //indice del arreglo ordenado
  while(i<=limite_superior1 && j<=limite_superior2){
    if(s[i]<=s[j] && i<=limite_superior1){//si el elemento del indice i es menor o igual al indice j
      arr[l]=s[i];
      l++;//se aumenta el indice del nuevo arreglo
      i++;}
    else if ( s[j]<=s[i] && j<=limite_superior2 ) {//si el elemento del indice i es menor o igual al indice j
      arr[l]=s[j];
      l++;//se aumenta el indice del nuevo arreglo
      j++;}
  }
  if(i<=limite_superior1){//se meten lo numeros del primer intervalo sobrantes
    for(int r = i; r<=limite_superior1;r++){
      arr[l]=s[i];
      l++;
      i++;
    }
  }
  else if(j<=limite_superior2){//se meten lo numeros del segundo intervalo sobrantes
    for(int r = j; r<=limite_superior2;r++){
      arr[l]=s[j];
      l++;
      j++;
    }
  }
  for(int z = 0; z<=limite_superior2; z++){//se reasignan los valores delarreglo original
    s[z]= arr[z];}
    free(arr);
}

/**
*Metodo que aplica quick paralelo
*/
void quickParallel(int a[] , int longitud)
{
  int mitad = longitud/2;
	int inicio2 =mitad ;
	int final1 =mitad-1 ;
	int final2 = longitud-1 ;
	int sub [2][2];
  sub[0][0]=0;
  sub[0][1]=final1;
  sub[1][0]=inicio2;
  sub[1][1]=final2;
  #pragma omp parallel sections
    {
    #pragma omp section
  	quicksort(a, 0, final1);

    #pragma omp section
  	quicksort(a, inicio2, final2);

    }
  #pragma omp barrierr
    merge(a, sub);
}

int main()
{
  int* arreglo = malloc(SIZE * sizeof(int));
  llenaArreglo(arreglo, SIZE);

  int* arreglo2 = malloc(SIZE * sizeof(int));
  llenaArreglo(arreglo2, SIZE);

  clock_t t;
  t = clock();

  quicksort(arreglo, 0, SIZE-1);

  t = clock() -t;
  double time_taken = ((double)t)/CLOCKS_PER_SEC;

  if(isSorted(arreglo, SIZE))
  printf("Sequential quicksort with %i elements took %f seconds to execute \n",SIZE, time_taken );
  else printf("Secuential quicksort doesn't work");

  clock_t z;
  z = clock();

  quickParallel(arreglo2, SIZE);

  z = clock() -z;
  double time_taken2 = ((double)z)/CLOCKS_PER_SEC;

  if(isSorted(arreglo2, SIZE))
  printf("Parallel quicksort with %i elements took %f seconds to execute \n",SIZE, time_taken2 );
  else printf("Parallel quicksort doesn't work\n");


}
