### Tuples ###

my_tuple = tuple()
my_other_tuple = ()

my_tuple = (35, 1.55, "Janiel", "Flores", "Janiel")
my_other_tuple = (35, 50, 40)

print(my_tuple)
print(type(my_tuple))

print(my_tuple[0])
print(my_tuple[-1])
#print(my_tuple[4]) IndexError
#print(my_tuple[-6]) IndexError

print(my_tuple.count("Janiel"))
print(my_tuple.index("Flores"))
print(my_tuple.index("Janiel"))

#my_tuple[1] = 1.80 'tuple' object does not support item assignment

mi_nueva_tupla = my_tuple + my_other_tuple
print(mi_nueva_tupla)

print(mi_nueva_tupla[3:6])

my_tuple = list(my_tuple)
print(type(my_tuple))

my_tuple[4] = "Appsum"
my_tuple.insert(1, "Negro")
my_tuple = tuple(my_tuple)
print(tuple(my_tuple))
print(type(my_tuple))

del my_tuple
#print(my_tuple) NameError: name 'my_tuple' is not defined