import sympy as sp

def calculadora():
    while True:
        # Menú de opciones
        print("\nCalculadora Python")
        print("1. Operaciones básicas")
        print("2. Calcular derivada")
        print("3. Salir")
        
        opcion = input("Seleccione una opción (1/2/3): ")

        if opcion == '1':
            expresion = input("Ingrese una expresión matemática: ")
            try:
                resultado = eval(expresion)
                print("Resultado:", resultado)
            except Exception as e:
                print("Error:", e)

        elif opcion == '2':
            expresion = input("Ingrese la expresión para derivar: ")
            variable = input("Respecto a qué variable desea derivar: ")
            try:
                x = sp.symbols(variable)
                expr = sp.sympify(expresion)
                derivada = sp.diff(expr, x)
                print("Derivada:", derivada)
            except Exception as e:
                print("Error:", e)

        elif opcion == '3':
            print("Saliendo de la calculadora. ¡Hasta luego!")
            break

        else:
            print("Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    calculadora()
