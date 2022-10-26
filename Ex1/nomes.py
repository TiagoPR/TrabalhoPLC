import re

f = open("processos.txt", "r")
ant = ""
dic = {}
ano = ""
for linha in f:
    if ant != linha:
        
