import re

        
f = open("processos.txt", "r")

parentesco = {}

aux = ''
for linha in f:
    info = re.split(r'::+',linha)
    if len(info)> 4:
        aux = re.findall(r'\,(([A-Z][a-z]+[ ]*)+)\.[ ]*Proc',info[-2])
        for pare in aux:
            if pare[0] not in parentesco:
                parentesco[pare[0]] = 1
            else:
                parentesco[pare[0]] += 1

frase = input("Qual o parentesco? ")
while frase != "":
    if frase in parentesco:
        print("Parentesco: ",frase, "Resultado: ",parentesco[frase])
    else:
        print("Não existe parentesco")
    frase = input("Qual o parentesco?")