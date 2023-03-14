### Challanges ###

"""
Reto #0: EL FAMOSO "FIZZ BUZZ”
* Escribe un programa que muestre por consola (con un print) los
 * números de 1 a 100 (ambos incluidos y con un salto de línea entre
 * cada impresión), sustituyendo los siguientes:
 * - Múltiplos de 3 por la palabra "fizz".
 * - Múltiplos de 5 por la palabra "buzz".
 * - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
"""


def fizzbuzz():
    for index in range(1, 101):
        if index % 3 == 0 and index % 5 == 0:
            print("fizzbuzz")
        elif index % 3 == 0:
            print("fizz")
        elif index % 5 == 0:
            print("buzz")
        else:
            print(index)


fizzbuzz()

"""
Reto #1: ¿ES UN ANAGRAMA?
* Escribe una función que reciba dos palabras (String) y retorne
 * verdadero o falso (Bool) según sean o no anagramas.
 * - Un Anagrama consiste en formar una palabra reordenando TODAS
 *   las letras de otra palabra inicial.
 * - NO hace falta comprobar que ambas palabras existan.
 * - Dos palabras exactamente iguales no son anagrama.
"""


def is_anagram(word_one, word_two):
    if word_one.lower() == word_two.lower():
        return False
    return sorted(word_one.lower()) == sorted(word_two.lower())


print(is_anagram("Amor", "Roma"))
print(sorted("amor".lower()), sorted("Roma".lower()))

"""
  Escribe un programa que imprima los 50 primeros números de la sucesión
  de Fibonacci empezando en 0.
  - La serie Fibonacci se compone por una sucesión de números en
    la que el siguiente siempre es la suma de los dos anteriores.
    0, 1, 1, 2, 3, 5, 8, 13...

 """
print("------------ reto 02 La sucesión de FIBONACCI ----------------")


def fibonacci():
    prev = 0
    next = 1
    fibo = list()
    for index in range(0, 50):
        # print(prev)
        fibo.append(f"{index}: {prev}")
        fib = prev + next
        prev = next
        next = fib
    print(fibo)


fibonacci()

"""
 * Escribe un programa que se encargue de comprobar si un número es o no primo.
 * Hecho esto, imprime los números primos entre 1 y 100.
"""
print("------------ reto 03 Es un numero primo? ----------------")


def is_prime():
    primos = list()
    for number in range(1, 101):
        if number >= 2:

            is_divisible = False

            for index in range(2, number):
                if number % index == 0:
                    is_divisible = True
                    break

            if not is_divisible:
                primos.append(number)
    print(primos)


is_prime()


"""
  Crea un programa que invierta el orden de una cadena de texto
  sin usar funciones propias del lenguaje que lo hagan de forma automática.
  - Si le pasamos "Hola mundo" nos retornaría "odnum aloH"
"""
print("------------ reto 06 INVIRTIENDO CADENAS ----------------")


def cadena(text):
    inver = ""
    for caracter in text:
        inver = caracter + inver
    return inver


print(cadena("Hola mundo"))
