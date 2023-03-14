### File Handling  ###

import json
import os

# .txt file
text_file = open("Intermediate/my_file.txt", "r+")  # Leer y Escribir
text_file.write(
    "Mi nombre es Brais\nMi apellido es Moure\n35 años\nY mi lenguaje preferido es Python")

# print(text_file.read())
print(text_file.read(10))
print(text_file.readline())
print(text_file.readline())
for line in text_file.readlines():
    print(line)

text_file.write("\nAunque también me gusta Kotlin")
print(text_file.readline())

text_file.close()


with open("Intermediate/my_file.txt", "a") as my_other_file:
    my_other_file.write("\nY Swift")

# os.remove("Intermediate/my_file.txt")

# .json file

json_file = open("Intermediate/my_file.json", "w+")

json_text = {
    "name": "Brais",
    "surname": "Moure",
    "age": 35,
    "language": ["Python", "Swift", "Kotlin"],
    "website": "https://moure.dev"}

json.dump(json_text, json_file, indent=2)

json_file.close()
for line in json_file.readline():
    print(line)

with open("Intermediate/my_file.json") as my_other_file:
    for line in my_other_file.readline():
        print(line)
