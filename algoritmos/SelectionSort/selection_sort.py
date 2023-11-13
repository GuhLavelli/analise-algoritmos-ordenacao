class SelectionSort():
    def __init__(self):
        self.qtde_trocas = 0
        self.qtde_compar = 0

    def selectionSort(self, array):
        length = len(array)
        
        for i in range(length - 1):
            minIndex = i
            
            for j in range(i + 1, length):
                self.qtde_compar += 1  # Incrementa o contador de comparações
                if array[j] < array[minIndex]:
                    minIndex = j

            # Troca os elementos se necessário
            if i != minIndex:
                array[i], array[minIndex] = array[minIndex], array[i]
                self.qtde_trocas += 1  # Incrementa o contador de trocas

        return array
    
#Problemas de caminho ao executar pelo Linux
path = '/home/lavelli/AnaliseDeAlgoritmos/analise_algoritmos_ordenacao'
import sys
sys.path.append(path)

from test_arrays import getArray
import matplotlib.pyplot as plt
import timeit

tamanhos = ['1000', '10000', '100000']
arrays = dict()
for tam in tamanhos:
  array_crescente = getArray(path+"/test_arrays",tam+'_elements', 'array_crescente'+tam+'.txt')
  array_desordenado = getArray(path+"/test_arrays",tam+'_elements', 'array_desordenado'+tam+'.txt')
  array_decrescente = getArray(path+"/test_arrays",tam+'_elements', 'array_decrescente'+tam+'.txt')

  crescente = SelectionSort()
  desordenado = SelectionSort()
  decrescente = SelectionSort()
  

  tempo_crescente = timeit.timeit(lambda: crescente.selectionSort(array_crescente), number=1)
  print("Array Crescente:", tempo_crescente)
  print("Comparacoes Crescente:", crescente.qtde_compar)
  print("Trocas Crescente:", crescente.qtde_trocas)
  print()
  tempo_desordenado = timeit.timeit(lambda: desordenado.selectionSort(array_desordenado), number=1)
  print("Array Aleatório:", tempo_desordenado)
  print("Comparacoes Crescente:", desordenado.qtde_compar)
  print("Trocas Crescente:", desordenado.qtde_trocas)
  print()
  tempo_decrescente = timeit.timeit(lambda: decrescente.selectionSort(array_decrescente), number=1)
  print("Array Decrescente:", tempo_decrescente)
  print("Comparacoes Crescente:", decrescente.qtde_compar)
  print("Trocas Crescente:", decrescente.qtde_trocas)
  print("==========================================================")

  # Gráfico de tempo
  plt.plot([0, tempo_crescente],[1,1], 'o-',label="Melhor Caso", color='g')
  plt.plot([0, tempo_desordenado],[2,2], 'o-',label="Caso Médio", color='b')
  plt.plot([0,tempo_decrescente],[3,3], 'o-',label="Pior Caso", color='r')

  plt.title("Tempo de execução - "+tam+" Elementos")
  plt.yticks([])
  plt.xlabel("Tempo de Execução (s)")
  plt.legend()

  plt.savefig("Tempo_"+tam+"_elementos.jpg")
  plt.clf()

  # Gráfico de Trocas x Tempo
  plt.plot([0, tempo_crescente],[0, crescente.qtde_trocas], 'o-',label="Melhor Caso", color='g')
  plt.plot([0, tempo_desordenado],[0, desordenado.qtde_trocas], 'o-',label="Caso Médio", color='b')
  plt.plot([0,tempo_decrescente],[0, decrescente.qtde_trocas], 'o-',label="Pior Caso", color='r')

  plt.title("Trocas x Tempo - "+tam+" Elementos")
  plt.xlabel("Tempo de Execução (s)")
  plt.legend()

  plt.savefig("Tempo_Troca_"+tam+"_elementos.jpg")
  plt.clf()
  
  # Gráfico de Comparacoes x Tempo
  plt.plot([0, tempo_crescente],[0, crescente.qtde_compar], 'o-', label="Melhor Caso", color='g')
  plt.plot([0, tempo_desordenado],[0, desordenado.qtde_compar], 'o-', label="Caso Médio", color='b')
  plt.plot([0,tempo_decrescente],[0, decrescente.qtde_compar], 'o-',label="Pior Caso", color='r')

  plt.title("Comparações x Tempo - "+tam+" Elementos")
  plt.xlabel("Tempo de Execução (s)")
  plt.legend()

  plt.savefig("Comparacoes_Tempo_"+tam+"_elementos.jpg")
  plt.clf()

  
  # Gráfico de Comparações x Trocas
  plt.plot([0, crescente.qtde_compar],[0, crescente.qtde_trocas], 'o-', label="Melhor Caso", color='g')
  plt.plot([0, desordenado.qtde_compar],[0, desordenado.qtde_trocas], 'o-', label="Caso Médio", color='b')
  plt.plot([0, decrescente.qtde_compar],[0, decrescente.qtde_trocas], 'o-', label="Pior Caso", color='r')

  plt.title("Comparações x Trocas - "+tam+" Elementos")
  plt.xlabel("Tempo de Execução (s)")
  plt.legend()

  plt.savefig("Comparacoes_Trocas"+tam+"_elementos.jpg")
  plt.clf()