"""
Encontrar el Mayor y Menor en un arreglo por medio de recursividad.
Considere lo siguiente:
    1) arreglo[1:] -> recorre todo el arreglo desde el índice 1.
    2) todo arreglo inicia desde 0.
"""

def Buscar(arreglo, mayor, menor):
    if(len(arreglo) == 0):
        print(f"Mayor: {mayor} - Menor: {menor}")
    
    else:
        if(arreglo[0] > mayor):
            mayor = arreglo[0]
        elif(arreglo[0] < menor):
            menor = arreglo[0]
        
        Buscar(arreglo[1:], mayor, menor)


arreglo = [4, 7, 2, 3, 1, 5, 6]
mayor = -999999
menor = 999999

Buscar(arreglo, mayor, menor)