#!/usr/bin/python3
wartosci = input()
lista = wartosci.split(',')
print(lista, type(lista))


for i in range(len(lista)):    #zamieniamy na int
    lista[i] = int(lista[i])

lista = [int(i) for i in lista]  #drugi sposob
print(lista, type(lista))


#kolejny sposob
lista = list(map(int, lista))
print(lista)
