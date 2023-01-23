### Classes ###

class MyEmplyPerson:
    pass 

print(MyEmplyPerson)
print(MyEmplyPerson())

class Person:
    def __init__(self, name, surname,alias = "Sin alias"):
        self.full_name = f"{name} {surname} ({alias})"
        self.__name = name
        self.__surname = surname

    def walk(self):
        print(f"{self.full_name} Esta caminando")

my_person  = Person("Brains", "Moure")
print(my_person.full_name)
my_person.walk()

my_other_person = Person("Brais", "Moure", "MoureDev")
print(my_person.full_name)
my_other_person.walk()
my_other_person.full_name = "Hector de Leon (EL loco de los perros)"
print(my_other_person.full_name)

my_other_person.full_name = 666 #Tipado debil (no respeta los tipos de valores)
print(my_other_person.full_name)