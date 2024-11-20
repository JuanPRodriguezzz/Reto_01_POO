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