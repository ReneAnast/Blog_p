from urllib.request import urlopen

# Abrir URL.
r = urlopen("https://production-api2.42-q.com/mes-api/p2447dc6/units/P1104207-01-N:SE4A24276001841/summary")
# Leer el contenido y e imprimir su tamaño.
print(r.read())
# Cerrar para liberar recursos.
r.close()