from curses import flushinp
import re

        
f = open("processos.txt", "r")

parentesco = {}

aux = ''
for linha in f:
    info = re.split(r'::+',linha)
    print(info)
    if len(info)> 4:
        print(info[-2])
        aux = re.findall(r'\,(([A-Z][a-z]+[ ]*)+)\.',info[-2])
        for pare in aux:
            print(pare)
            if pare[0] not in parentesco:
                parentesco[pare[0]] = 1
            else:
                parentesco[pare[0]] += 1

print(parentesco)