import random

def main():
    pasword = password_generator()
    print (pasword)

def password_generator():

    numbers = ['1','2','3','4','5','6','7','8','9', '0']
    uppers = [ 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    lowers = ['a', 'b', 'c', 'd', 'e', 'f','g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    symbols = ['!', '_' '@', '$', ' ', '%', '&', '=', '+', '-', '/']

    password = []

    for i in range(4):
        random_numbers = random.choice(numbers)
        password.append(random_numbers)

    random_symbol = random.choice(symbols)
    password.append(random_symbol)

    for i in range(4):
        random_uppers = random.choice(uppers)
        password.append(random_uppers)
        
    for i in range(4):
        random_lowers = random.choice(lowers)
        password.append(random_lowers)
    
    random_symbol = random.choice(symbols)
    password.append(random_symbol)

    password = ''.join(password)    
    return password


if __name__ == '__main__':
    main()