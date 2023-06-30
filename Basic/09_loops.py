### Loops ###

# While

my_condition = 0

while my_condition < 10:
    print(my_condition)
    my_condition += 2
else: #es opcional
    print("Mi condicion es mayor o igual que 10")

print("La ejecucion continua")

while my_condition < 20:
    my_condition += 1
    if my_condition == 15:
        print("Mi condicion es 15")
        break
    print(my_condition)

print ("La ejecuion continua")

# For

my_list = [35, 19, 24, 56, 30, 30, 17]

for element in my_list: #pasa por cada elemento de la lista y los imprime.
    print(element)

my_tuple = (35, 1.55, "Janiel", "Flores", "Janiel")

for element in my_tuple: #pasa por cada elemento de la lista y los imprime.
    print(element)

my_set = {"Janiel", "Flores", 19}

for element in my_set: #pasa por cada elemento de la lista y los imprime.
    print(element)

my_other_dict = {"Nombre":"Janiel", "Apellido":"Flores", "Edad": 19, 1:"Python"}

for element in my_other_dict: #pasa por cada clave  del diccionario de datos y los imprime (al menos de que lo pasemos a lista y le pongamos .value())
    print(element)
    if element == "Edad":
        break #Romper el bucle
else:
    print("EL bucle for para diccionario ha finalizado")

print("La ejecucion continua")

for element in my_other_dict: #pasa por cada clave  del diccionario de datos y los imprime (al menos de que lo pasemos a lista y le pongamos .value())
    print(element)
    if element == "Edad":
        continue #Continuar el bucle
    print("Se ejecuta")
else: 
    print("EL bucle for para diccionario ha finalizado")