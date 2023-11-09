import random
import timeit

# Função BubbleSort
def bubbleSort(array):
    
  # loop to access each array element
  for i in range(len(array)):

    # loop to compare array elements
    for j in range(0, len(array) - i - 1):

      # compare two adjacent elements
      # change > to < to sort in descending order
      if array[j] > array[j + 1]:

        # swapping elements if elements
        # are not in the intended order
        temp = array[j]
        array[j] = array[j+1]
        array[j+1] = temp
from test import getArray
tam = '1000'
array_crescente = getArray('test', tam+'_elements', 'array_crescente'+tam+'.txt')
array_desordenado = getArray('test', tam+'_elements', 'array_desordenado'+tam+'.txt')
array_decrescente = getArray('test', tam+'_elements', 'array_decrescente'+tam+'.txt')


tempo = timeit.timeit(lambda: bubbleSort(array_crescente), number=1)
print("Array Crescente:", tempo)
tempo = timeit.timeit(lambda: bubbleSort(array_desordenado), number=1)
print("Array Aleatório:", tempo)
tempo = timeit.timeit(lambda: bubbleSort(array_decrescente), number=1)
print("Array Decrescente:", tempo)