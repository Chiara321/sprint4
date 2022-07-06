import csv
from http.client import RESET_CONTENT
import sys

parametro = sys.argv[1:]
n_archivo_csv = parametro[0]
dni_filtro = parametro[1]
salida = parametro[2]
tipo_cheque = parametro[3]

with open(n_archivo_csv, 'r') as archivo_csv:
    csv_reader = csv.reader(archivo_csv, delimiter = ',')
    for fila in csv_reader:
        dni = fila [8]
        cheque = fila[9]

        if dni == dni_filtro and cheque == tipo_cheque:
           res.append(fila)

if salida == 'pantalla':
    for fila in res:
        print(fila)

