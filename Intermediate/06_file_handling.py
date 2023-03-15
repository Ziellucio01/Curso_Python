### File Handling  ###

import xml
import csv
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

with open("Intermediate/my_file.json") as my_other_file:
    for line in my_other_file.readlines():
        print(line)

json_dict = json.load(open("Intermediate/my_file.json"))
print(json_dict)
print(type(json_dict))
print(json_dict["name"])

# .csv file
csv_file = open("Intermediate/my_file.csv", "w+")
csv_write = csv.writer(csv_file)
csv_write.writerow(["name", "surname", "age", "language", "website"])
csv_write.writerow(["Brais", "Moure", "35", "Python", "https://moure.dev"])
csv_write.writerow(["Roswell", "", "2", "Cobol", ""])

csv_file.close()

with open("Intermediate/my_file.csv") as my_other_file:
    for line in my_other_file.readlines():
        print(line)
# xlsx file
# import xlrd # debe instalarse el modulo


#  xml file
