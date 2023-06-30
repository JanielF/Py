#Esto es un comentario : Hola mundo
#Nuestro hola mundo en Python
print("Hola Python")
print('Hola Python')



"""
Esto es un 
comentario 
en varias lineas
"""

'''
Este tambien es un 
comentario 
en varias lineas
'''

#Consultar el tipo de dato
print(type("Soy un dato str")) #Tipo 'str(string)'
print(type(5)) #Tipo 'int'
print(type(1.5)) #Tipo 'float'
print(type(1 + 1j)) #Tipo 'complex'
print(type(True)) #Tipo 'bool'

print(type(print("Mi cadena de texto"))) # Tipo 'NoneType'

name1 = str(input("Por favor ingresa tu nombre:"))
lastname = str(input("Por favor ingresa tu apellido:"))
age1 = int(input("Por favor ingresa tu edad:"))

print('Su nombre completo es {} {} y su edad es {}'.format(name1,lastname,age1))