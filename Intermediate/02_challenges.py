### Challanges ###

"""
EL FAMOSO "FIZZ  BUZZ"
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
¿ES UN ANAGRAMA?
"""

def is_anagram(word_one, word_two):
    if word_one.lower() == word_two.lower():
        return False
    elif 
    return word_one == word_two

print(is_anagram("Amor", "Roma"))