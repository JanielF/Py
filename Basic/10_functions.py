### Functions ###


def my_function ():
    print("Esto es una funcion")

my_function ()
my_function ()
my_function ()

def sum_two_values (first_value : int, second_value): #aca se le pasan los paramatros a usar pero aunque se defina el tipo, si la operacion puede ser realizada con string lo hara de todas maneras.
    print(first_value + second_value)

sum_two_values(5, 7)
sum_two_values(54754, 71231)
sum_two_values("5", "7")
sum_two_values(1.4, 5.2)

def sum_two_values_with_return (first_value, second_value):
    my_sum = first_value + second_value
    return my_sum

my_result = sum_two_values(1.4, 5.2) #Este da None ya que no retorna nada.
print(my_result)

my_result = sum_two_values_with_return(10, 5)
print(my_result)

def print_name (name, surname):
    print(f"{name} {surname}")

print_name(surname="Flores", name="Janiel") #se pueden reordenar los parametros asignados.

def print_name_with_default (name, surname, alias = "Sin alias"): #forma tener valor asignado dentro de una funcion.
    print(f"{name} {surname} {alias}")

print_name_with_default("Janiel", "Flores")
print_name_with_default("Janiel", "Flores", "Janielito")

def print_upper_texts (*text): #con el *(variable) puedes pasar todos los parametros que quieras.
    for text in text:
        print(text.upper())

print_upper_texts("Hola", "Python", "Janielito")
print_upper_texts("Hola")