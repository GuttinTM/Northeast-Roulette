# You can use this file to test whatever you want

from random import sample
lista1 = [True, True, True]
lista2 = [False, False, False]
lista3 = sample(lista1 + lista2, k=len(lista1 + lista2))
print(lista3)