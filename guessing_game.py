import random

def main():
    target = random.randint(1, 100)
    number = int(input("Elige un numero del 1 al 100: "))
    guessing(target, number)
    

def guessing(target, number):
    if number == target:
        print("Has adivinado, Ganaste!")
    elif number < target:
        number = int(input("Elige un numero mayor: "))
        guessing(target, number)
    elif number > target:
        number =int(input("Elige un numero menor: "))
        guessing(target, number)    
    

if __name__ == '__main__':
    main()