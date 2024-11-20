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