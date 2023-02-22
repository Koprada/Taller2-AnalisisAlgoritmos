import random
import time as tiempo
import pandas as pd
import statsmodels.api as sm
import statsmodels.formula.api as smf
import numpy as np


#Creacion de archivo que incrementa de 100 en 100 datos hasta llegar a 30000
def escritura_archivo(pos):
    max_num = 12

    with open("input.in", "a") as f:
        numbers = []
        for i in range(pos*100):
            num = random.randint(0, max_num)
            numbers.append(num)
        f.write(" ".join(str(x) for x in numbers))
        f.write("\n")

for i in range(300):
  escritura_archivo(i + 1)


#Algoritmo 
def max_idiferencia_dividir_y_vencer(s, b, e):
    if  b - e < 2:
        return 0
    q= (b + e) // 2

    suma_izquierda = sum(s[b:q])
    suma_derecha = sum(s[q:e])

    diferencia1 = suma_izquierda - suma_derecha
    diferencia2 = max_idiferencia_dividir_y_vencer(s, b, q)
    diferencia3 = max_idiferencia_dividir_y_vencer(s, q, e)
    max_diferencia = max(abs(diferencia1), abs(diferencia2), abs(diferencia3))

    return max_diferencia



#Captura de tiempos
def measure_time(s):
  st = tiempo.process_time()
  max_idiferencia_dividir_y_vencer(s,0,len(s))
  et = tiempo.process_time()
  return (et - st)
  


# Abrir el archivo .in en modo lectura
with open('input.in', 'r') as f:
    # Leer cada línea del archivo
    lineas = f.readlines()

# Convertir cada línea en una lista de números
numeros = []
for linea in lineas:
    i = 0
    # Eliminar los espacios en blanco al inicio y al final de la línea
    linea = linea.strip()
    # Separar los valores por espacios en blanco y convertirlos a números
    s = [float(x) for x in linea.split()]
    # Agregar los valores a la lista de números
    time = measure_time(s)
    print(len(s),f"{time: .15f}")
    with open("output.res","a") as file:
      file.write(f"{len(s)} {time:.15f}\n")




#Creacion de grafica
df_results = pd.read_csv('/content/output.res', sep=' ', header=None, names=['n','Maxima'])
df_results.head()

df_results.plot(y=['Maxima'],x='n')

mod = smf.ols(formula='Maxima ~ n:np.log2(n)', data=df_results)
res = mod.fit()
print(res.summary())