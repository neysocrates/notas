import pandas as pd

from utils.simulacion_notas import generar_nota
from utils.simulacion_programas import generar_programa 

from notebook.limpieza import limpiar_programas
from notebook.limpieza import limpiar_notas

notas = generar_nota(60)
notas_ordenadas=pd.DataFrame(notas)
#print(notas_ordenadas)

simulaciones_limpias_notas = limpiar_notas(notas_ordenadas)
print (simulaciones_limpias_notas)

programas = generar_programa(50)
programas_ordenados = pd.DataFrame(programas)
# print(programas_ordenados)

simulaciones_limpias_programas = limpiar_programas(programas_ordenados)
print (simulaciones_limpias_programas)

