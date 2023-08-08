import numpy as np
import matplotlib.pyplot as plt
import sympy as sp


def ajuste_lineal(x, y):
    if len(x) != len(y):
        raise ValueError(
            "El número de puntos en X debe ser igual al número de puntos en Y.")

    x_media = np.mean(x)
    y_media = np.mean(y)

    # numerador = np.sum((x - x_media) * (y - y_media))
    numerador = len(x) * np.sum(x * y) - np.sum(x) * np.sum(y)
    # denominador = np.sum((x - x_media)**2)
    denominador = len(x) * np.sum(x**2) - np.sum(x)**2
    if denominador == 0:
        raise ValueError(
            "El denominador en el cálculo de la pendiente (m) no puede ser cero.")

    m = numerador / denominador
    b = y_media - m * x_media

    print(f"La pendiente es: {m}")
    print(f"El intercepto es: {b}")

    return round(m, 5), round(b, 5)


try:
    n_puntos = int(input("Ingrese el número de puntos: "))
    x_data = []
    y_data = []
    for i in range(n_puntos):
        x_val = float(input(f"Ingrese el valor de x{i + 1}: "))
        y_val = float(input(f"Ingrese el valor de y{i + 1}: "))
        x_data.append(x_val)
        y_data.append(y_val)

    m, b = ajuste_lineal(np.array(x_data), np.array(y_data))

    x, y = sp.symbols('x y')
    ecuacion = sp.Eq(y, m * x + b)
    print(f"\nEcuación de la línea recta: {ecuacion}")

    plt.scatter(x_data, y_data, color="green", label="Datos")
    x_values = np.linspace(min(x_data), max(x_data), 100)
    y_values = m * x_values + b
    plt.plot(x_values, y_values, color="orange",
             label="Ajuste lineal para: " + str(ecuacion))
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.legend()
    plt.grid(True)
    plt.title("Ajuste Lineal de Curvas")
    plt.show()

except ValueError as ve:
    print(f"Error: {ve}")
except Exception as e:
    print(f"Error inesperado: {e}")
