# Reto01_Poo
# Juan Pablo Rodríguez Cruz
1. Crear una función que realice operaciones básicas (suma, resta, multiplicación, división) entre dos números, según la elección del usuario, la forma de entrada de la función será los dos operandos y el caracter usado para la operación. entrada: (1,2,"+"), salida (3).

```
from subprocess import call

def limpiar_pantalla(): #Función para limpiar la consola
    call("cls",shell=True)

def continuar(): # Función para limpiar la consola dando Enter
    input("\nEnter para continuar")
    call("cls",shell=True)

def operaciones_basicas(num1,num2,operador):
    while True:     
        if operador == '+':
            Resultado = num1 + num2
        elif operador == '-':
            Resultado = num1 - num2
        elif operador == '*':
            Resultado = num1 * num2
        elif operador == '/':
            if num2 != 0:
                Resultado = num1 / num2
            else:
                print("\nNo se puede dividir por cero.\n")
                break
        else:
            print("\n\nIntente de nuevo\n")
            continuar()
            break
        print(f"\n\n{num1} {operador} {num2} = {Resultado}\n")
        break
      
while True:
    limpiar_pantalla()
    num1,num2,operador = input("\nIngrese el 1er número, el 2do y el operador separados por comas, (num1,num2,op): ").split(',')
    num1=float(num1)
    num2=float(num2)
    operador=str(operador)
    operaciones_basicas(num1,num2,operador)
    continuar()
    continue
```

2. Realice una función que permita validar si una palabra es un palíndromo. Condición: No se vale hacer slicing para invertir la palabra y verificar que sea igual a la original.


```
from subprocess import call

def limpiar_pantalla(): 
    call("cls",shell=True)
def continuar(): # Función para limpiar la pantalla continuando
    input("\nEnter para continuar ")
    call("cls",shell=True)


def verif_palindromo(palabra):
    palabra = palabra.upper()
    
    Length = len(palabra)
    
    for i in range(Length // 2):
        if palabra[i] != palabra[Length - i - 1]:
            return False
    return True

limpiar_pantalla()
while True:
    Ingreso = input("\nIngrese una palabra para verificar si es un palíndromo: ")
    if verif_palindromo(Ingreso):
        print(f"\n\n{Ingreso} es un palíndromo.\n")
        continuar()
        continue
    else:
        print(f"\n\n{Ingreso} no es un palíndromo.\n")
        continuar()
        continue
```

3. Escribir una función que reciba una lista de números y devuelva solo aquellos que son primos. La función debe recibir una lista de enteros y retornar solo aquellos que sean primos.

```
from subprocess import call

def limpiar_pantalla(): #Función para limpiar la consola
    call("cls",shell=True)

def números_primos():
    lista = input("Ingrese una lista de números separados por comas y sin espacios: ").split(',')
    primos = []
    for números in lista:
        try:
            número=int(números)
            if número > 1:
                número_primo = True
            elif número == 1:
                    número_primo = False

            for i in range(2, int(número ** 0.5) + 1):
                if número % i == 0:
                    número_primo = False
                    break   
            if número_primo:
                primos.append(número)
        except:
            print(f"\"{números}\" no es un número entero válido.")
    return primos

if __name__=="__main__":
    limpiar_pantalla()
    print("Números primos en la lista:", números_primos())
```
4. Escribir una función que reciba una lista de números enteros y retorne la mayor suma entre dos elementos consecutivos.


```
from subprocess import call

def limpiar_pantalla(): #Función para limpiar la consola
    call("cls",shell=True)

def mayor_suma_consecutiva():
    # Solicitar al usuario que ingrese la lista de números separados por espacios
    entrada = input("\nIngrese una lista de números enteros separados por espacios: ")
    lista = list(map(int, entrada.split()))  # Convertir la entrada en una lista de enteros
    
   
    if len(lista) < 2:
        return None  # No se puede calcular la suma si hay menos de dos elementos
    
    suma = lista[0] + lista[1]  
    for i in range(len(lista) - 1):
        sumas_consecutivas = lista[i] + lista[i + 1]
        max_suma = max(suma, sumas_consecutivas)
    
    return max_suma

if __name__=="__main__":
    limpiar_pantalla()
    print("\n\nLa mayor suma entre dos números consecutivos es:", mayor_suma_consecutiva(),"\n\n")  
```

5.Escribir una función que reciba una lista de string y retorne unicamente aquellos elementos que tengan los mismos caracteres.


```
from subprocess import call

def limpiar_pantalla(): #Función para limpiar la consola
    call("cls",shell=True)

def mayor_suma_consecutiva():
    # Solicitar al usuario que ingrese la lista de números separados por espacios
    entrada = input("\nIngrese una lista de números enteros separados por espacios: ")
    lista = list(map(int, entrada.split()))  # Convertir la entrada en una lista de enteros
    
   
    if len(lista) < 2:
        return None  # No se puede calcular la suma si hay menos de dos elementos
    
    suma = lista[0] + lista[1]  
    for i in range(len(lista) - 1):
        sumas_consecutivas = lista[i] + lista[i + 1]
        max_suma = max(suma, sumas_consecutivas)
    
    return max_suma

if __name__=="__main__":
    limpiar_pantalla()
    print("\n\nLa mayor suma entre dos números consecutivos es:", mayor_suma_consecutiva(),"\n\n")
```
