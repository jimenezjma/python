import random
import os

def main():

    target = random_word()
    arrow = guides(target)

    while arrow != target:
        os.system('cls')
        print('Adivina la palabra!')
        print(stringify(arrow))
        char = input('Ingresa una letra: ')
        char  = char.upper()
        comparisons(char, target, arrow)
    else:
        os.system('cls')
        print(f'Has ganado! la palabra era: \n {stringify(target)}!')
            


#funcion para definir la palabra a adivinar, limpiarla y
# convertirla en un diccionario donde cada valor es una letra de la palabra:
def random_word():
    with open('./data.txt', 'r', encoding='utf-8') as f:
        objective = random.choice(f.readlines())
    objective = objective.rstrip()
    objective = objective.replace('á', 'a')
    objective = objective.replace('é', 'e')
    objective = objective.replace('í', 'i')
    objective = objective.replace('ó', 'o')
    objective = objective.replace('ú', 'u')
    objective = objective.upper()
    objective = dict(enumerate(objective))
    return objective

#funcion para definir el diccionario guia con el cual se comparara la palabra
def guides(dictionary):
    guides = ['_ ' for i in range(len(dictionary))]
    guides = dict(enumerate(guides))
    return guides

#funcion para hacer las comparaciones y sobreescribir el diccionario guia
def comparisons(char, word, guide):
    if char in word.values():
        for key, value in word.items():
            if value == char:
                guide[key] = char
            else:
                continue

#funcion para convertir diccionarios en strings
def stringify(dictionary):
    string = ''
    for key, value in dictionary.items():
        string += value
    return string
        

if __name__ == '__main__':
    main()