def getArray(*args):
    import os
    nome_arquivo = os.path.join(*args)
    array = []
    with open(nome_arquivo, 'r') as file:
        for row in file:
            array.append(int(row))
    return array