#APLICACION PROYECTO
def leer_numero_natural():
    print("*** Calcular Divisores de un Numero Natural ***")
    while True:
        try:
            numero = int(input("Ingrese un número natural: "))

            if numero < 1:
                raise ValueError("El número debe ser un entero positivo.")
            return numero
        except ValueError as e:

            print(f"Entrada no válida: {e}. Intente nuevamente.")

def calcular_divisores(numero):
    divisores = [i for i in range(1, numero + 1) if numero % i == 0]
    return divisores

def main():

    numero = leer_numero_natural()

    divisores = calcular_divisores(numero)

    print(f"Los divisores de {numero} son: {divisores}")

if __name__ == "__main__":
    main()
