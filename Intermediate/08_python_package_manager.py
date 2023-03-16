### Python Package Manager  ###

# PIP herramienta para instalar paquetes en python https://pypi.org

# import pandas  # pip install pandas
from mypackage import arithmetics
import mypackage
import requests
import numpy  # pip install numpy

print(numpy.version.version)

numpy_array = numpy.array([35, 24, 60, 52, 30, 30, 17])

print(type(numpy_array))

print(numpy_array * 2)

# pandas

# pip list
# pip unistall pandas
# pip show numpy
# import requests

response = requests.get("https://pokeapi.co/api/v2/pokemon?limit=151")
print(response)
print(response.status_code)
print(response.json())

for index, pokemon in enumerate(response.json()["results"]):
    pokemon_name = pokemon["name"]
    print(f"#{index +1} {pokemon_name}")

# Arithmetics Package

# import mypackage
# from mypackage import arithmetics
print(mypackage.arithmetics.sum_two_values(1, 4))
