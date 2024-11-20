# Reto_01_Poo
# Juan Pablo Rodríguez Cruz
1. Crear una función que realice operaciones básicas (suma, resta, multiplicación, división) entre dos números, según la elección del usuario, la forma de entrada de la función será los dos operandos y el caracter usado para la operación. entrada: (1,2,"+"), salida (3).

```python
import os # Para limpiar la pantalla

class Calculadora:

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

``` python


2. Realice una función que permita validar si una palabra es un palíndromo. Condición: No se vale hacer slicing para invertir la palabra y verificar que sea igual a la original.

``` python
import os  # Para limpiar la pantalla

class PalindromoChecker:
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
        PalindromoChecker.limpiar_pantalla()

    @staticmethod
    def verif_palindromo(palabra):
        palabra = palabra.upper()
        longitud = len(palabra)
        
        for i in range(longitud // 2):
            if palabra[i] != palabra[longitud - i - 1]:
                return False
        return True

    def ejecutar(self):
        while True:
            self.limpiar_pantalla()
            try:
                palabra = input("\nIngrese una palabra para verificar si es un palíndromo: ").strip()
                if not palabra:
                    print("\nError: No se ingresó ninguna palabra. Intente nuevamente.\n")
                    self.continuar()
                    continue

                if self.verif_palindromo(palabra):
                    print(f"\n\n{palabra} es un palíndromo.\n")
                else:
                    print(f"\n\n{palabra} no es un palíndromo.\n")
            except Exception as e:
                print(f"\nError: {str(e)}\n")
            self.continuar()

if __name__ == "__main__":
    checker = PalindromoChecker()
    checker.ejecutar()
``` python

3. Escribir una función que reciba una lista de números y devuelva solo aquellos que son primos. La función debe recibir una lista de enteros y retornar solo aquellos que sean primos.

``` python
import os  # Para limpiar la pantalla

class Primos:
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

    @staticmethod
    def es_primo(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    @staticmethod
    def obtener_primos(lista):
        primos = []
        for item in lista:
            try:
                numero = int(item)
                if Primos.es_primo(numero):
                    primos.append(numero)
            except ValueError:
                print(f"\"{item}\" no es un número entero válido.")
        return primos

    def ejecutar(self):
        while True:
            self.limpiar_pantalla()
            try:
                entrada = input("Ingrese una lista de números separados por comas y sin espacios: ")
                numeros = entrada.split(',')
                primos = self.obtener_primos(numeros)
                print("\nNúmeros primos en la lista:", primos)
            except Exception as e:
                print(f"\nError: {str(e)}")
            self.continuar()

if __name__ == "__main__":
    primos_checker = Primos()
    primos_checker.ejecutar()

``` python

4. Escribir una función que reciba una lista de números enteros y retorne la mayor suma entre dos elementos consecutivos.


``` python
import os  # Para limpiar la pantalla

class MayorSumaConsecutiva:
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

    @staticmethod
    def calcular_mayor_suma(lista):
        if len(lista) < 2:
            return None  # No se puede calcular si hay menos de dos elementos

        mayor_suma = lista[0] + lista[1]
        for i in range(len(lista) - 1):
            suma_actual = lista[i] + lista[i + 1]
            if suma_actual > mayor_suma:
                mayor_suma = suma_actual

        return mayor_suma

    def ejecutar(self):
        while True:
            self.limpiar_pantalla()
            try:
                entrada = input("\nIngrese una lista de números enteros separados por espacios: ").strip()
                lista = list(map(int, entrada.split()))  # Convertir la entrada en una lista de enteros

                if not lista:  # Si la lista está vacía
                    print("\nError: Debe ingresar números. Intente nuevamente.\n")
                else:
                    resultado = self.calcular_mayor_suma(lista)
                    if resultado is None:
                        print("\nError: La lista debe contener al menos dos números.\n")
                    else:
                        print(f"\nLa mayor suma entre dos números consecutivos es: {resultado}\n")
            except ValueError:
                print("\nError: Asegúrate de ingresar solo números enteros separados por espacios.\n")
            except Exception as e:
                print(f"\nOcurrió un error inesperado: {str(e)}\n")

            self.continuar()

if __name__ == "__main__":
    programa = MayorSumaConsecutiva()
    programa.ejecutar()

``` python

5.Escribir una función que reciba una lista de string y retorne unicamente aquellos elementos que tengan los mismos caracteres.


``` python
import os  # Para limpiar la pantalla

class MismosCaracteres:
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

    @staticmethod
    def filtrar_mismos_caracteres(lista):
        grupos = {}  # Diccionario para agrupar palabras
        lista = list(set(lista))  # Elimina duplicados de la lista original
        
        for palabra in lista:
            clave = ''.join(sorted(palabra.lower()))  # Ordena los caracteres y convierte a minúsculas
            if clave not in grupos:
                grupos[clave] = []
            grupos[clave].append(palabra)

        # Filtra solo los grupos con más de una palabra
        resultado = [item for sublista in grupos.values() if len(sublista) > 1 for item in sublista]
        return resultado

    def ejecutar(self):
        while True:
            self.limpiar_pantalla()
            try:
                entrada = input("\nIngrese una lista de palabras separadas por espacios: ").strip()
                lista = entrada.split()  # Divide la entrada en una lista de palabras

                if not lista:  # Si la lista está vacía
                    print("\nIntente nuevamente.\n")
                else:
                    resultado = self.filtrar_mismos_caracteres(lista)
                    if resultado:
                        print(f"\nLas palabras con los mismos caracteres son: {resultado}\n")
                    else:
                        print("\nNo se encontraron palabras con los mismos caracteres.\n")
            except Exception as e:
                print(f"\nError: {str(e)}\n")

            self.continuar()

if __name__ == "__main__":
    MismosCaracteres().ejecutar()
``` python
