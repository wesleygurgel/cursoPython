"""
Deque: Lista de Alta Perfomance
"""

from collections import deque

deq = deque('wesley')
print(deq)

print('\nAdicionando Elementos')
deq.append('y') # Adiciona l no Final
print(deq)

deq.appendleft('k') # Adiciona ao começo da lista
print(deq)

print('\nRemovendo elementos')
print(deq.pop())
print(deq)
print(deq.popleft())
print(deq)