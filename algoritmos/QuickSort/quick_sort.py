class QuickSort():
    def __init__(self):
        self.qtde_trocas = 0
        self.qtde_compar = 0

    def particao(self, A, esquerda, direita):
        pivo = A[esquerda]
        i = esquerda
        j = direita

        while i <= j:
            self.qtde_compar += 1
            while A[i] <= pivo:
                i += 1
                if i == direita:
                    break

            self.qtde_compar += 1
            while pivo <= A[j]:
                j -= 1
                if j == esquerda:
                    break

            if i >= j:
                break

            self.qtde_trocas += 1
            A[i], A[j] = A[j], A[i]

        self.qtde_trocas += 1
        A[esquerda], A[j] = A[j], pivo

        return j

    def quickSort(self, A, esquerda, direita):
        stack = [(esquerda, direita)]
        while stack:
            esq, dir = stack.pop()
            if esq < dir:
                pivo = self.particao(A, esq, dir)
                stack.append((esq, pivo - 1))
                stack.append((pivo + 1, dir))

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

  crescente = QuickSort()
  desordenado = QuickSort()
  decrescente = QuickSort()

  tempo_crescente = timeit.timeit(lambda: crescente.quickSort(array_crescente, 0, len(array_crescente)-1), number=1)
  tempo_desordenado = timeit.timeit(lambda: desordenado.quickSort(array_desordenado, 0, len(array_desordenado)-1), number=1)
  tempo_decrescente = timeit.timeit(lambda: decrescente.quickSort(array_decrescente, 0, len(array_decrescente)-1), number=1)


  with open('resultados.txt', 'a') as resultados:
    print("Array Crescente:", tempo_crescente, file=resultados)
    print("Comparacoes Crescente:", crescente.qtde_compar, file=resultados)
    print("Trocas Crescente:", crescente.qtde_trocas, file=resultados)
    print(file=resultados)
    print("Array Aleatório:", tempo_desordenado, file=resultados)
    print("Comparacoes Crescente:", desordenado.qtde_compar, file=resultados)
    print("Trocas Crescente:", desordenado.qtde_trocas, file=resultados)
    print(file=resultados)
    print("Array Decrescente:", tempo_decrescente, file=resultados)
    print("Comparacoes Crescente:", decrescente.qtde_compar, file=resultados)
    print("Trocas Crescente:", decrescente.qtde_trocas, file=resultados)
    print("==========================================================", file=resultados)

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