### Diccionaries ###

my_dict = dict()
my_other_dict = {}

print(type(my_dict))
print(type(my_other_dict))

my_other_dict = {"Nombre":"Janiel", "Apellido":"Flores", "Edad": 19, 1:"Python"}

my_dict = {
    "Nombre":"Janiel", 
    "Apellido":"Flores", 
    "Edad": 19, 
    "Lenguajes": {"Python","Swift", "Kotlin"}, # Diccionario se pueden guardar datos de tipo clave-valor.
    1:1.61
    }

print(my_other_dict)
print(my_dict)

print(len(my_other_dict)) #len solo va a leer las claves que esten en el diccionario.
print(len(my_dict))

print(my_dict["Nombre"])

my_dict["Nombre"] = "Pedrito"
print(my_dict["Nombre"])

print(my_dict[1])

my_dict["Calle"] = "Charles de Gaulle"
print(my_dict)

del my_dict["Calle"] #forma de eliminar un solo elemento en el diccionario.
print(my_dict)

print("Janiel" in my_dict) #cuando se busca dentro de la lista, se busca la clave.
print("Nombre" in my_dict)

print(my_dict.items())
print(my_dict.keys()) #solo retorna las claves o llaves del diccionario
print(my_dict.values()) #solo retorna los valores del diccionario

my_list = ["Nombre", 1, "Piso"]

my_new_dict = dict.fromkeys((my_list))
print(my_new_dict)
my_new_dict = dict.fromkeys(("Nombre", 1, "Piso"))
print(my_new_dict)
my_new_dict = dict.fromkeys(my_dict) #hacer esto es como hacer una copia del diccionario pero solo se queda con las claves.
print(my_new_dict)
my_new_dict = dict.fromkeys(my_dict, "Janiel") #esto le pasa el valor Janiel a todas las Claves del diccionario.
print(my_new_dict)

my_values = my_new_dict.values()
print(type(my_values))

print(my_new_dict.values())
print(list(dict.fromkeys(list(my_new_dict.values())).keys()))
print(tuple(my_new_dict))
print(set(my_new_dict))