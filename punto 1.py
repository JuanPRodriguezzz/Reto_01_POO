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