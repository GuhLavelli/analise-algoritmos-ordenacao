import random

# Defina o tamanho do array
# tamanho = 100000

# Crie um array com números aleatórios no intervalo de 1 a 1000
array_aleatorio = [random.randint(1, 1000) for _ in range(tamanho)]
nome_arquivo = "array_desordenado"+str(tamanho)+".txt"
with open(nome_arquivo, 'w') as arquivo:
    # Escreva cada elemento do array no arquivo, um por linha
    for numero in array_aleatorio:
        arquivo.write(str(numero) + '\n')

# Ordene o array em ordem crescente
array_aleatorio = [i for i in range(tamanho)]
nome_arquivo = "array_crescente"+str(tamanho)+".txt"
with open(nome_arquivo, "w") as arquivo:
    for numero in array_aleatorio:
        arquivo.write(str(numero) + '\n')

# Ordene o array em ordem decrescente
array_aleatorio.sort(reverse=True)
nome_arquivo = "array_decrescente"+str(tamanho)+".txt"
with open(nome_arquivo, "w") as arquivo:
    for numero in array_aleatorio:
        arquivo.write(str(numero) + '\n')