### Listas ###

my_list = list()
my_other_list = []

print(len(my_list))

my_list = [35, 19, 24, 56, 30, 30, 17]

print(my_list)
print(len(my_list))

my_other_list = [35, 1.55, "Janiel", 'Flores']

print(type(my_list))
print(type(my_other_list))

print(my_other_list[0])
print(my_other_list[1])
print(my_other_list[-1])
print(my_other_list[-4])
print(my_list.count(30)) #Cuenta los que se repiten :D
#print(my_other_list[4]) IndexError no range
#print(my_other_list[-5]) IndexError no range

age , height, name, surname = my_other_list
print(name)

name , height, age, surname = my_other_list[2], my_other_list [1], my_other_list[0], my_other_list [3]
print(age)

print(my_list + my_other_list)
#print(my_list - my_other_list)

my_other_list.append("AppSum")
print(my_other_list)

my_other_list.insert(1, 'Negro')
print(my_other_list)

my_other_list[1] = "Rojo"
print(my_other_list)

my_other_list.remove("AppSum") #Se agrega el nombre de lo que quieres eliminar, no la posicion.
print(my_other_list)

my_list.remove(30)
print(my_list)

print(my_list.pop()) #pop agarra el elemento de la lista y lo saca, pero lo guarda.
print(my_list)

print(my_list.pop(2))
print(my_list)

my_pop_element =  my_list.pop(2)
print(my_pop_element)
print(my_list)

del my_list[2]
print(my_list)

my_new_list = my_list.copy()

my_list.clear()
print(my_list)
print(my_new_list)

my_new_list.reverse()
print(my_new_list)

my_new_list.sort()
print(my_new_list)

print(my_new_list[1:3])

my_list = "Hola Python"
print(my_list)
print(type(my_list))