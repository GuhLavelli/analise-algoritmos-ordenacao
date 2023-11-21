import os
from pprint import pprint
import matplotlib.pyplot as plt

class Resultados:
    def __init__(self):
        self.results_dict = {}
        for root, dirs, files in os.walk('/home/lavelli/AnaliseDeAlgoritmos/analise_algoritmos_ordenacao/algoritmos'):
            for file in files:
                if file == 'resultados.txt':
                    file_path = os.path.join(root, file)
                    name_algorithms = root.split("/")[-1]
                    self.results_dict[name_algorithms] = self.ler_resultados(file_path)
        
    def ler_resultados(self, file_path):
        with open(file_path, 'r') as resultados:
            cont = 0
            dic =  dict()
            dic['1000'] = {}
            dic['10000'] = {}
            dic['100000'] = {}
            for row in resultados:
                cont += 1
                row_splited = row.split(':')
                if cont < 12:
                    # Crescente 1000
                    if 'Array Crescente' in row:
                        dic['1000']['array_crescente'] = float(row_splited[-1].removesuffix('\n'))
                    elif 'Comparacoes Crescente' in row:
                        dic['1000']['comparacoes_crescente'] = int(row_splited[-1].removesuffix('\n'))
                    elif 'Trocas Crescente' in row:
                        dic['1000']['trocas_crescente'] = int(row_splited[-1].removesuffix('\n'))
                    # Aleatório 1000
                    elif 'Array Aleatório' in row:
                        dic['1000']['array_aleatorio'] = float(row_splited[-1].removesuffix('\n'))
                    elif 'Comparacoes Aleatório' in row:
                        dic['1000']['comparacoes_aleatorio'] = int(row_splited[-1].removesuffix('\n'))
                    elif 'Trocas Aleatório' in row:
                        dic['1000']['trocas_aleatorio'] = int(row_splited[-1].removesuffix('\n'))
                    # Decrescente 1000
                    elif 'Array Decrescente' in row:
                        dic['1000']['array_decrescente'] = float(row_splited[-1].removesuffix('\n'))
                    elif 'Comparacoes Decrescente' in row:
                        dic['1000']['comparacoes_decrescente'] = int(row_splited[-1].removesuffix('\n'))
                    elif 'Trocas Decrescente' in row:
                        dic['1000']['trocas_decrescente'] = int(row_splited[-1].removesuffix('\n'))
                elif cont < 24:
                    # Crescente 10000
                    if 'Array Crescente' in row:
                        dic['10000']['array_crescente'] = float(row_splited[-1].removesuffix('\n'))
                    elif 'Comparacoes Crescente' in row:
                        dic['10000']['comparacoes_crescente'] = int(row_splited[-1].removesuffix('\n'))
                    elif 'Trocas Crescente' in row:
                        dic['10000']['trocas_crescente'] = int(row_splited[-1].removesuffix('\n'))
                    # Aleatório 10000
                    elif 'Array Aleatório' in row:
                        dic['10000']['array_aleatorio'] = float(row_splited[-1].removesuffix('\n'))
                    elif 'Comparacoes Aleatório' in row:
                        dic['10000']['comparacoes_aleatorio'] = int(row_splited[-1].removesuffix('\n'))
                    elif 'Trocas Aleatório' in row:
                        dic['10000']['trocas_aleatorio'] = int(row_splited[-1].removesuffix('\n'))
                    # Decrescente 10000
                    elif 'Array Decrescente' in row:
                        dic['10000']['array_decrescente'] = float(row_splited[-1].removesuffix('\n'))
                    elif 'Comparacoes Decrescente' in row:
                        dic['10000']['comparacoes_decrescente'] = int(row_splited[-1].removesuffix('\n'))
                    elif 'Trocas Decrescente' in row:
                        dic['10000']['trocas_decrescente'] = int(row_splited[-1].removesuffix('\n'))
                elif cont < 36:
                    # Crescente 100000
                    if 'Array Crescente' in row:
                        dic['100000']['array_crescente'] = float(row_splited[-1].removesuffix('\n'))
                    elif 'Comparacoes Crescente' in row:
                        dic['100000']['comparacoes_crescente'] = int(row_splited[-1].removesuffix('\n'))
                    elif 'Trocas Crescente' in row:
                        dic['100000']['trocas_crescente'] = int(row_splited[-1].removesuffix('\n'))
                    # Aleatório 100000
                    elif 'Array Aleatório' in row:
                        dic['100000']['array_aleatorio'] = float(row_splited[-1].removesuffix('\n'))
                    elif 'Comparacoes Aleatório' in row:
                        dic['100000']['comparacoes_aleatorio'] = int(row_splited[-1].removesuffix('\n'))
                    elif 'Trocas Aleatório' in row:
                        dic['100000']['trocas_aleatorio'] = int(row_splited[-1].removesuffix('\n'))
                    # Decrescente 100000
                    elif 'Array Decrescente' in row:
                        dic['100000']['array_decrescente'] = float(row_splited[-1].removesuffix('\n'))
                    elif 'Comparacoes Decrescente' in row:
                        dic['100000']['comparacoes_decrescente'] = int(row_splited[-1].removesuffix('\n'))
                    elif 'Trocas Decrescente' in row:
                        dic['100000']['trocas_decrescente'] = int(row_splited[-1].removesuffix('\n'))
        return dic
    

    def plotar_grafico(self, metrica, nome_arquivo):
        tamanhos = ['1000', '10000', '100000']
        fig, ax = plt.subplots(figsize=(10, 6))
        for algoritmo, valores_tamanho in self.results_dict.items():
            valores = [valores_tamanho[tamanho].get(metrica, 0) for tamanho in tamanhos]
            pprint(self.results_dict)
            ax.plot(tamanhos, valores, label=algoritmo, marker='o')

        ax.grid(True)    
        plt.xlabel('Tamanho de Entrada')
        if metrica.split('_')[0] in 'comparacoes':
            plt.ylabel('Comparações')
        elif metrica.split('_')[0] in 'trocas':
            plt.ylabel('Trocas')
        else:
            plt.ylabel('Tempo')
        plt.yscale('log')
        metrica = metrica.replace('_', ' ')
        plt.title(f'Comparação de elementos ({metrica}) para diferentes algoritmos')
        plt.legend()
        plt.show()
        plt.savefig(nome_arquivo)
        plt.clf()

resultados = Resultados()

for metrica in ['array_crescente', 'array_aleatorio', 'array_decrescente', 'trocas_crescente', 'trocas_aleatorio', 'trocas_decrescente', 'comparacoes_crescente', 'comparacoes_aleatorio', 'comparacoes_decrescente']:
    resultados.plotar_grafico(metrica, metrica+'.png')
