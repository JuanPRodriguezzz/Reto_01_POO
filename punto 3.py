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