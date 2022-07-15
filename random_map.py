from global_variables import get_random_int

# needs refactoring

mapa = {
    '1': [],
    '2': [],
    '3': [],
    '4': [],
    '5': [],
    '6': [],
    '7': [],
    '8': [],
    '9': [],
    '10': [],
    '11': [],
}
array_strings = []

# refactoring, odds tweaks
def generate_random_map():

    for linha in mapa:
        if linha == '9' or linha == '10' or linha == '11':
            
            for i in range(0, 30): # comprimento do mundo
                x = get_random_int(0, 2) # chances
                if x == 0:
                    mapa[linha].append('X')
                    mapa[linha].append('X')
                    mapa[linha].append('X')
                    mapa[linha].append('X')
                
                else:
                    mapa[linha].append(' ')
                    mapa[linha].append(' ')

        elif int(linha) % 2 == 0:
            for i in range(0, 30):
                x = get_random_int(0, 40)
                if x == 0:
                    mapa[linha].append('X')
                    mapa[linha].append('X')
                    mapa[linha].append('X')
                    mapa[linha].append('X')
                
                else:
                    mapa[linha].append(' ')
                    mapa[linha].append(' ')

        elif int(linha) % 2 != 0:
            for i in range(0, 30):
                x = get_random_int(0, 10)
                if x == 0:
                    mapa[linha].append('X')
                    mapa[linha].append('X')
                    mapa[linha].append('X')
                    mapa[linha].append('X')
                
                else:
                    mapa[linha].append(' ')
                    mapa[linha].append(' ')
 

    # converter para string usando join
    for linha, array in mapa.items():
        s = ''.join(array)
        array_strings.append(s)
    
    print("map generated")
    return array_strings


# print(generate_random_map())