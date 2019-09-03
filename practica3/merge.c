#include<stdio.h>

/**
*Metodo que ordena dos arreglos ordenados
*/
void merge(int s[], int sub[][2]){
  int arr[8]; //arreglo donde se almacenara el numero ordenado
  int i = sub[0][0]; //inicio sub arreglo 1
  int j = sub[1][0]; //inicio sub arreglo 2
  int limite_superior1 = sub[0][1]; //tamaño sub arreglo 1
  int limite_superior2 = sub[1][1]; //tamaño sub arreglo 2
  int l = 0; //indice del arreglo ordenado
  while(i<=sub[0][1] && j<=limite_superior2){
    if(s[i]<=s[j] && i<=limite_superior1){
      arr[l]=s[i];
      l++;
      i++;}
    else if ( s[j]<=s[i] && j<=limite_superior2 ) {
      arr[l]=s[j];
      l++;
      j++;}
  }
  if(i<=limite_superior1){
    for(int r = i; r<=limite_superior1;r++){
      arr[l]=s[i];
    }
  }
  else if(j<=limite_superior2){
    for(int r = j; r<=limite_superior2;r++){
      arr[l]=s[j];
    }
  }
  for(int z = 0; z< limite_superior2; z++){
    s[z]= arr[z];}
}


int main(){
  //int longitud = sizeof(tuArreglo) / sizeof(tuArreglo[0]);
  int matriz[]= {0,2,4,6,1,3,5,7};
  int sub [2][2];
  sub[0][0]=0;
  sub[0][1]=3;
  sub[1][0]=4;
  sub[1][1]=7;
  merge(matriz, sub);
  for(int i = 0; i<8; i++){
    printf("%i\n",matriz[i]);
  }
  return 0;
}
