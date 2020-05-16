'''
Escribir un programa que almacene la cadena de caracteresa contraseña en una variable,
pregunte al usuario por la contraseña e imprima por pantalla si la
contraseña introducida por el usuario coincide con la guardada
en la variable sin tener en cuenta mayusculas y minusculas
'''

password = 'contraseña'

password_del_usuario = input('introduzca la contraseña: ')
password_del_usuario = password_del_usuario.lower()

if password == password_del_usuario:
    print('El password es correcto')
else:
    print('El password no coincide')