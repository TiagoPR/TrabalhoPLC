import re

f = open("processos.txt", "r")
ant = ""
dic_nome = {}
dic_apelido = {}
ano = ""
info = []
nome_proprio = ""
nome_apelido = ""
seculo = 0

def add_dic(pessoa):

    if "Doc.danificado" not in pessoa:
        nome = re.match(rf'([A-Z][a-z]+)([ ]+[A-Z][a-z]+)+',pessoa)
        if nome:
            nome_proprio = nome.group(1)
            nome_apelido = nome.group(2).lstrip()

            if nome_proprio not in dic_nome[seculo]:
                dic_nome[seculo][nome_proprio] = 1
            else:
                dic_nome[seculo][nome_proprio] += 1

            if nome_apelido not in dic_apelido[seculo]:
                dic_apelido[seculo][nome_apelido] = 1
            else:
                dic_apelido[seculo][nome_apelido] += 1

for linha in f:
    if ant != linha:
        info = re.split(r'::+',linha)
        #print(info)
        if info[0] != "\n":
            ano = info[1][0:4]
            #print(ano)
            if ano[2:4] == "00":
                seculo = int(ano[0:2])
            else:
                seculo = int(ano[0:2]) + 1

            if seculo not in dic_nome:
                dic_nome[seculo] = {}
            if seculo not in dic_apelido:
                dic_apelido[seculo] = {}

            for elem in info[2:-1]:
                parent_proc = re.findall(r'([a-zA-Z ]+)(\,[a-zA-Z ]+)(\.[ ]Proc\.[0-9]+)',elem)
                if parent_proc:
                    for pessoa in parent_proc:
                        add_dic(pessoa[0])
                else:
                    add_dic(elem)
            
frase = input("Qual o seculo? ")
while frase != "":
    seculo = int(frase)
    nome = input("Qual o nome? ")
    apelido = input("Qual o apelido? ")
    if seculo in dic_nome and int(frase) in dic_apelido:
        print("Seculo certo!!!")
        if nome in dic_nome[seculo] and apelido in dic_apelido[seculo]:
            print("Seculo: ",seculo, "Nome: ",dic_nome[seculo][nome], "Apelido: ",dic_apelido[seculo][apelido])
    else:
        print("Não existe processo")
    frase = input("Qual o seculo?")
