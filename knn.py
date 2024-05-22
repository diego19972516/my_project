def classify(Clasificar_x, Clasificar_y):
    x = [150, 170, 50, 20, 150, 30]
    y = [60, 80, 3, 7, 70, 10]
    z = ["A", "A", "B", "B", "A", "B"]

    diferencias_x = [Clasificar_x - num for num in x]
    diferencias_y = [Clasificar_y - num for num in y]

    potencia_diferencias_x = [dif ** 2 for dif in diferencias_x]
    potencia_diferencias_y = [dif ** 2 for dif in diferencias_y]

    suma_potencias = [px + py for px, py in zip(potencia_diferencias_x, potencia_diferencias_y)]

    raiz_suma_potencias = [suma ** 0.5 for suma in suma_potencias]

    distancias_con_etiquetas = list(zip(raiz_suma_potencias, z))

    distancias_con_etiquetas.sort(key=lambda x: x[0])

    tres_mas_cortas = distancias_con_etiquetas[:3]

    conteo_A = sum(1 for _, etiqueta in tres_mas_cortas if etiqueta == 'A')
    conteo_B = sum(1 for _, etiqueta in tres_mas_cortas if etiqueta == 'B')

    resultado = 'A' if conteo_A > conteo_B else 'B'

    return {
        'Clasificar_x': Clasificar_x,
        'Clasificar_y': Clasificar_y,
        'resultado': resultado,
        'tres_mas_cortas': tres_mas_cortas
    }
