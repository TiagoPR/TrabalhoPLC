import re

f = open("processos.txt", "r")
dic = {}
ano = ""
for linha in f:
    y = re.match(r'([1-9][0-9]*)::([0-9]{4})', linha)
    if y:
        ano = y.group(2)
        if ano not in dic:
            dic[ano] = 1
        else:
            dic[ano] += 1

frase = input("Qual o ano? ")
while frase != "":
    if frase in dic:
        print("Ano: ",frase, "Resultado: ",dic[frase])
    else:
        print("Não existe processo")
    frase = input("Qual o ano?")
print(dic)