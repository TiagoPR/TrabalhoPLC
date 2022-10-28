import re

f = open("ex5.csv", "r")
list = []
primeira = next(f)

atributos = re.split(',',primeira)
atributos[-1] = atributos[-1][:-1]
tamanho = len(atributos)
dic = {}
for linha in f:
    valores = re.split(',',linha)
    for j in range(tamanho):
        if tamanho-1 == j:
            dic[atributos[j]] = valores[j][:-1]
        else:
            dic[atributos[j]] = valores[j]
    list.append(dic)
print(list)
