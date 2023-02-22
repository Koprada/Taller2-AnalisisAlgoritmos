import random
import time as tiempo
import pandas as pd
import statsmodels.api as sm
import statsmodels.formula.api as smf
import numpy as np


#Creacion de archivo que incrementa de 100 en 100 datos hasta llegar a 30000
def writeData(pos):
    max_n = 100000
    max_num = 12
    ns = set()

    with open("input.in", "a") as f:
        numbers = []
        for i in range(pos*100):
            num = random.randint(0, max_num)
            numbers.append(num)
        f.write(" ".join(str(x) for x in numbers))
        f.write("\n")

for i in range(300):
  writeData(i + 1)

#Algoritmo 
def max_idiferencia_dividir_y_vencer(S, b, e):
    if  b - e < 2:
        return 0
    q= (b + e) // 2

    suma_izquierda = sum(S[b:q])
    suma_derecha = sum(S[q:e])

    diferencia1 = suma_izquierda - suma_derecha
    diferencia2 = max_idiferencia_dividir_y_vencer(S, b, q)
    diferencia3 = max_idiferencia_dividir_y_vencer(S, q, e)
    max_diferencia = max(abs(diferencia1), abs(diferencia2), abs(diferencia3))

    return max_diferencia



#Apertura del archivo.
def MeasureTime(S):
  sT = tiempo.process_time()
  max_idiferencia_dividir_y_vencer(S,0,len(S))
  eT = tiempo.process_time()
  return (eT - sT)
  
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
    S = [float(x) for x in linea.split()]
    # Agregar los valores a la lista de números
    time = MeasureTime(S)
    print(len(S),f"{time: .15f}")
    with open("output.res","a") as file:
      file.write(f"{len(S)} {time:.15f}\n")




#Creacion de grafica
df_results = pd.read_csv('/content/output.res', sep=' ', header=None, names=['n','Maxima'])
df_results.head()

df_results.plot(y=['Maxima'],x='n')

mod = smf.ols(formula='Maxima ~ n:np.log2(n)', data=df_results)
res = mod.fit()
print(res.summary())