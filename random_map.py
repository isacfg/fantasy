import pygame, random

# needs refactoring

mapa = {
    '1l': [],
    '2l': [],
    '3l': [],
    '4l': [],
    '5l': [],
    '6l': [],
    '7l': [],
    '8l': [],
    '9l': [],
    '10l': [],
    '11l': [],
}
array_strings = []

def generate_random_map():
    for i in range(20):
        random_number = random.randint(1, 14)
        if random_number == 1:
            mapa['1l'].append('X')
            mapa['1l'].append('X')
            mapa['1l'].append('X')
        
        else:
            mapa['1l'].append(' ')
            mapa['1l'].append(' ')

    for i in range(20):
        random_number = random.randint(1, 16)
        if random_number == 1:
            mapa['2l'].append('X')
            mapa['2l'].append('X')
            mapa['2l'].append('X')
        
        else:
            mapa['2l'].append(' ')
            mapa['2l'].append(' ')

    for i in range(20):
        random_number = random.randint(1, 16)
        if random_number == 1:
            mapa['3l'].append('X')
            mapa['3l'].append('X')
            mapa['3l'].append('X')
        
        else:
            mapa['3l'].append(' ')
            mapa['3l'].append(' ')

    for i in range(20):
        random_number = random.randint(1, 18)
        if random_number == 1:
            mapa['4l'].append('X')
            mapa['4l'].append('X')
            mapa['4l'].append('X')
        
        else:
            mapa['4l'].append(' ')
            mapa['4l'].append(' ')

    for i in range(20):
        random_number = random.randint(1, 16)
        if random_number == 1:
            mapa['5l'].append('X')
            mapa['5l'].append('X')
            mapa['5l'].append('X')
        
        else:
            mapa['5l'].append(' ')
            mapa['5l'].append(' ')

    for i in range(20):
        random_number = random.randint(1, 20)
        if random_number == 1:
            mapa['6l'].append('X')
            mapa['6l'].append('X')
            mapa['6l'].append('X')
        
        else:
            mapa['6l'].append(' ')
            mapa['6l'].append(' ')

    for i in range(20):
        random_number = random.randint(1, 16)
        if random_number == 1:
            mapa['7l'].append('X')
            mapa['7l'].append('X')
            mapa['7l'].append('X')
        
        else:
            mapa['7l'].append(' ')
            mapa['7l'].append(' ')

    for i in range(20):
        random_number = random.randint(1, 15)
        if random_number == 1:
            mapa['8l'].append('X')
            mapa['8l'].append('X')
            mapa['8l'].append('X')
        
        else:
            mapa['8l'].append(' ')
            mapa['8l'].append(' ')

    for i in range(20):
        random_number = random.randint(1, 14)
        if random_number == 1:
            mapa['9l'].append('X')
            mapa['9l'].append('X')
            mapa['9l'].append('X')
        
        else:
            mapa['9l'].append(' ')
            mapa['9l'].append(' ')

    for i in range(20):
        random_number = random.randint(1, 8)
        if random_number == 1:
            mapa['10l'].append('X')
            mapa['10l'].append('X')
            mapa['10l'].append('X')
        
        else:
            mapa['10l'].append(' ')
            mapa['10l'].append(' ')
        
    for i in range(20):
        random_number = random.randint(1, 6)
        if random_number == 1:
            mapa['11l'].append('X')
            mapa['11l'].append('X')
            mapa['11l'].append('X')
        
        else:
            mapa['11l'].append(' ')
            mapa['11l'].append(' ')


    # converter para string usando join
    for linha, array in mapa.items():
        s = ''.join(array)
        array_strings.append(s)
    
    return array_strings


print(generate_random_map())