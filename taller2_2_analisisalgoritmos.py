#algoritmo modificado para dos datos de retorno
def max_idiferencia_dividir_y_vencer(S, b, e):
    if e - b < 2:
        return 0, None
    else:
        q = (b + e) // 2

        max_dif_izq, izq_max_pos = max_idiferencia_dividir_y_vencer(S, b, q-1)
        max_dif_der, der_max_pos = max_idiferencia_dividir_y_vencer(S, q+1,e)

        suma_izq = sum (S [ b:q])
        suma_der= sum(S [q+1:e])
        max_diferencia= max(max_dif_izq, max_dif_der, suma_izq - suma_der)
        if max_diferencia == max_dif_izq:
            return max_diferencia, izq_max_pos
        elif max_diferencia == max_dif_der:
            return max_diferencia, der_max_pos
        else: 
            return max_diferencia, q

# Abrir el archivo .in en modo lectura
with open('test_cases.in', 'r') as f:
    # Leer cada línea del archivo
    lineas = f.readlines()

# Convertir cada línea en una lista de números
numeros = []
for linea in lineas:
    # Eliminar los espacios en blanco al inicio y al final de la línea
    linea = linea.strip()
    # Separar los valores por espacios en blanco y convertirlos a números
    S = [float(x) for x in linea.split()]
    # Agregar los valores a la lista de números
    max_diferencia, pos= max_idiferencia_dividir_y_vencer(S, 0, len(S))
    print(pos,max_diferencia)
    with open("output.in","a") as file:
      file.write(f"{pos} {max_diferencia}\n")