### Sets ###

my_set = set()
my_other_set = {}

print(type(my_set))
print(type(my_other_set)) # Inicialmente es un diccionario

my_other_set = {"Janiel", "Flores", 19}
print(type(my_other_set))

print(len(my_other_set))

my_other_set.add("Janielito")

print(my_other_set) # No es una estructura ordenada.

my_other_set.add("Janielito") #Un set no admite repetidos.

print(my_other_set)

print("Janiel" in my_other_set) #forma de comprobar si el elemento existe dentro de un set.
print("Janie" in my_other_set)

my_other_set.remove("Janielito")
print(my_other_set)

my_other_set.clear()
print(len(my_other_set))

del my_other_set # del elimina el objeto por lo tanto ya no se puede hacer ningun print ni acceder a ella, ya que no existe.
#print(my_other_set)

my_set = {"Janiel", "Flores", 19}
my_list = list(my_set)
print(my_list)
print(my_list[0])

my_other_set = {"Kotlin", "Swift", "Python"}

my_new_set = my_set.union(my_other_set)
print(my_new_set.union(my_new_set).union(my_set).union({"JavaScript", "C#"}))

print(my_new_set.difference(my_set))