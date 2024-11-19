# Reto_01_Poo
# Juan Pablo Rodríguez Cruz
1. Crear una función que realice operaciones básicas (suma, resta, multiplicación, división) entre dos números, según la elección del usuario, la forma de entrada de la función será los dos operandos y el caracter usado para la operación. entrada: (1,2,"+"), salida (3).

```
import os

class Calculadora:
    """Clase para realizar operaciones básicas entre dos números."""

    def __init__(self):
        pass

    @staticmethod
    def limpiar_pantalla():
        """Limpia la consola."""
        os.system("cls" if os.name == "nt" else "clear")

    @staticmethod
    def continuar():
        """Pausa la ejecución hasta que el usuario presione Enter."""
        input("\nPresiona Enter para continuar...")
        Calculadora.limpiar_pantalla()

    def operaciones_basicas(self, num1, num2, operador):
        try:
            if operador == '+':
                resultado = num1 + num2
            elif operador == '-':
                resultado = num1 - num2
            elif operador == '*':
                resultado = num1 * num2
            elif operador == '/':
                if num2 != 0:
                    resultado = num1 / num2
                else:
                    print("\nError: No se puede dividir por cero.\n")
                    return
            else:
                print("\nError: Operador no válido. Intenta nuevamente.")
                return
            print(f"\nResultado: {num1} {operador} {num2} = {resultado}\n")
        except Exception as e:
            print(f"\nError: {str(e)}")

    def ejecutar(self):
        while True:
            self.limpiar_pantalla()
            try:
                entrada = input("Ingrese el 1er número, el 2do y el operador separados por comas (num1,num2,operador): ")
                num1, num2, operador = entrada.split(',')
                num1 = float(num1)
                num2 = float(num2)
                operador = operador.strip()
                self.operaciones_basicas(num1, num2, operador)
            except ValueError:
                print("\nError: Entrada inválida. Asegúrate de usar el formato correcto (num1,num2,operador).\n")
            self.continuar()

# Instanciar y ejecutar la calculadora
if __name__ == "__main__":
    calculadora = Calculadora()
    calculadora.ejecutar()

```


2. Realice una función que permita validar si una palabra es un palíndromo. Condición: No se vale hacer slicing para invertir la palabra y verificar que sea igual a la original.

```
import os  # Para limpiar la pantalla

class PalindromoChecker:
    def __init__(self):
        """Inicializa la clase PalindromoChecker."""
        pass

    @staticmethod
    def limpiar_pantalla():
        """Limpia la consola."""
        os.system("cls" if os.name == "nt" else "clear")

    @staticmethod
    def continuar():
        """Pausa la ejecución hasta que el usuario presione Enter."""
        input("\nPresiona Enter para continuar...")
        PalindromoChecker.limpiar_pantalla()

    @staticmethod
    def es_palindromo(palabra):
        Parámetros:
        - palabra (str): La palabra a verificar.

        Retorna:
        - True si es un palíndromo, False en caso contrario.
        """
        palabra = palabra.upper()
        longitud = len(palabra)
        
        for i in range(longitud // 2):
            if palabra[i] != palabra[longitud - i - 1]:
                return False
        return True

    def ejecutar(self):
        """Método principal para ejecutar el programa."""
        while True:
            self.limpiar_pantalla()
            try:
                palabra = input("\nIngrese una palabra para verificar si es un palíndromo: ").strip()
                if not palabra:
                    print("\nError: No ingresaste ninguna palabra. Intenta nuevamente.\n")
                    self.continuar()
                    continue

                if self.es_palindromo(palabra):
                    print(f"\n\n{palabra} es un palíndromo.\n")
                else:
                    print(f"\n\n{palabra} no es un palíndromo.\n")
            except Exception as e:
                print(f"\nOcurrió un error inesperado: {str(e)}\n")
            self.continuar()

if __name__ == "__main__":
    checker = PalindromoChecker()
    checker.ejecutar()
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
