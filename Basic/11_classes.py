### Classes ###

class MyEmptyPerson: #Primera letra de cada palabra en mayusculas y sin espacios
    pass

print(MyEmptyPerson)
print(MyEmptyPerson())

class Person: 
    def __init__(self, name, surname, alias = "Sin alias"): #Constructor de la clase.
        self.full_name = f"{name} {surname} ({alias})" #propiedad publica.
        self.__name = name #variable privada o propiedad privada.
        self.__surname = surname

    def get_name (self):
        return self.__name

    def walk (self): #esto es una funcion para caminar no debe de llamar la clase person.
        print(f"{self.full_name} Esta caminando")

my_person = Person("Janiel", "Flores")
print(my_person.get_name())
my_person.walk()

my_other_person = Person("Brais", "Moure", "MoureDev")
print(my_other_person.full_name)
my_other_person.walk()

my_other_person.full_name = "Julio F Pa-Goza"
print(my_other_person)
my_other_person.walk()

my_other_person.full_name = 666
print(my_other_person.full_name)