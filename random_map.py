from global_variables import get_random_int


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
        
        tiles_letters = ['not', 'X', 'F', 'G', 'I']
        if int(linha) > 5:
            for i in range(0, 30):
                x = get_random_int(0, 10)
                if x == 0:
                    mapa[linha].append(tiles_letters[get_random_int(1,4)])
                    mapa[linha].append(tiles_letters[get_random_int(1,4)])
                    mapa[linha].append(tiles_letters[get_random_int(1,4)])
                    mapa[linha].append(tiles_letters[get_random_int(1,4)])
                
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

def reset_map():
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
    print("map reseted")