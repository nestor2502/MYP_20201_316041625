#include<stdio.h>

int esPrimo(int numero){
     if(numero == 1)
     	return 0;
	 int i = 2;
	 for(i; i< numero; i++){
	     if(numero%i==0)
	    	return 0;
	     }
	     return 1;
}

int main(){
	printf("Ingresa un numero\n");
	int i = 2 ;
	int n;
	int *a = &n;
	scanf("%i", a);
	for(i; i<n; i++){
		 if(esPrimo(i))
		 	printf("%i\n", i );
	}
}
