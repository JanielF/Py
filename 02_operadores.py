### Operadores Aritmeticos###

print(3 + 4)
print(3 - 4)
print(3 * 4)
print(3 / 4)
print(10 % 3)
print(10 // 3)
print(2 ** 3)
print(2 ** 3 + 3 - 7 / 1 // 4)


print('Hola ' + 'Python ' + 'Que tal ')  
print("Hola " + str(5))
print("Hola " * 5)
print("Hola " * (2 ** 3))

my_float = 2.5 * 2
print('Hola ' * int(my_float))

### Operadores Comparativos ###

print(3 > 4)
print(3 < 4)
print(3 <= 4)
print(4 >= 4)
print(3 == 4)
print(3 != 4)

print('Hola' > 'Python')
print('Hola' < 'Python')
print('aaa' >= 'aabaa') #Ordenacion alfabetica
print(len('aaaa') >= len("abaa")) # CUenta caracteres
print('Hola' <= 'Python')
print('Hola' == 'Hola')
print('Hola' != 'Python')

### Operadores Logicos ###

print(3 > 4 and 'Hola' > 'Python')
print(3 > 4 or 'Hola' > 'Python')
print(3 < 4 and 'Hola' < 'Python')
print(3 < 4 or 'Hola' > 'Python')
print(3 < 4 or ('Hola' > 'Python' and 4 == 4))
print(not(3 > 4 )) #not es negar toda la condicion