import re, json

f = open("alunos5.csv", "r")
list = []
primeira = next(f)
print(primeira)
funcao = re.search(r'::([A-Za-z]+)',primeira)
primeira = re.sub(r'(Notas){[0-9](\,[0-9])?}(::[A-Za-z]+)?',r'\1',primeira)

atributos = re.split(',',primeira)
atributos[-1] = atributos[-1][:-1]
print(atributos)
a = 0
for atributo in atributos:
    if atributo == '':
        break
    a += 1

if funcao:
    atributos[a] = funcao.group(1)
print("atr: ",atributos[:a+1])

for linha in f:
    dic = {}
    #print("linha: ",linha)
    valores = re.split(',',linha)
    #print("valores: ", valores)
    for j in range(a-1):
        dic[atributos[j]] = valores[j]
    if len(atributos) > 3:
        dic[atributos[a-1]] = []
        #print("dicionario: ", dic)
        for j in range(a-1,len(valores)-1):
            if valores[j] != '':
                dic[atributos[a-1]].append(int(valores[j]))
        if valores[-1] != "\n" and valores[-1] != '':
            print(dic)
            dic[atributos[a-1]].append(int(valores[-1][0:-1]))
        
        if atributos[a] == 'sum':
            dic[atributos[a]] = sum(dic[atributos[a-1]])
        elif atributos[a] == 'media':
            dic[atributos[a]] = sum(dic[atributos[a-1]])/len(dic[atributos[a-1]])
    else:
        #print(dic)
        dic[atributos[a-1]] = valores[a-1][:-1]
    list.append(dic)
    print("segundo dicionario: ", dic)

print("\n\n",list)

json_object = json.dumps(list, indent=4)

with open("Notas.json", "w") as outfile:
    outfile.write(json_object)

