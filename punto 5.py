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