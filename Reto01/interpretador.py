from collections import deque

#funcion que separa cada elemento de la cadena
def separaCadena(cadena):
	lista = []
	j = 0
	for i in cadena:
			lista.append(cadena[j])
			j+=1	
	#se crea una cola
	cola = deque(lista)

	return lista

#funcion que convierte la cola en una lista con numeros operables
def parser(cola):
	elementos = []
	j = 0
	n=0
	lista_temporal = []
	cola_temp = deque(lista_temporal)
	#se obtiene cada elemento
	for i in cola:
		if cola[j] != '*' and cola[j] != '+':
			if j+1 == len(cola):		
				cola_temp.append(cola[j])
				n+=1
				numero = ""
				m = 0
				while m <n :
					numero += str(cola_temp[m])
					m+=1
				elementos.append(int(numero))
			else:
				cola_temp.append(cola[j])
			n+=1
			j+=1
		elif cola[j] == '*' or cola[j] == '+':
			longitud = n	
			l = 0
			numero = ""
			while l <n :
				numero += str(cola_temp[l])
				l+=1
			if numero !="":
				elementos.append(int(numero))
			elementos.append(cola[j])
			cola_temp = deque(lista_temporal)
			n=0
			j+=1
	return elementos
				
#funcion que realiza el producto segun la jerarquia de operaciones
def realizaProducto(lista):
	pila = []
	j =0
	for l in lista:
		if j < len(lista):
			pila.append(lista[j])
			if lista[j] == "*":
				pila.pop()
				a = pila.pop()
				b = lista[j+1]
				c =  a*b
				pila.append(c)
				j+=1
		j+=1
	return pila

#funcion que suma todos los elementos de la lista
def realizasuma(lista):
	pila = []
	j =0
	for l in lista:
		if j < len(lista):
			pila.append(lista[j])
			if lista[j] == "+":
				pila.pop()
				a = pila.pop()
				b = lista[j+1]
				c =  a+b
				pila.append(c)
				j+=1
		j+=1
	return pila[0]

#funvion que realiza todo el proceso analizando diferentes casos
def general():
	cadena = str(raw_input())
	cadena_procesada = separaCadena(cadena)
	numeros = parser(cadena_procesada)
	se_encuentra_suma = "+" in cadena_procesada
	se_encuentra_producto = "*" in cadena_procesada

	if se_encuentra_suma and se_encuentra_producto==False:
		total = realizasuma(numeros)
		print(total)

	elif se_encuentra_producto and se_encuentra_suma==False:
		total = realizaProducto(numeros)
		print(total[0])

	else:
		sumandos = realizaProducto(numeros)
		total = realizasuma(sumandos)
		print(total)
	
general()


