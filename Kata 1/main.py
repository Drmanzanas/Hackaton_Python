'''
Una panaderia vende barras de pan a 3.49€ cada una. El pan que no es del dia tiene un descuento del 60%
Escribe un programa que comience leyendo el número de barras vendidas que no son del dia.Despues tu progrma debe mostrar el precio habitual
de una barra de pan, el descuento que se le hace por no se fresca y el coste final
'''

precio = 3.49
descuento = 0.4
precio_con_descuento = precio * descuento

numero_de_barras = input('Introduce el numero de barras vendidas:')

print('Precio habitual ' + str(precio))
print('Descuento ' + str(precio_con_descuento))
print('Coste final: ' + str(int(numero_de_barras) * precio_con_descuento))