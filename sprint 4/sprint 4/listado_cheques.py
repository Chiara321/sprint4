import csv
from datetime import datetime
import sys

parametro = sys.argv[1:]
n_archivo_csv = parametro[0]
dni_filtro = parametro[1]
salida = parametro[2]
tipo_cheque_filtro = parametro[3]
estado_filtro = None
r_fecha = None

if len(parametro) == 5:
    opcional = parametro[4]
    tipos_estados = ["PENDIENTE", "APROBADO", "RECHAZADO"]
    if opcional in tipos_estados: 
        estado_filtro = opcional
    else:
        r_fecha = opcional.split(':')
elif len(parametro) == 6:
    estado_filtro = parametro [4]
    r_fecha = parametro[5].split(':')
    
if r_fecha:
    r_fecha_inicio = datetime.timestamp(datetime.strptime(r_fecha[0], '%d-%m-%Y'))
    r_fecha_fin = datetime.timestamp(datetime.strptime(r_fecha[1], '%d-%m-%Y'))
    
res = []
    
with open(n_archivo_csv, 'r') as archivo_csv:
    csv_reader = csv.reader(archivo_csv, delimiter = ',')
    for fila in csv_reader:
        dni = fila [8]
        cheque = fila[9]
        estado_cheque = fila[10]
        fecha = float(fila[6])

        if dni != dni_filtro or cheque != tipo_cheque_filtro:
           continue
        if estado_filtro and estado_cheque != estado_filtro:
            continue
        if r_fecha and (fecha < r_fecha_inicio or fecha > r_fecha_fin):
            continue        
        res.append(fila)
        
for dni in res:
    if n_archivo_csv == tipo_cheque_filtro:
        res.append(f"Error: cheques repetidos")
    else:
        continue

if salida == 'pantalla':
    for fila in res:
        print(','.join(fila))
elif salida == "csv":
    filtro_datos = [[fila[3], fila[5], fila[6], fila[7]] for fila in res]
    dt = datetime.now()
    dt = dt.strftime("%d-%m-%Y")
    with open (f'{fila[8]}-{dt}.csv', 'w', newline = '') as archivo_salida:
        writer = csv.writer(archivo_salida)
        writer.writerows(filtro_datos)
