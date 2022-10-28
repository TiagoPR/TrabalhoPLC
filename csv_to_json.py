import re

f = open("ex5.csv", "r")
list = []
primeira = next(f)

atributos = re.split(',',primeira)
atributos[-1] = atributos[-1][:-1]
a = 0
for atributo in atributos:
    if atributo == '':
        break
    a += 1

print(atributos[:a])
tamanho = len(atributos)
dic = {}

for linha in f:
    valores = re.split(',',linha)
    for j in range(a-2):
        '''
        if tamanho-1 == j:
            dic[atributos[j]] = valores[j][:-1]
        else:
        '''
        dic[atributos[j]] = valores[j]
    dic[atributos[a-1]] = []
    for j in range(a-1,tamanho):
        dic[atributos[a-1]].append(valores[j])
    list.append(dic)
print(list)
