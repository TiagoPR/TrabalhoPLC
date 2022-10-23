import re, json

f = open("processos.txt", "r")
dic_linhas = {}
linha = ""
parent_proc = []
dic_pessoa = {}

for i in range(20):
    dic_linhas[i] = {}
    linha = next(f)
    info = re.split(r'::+',linha)
    dic_linhas[i]["numero"] = info[0]
    dic_linhas[i]["ano"] = info[1]
    dic_linhas[i]["pessoas"] = []
    for elem in info[2:-1]:
        #print(elem)
        parent_proc = re.findall(r'([a-zA-Z ]+)(\,[a-zA-Z ]+)(\.[ ]Proc\.[0-9]+)',elem)
        #print(parent_proc)
        if parent_proc:
            for pessoa in parent_proc:
                dic_pessoa = {"nome" : pessoa[0], "parentesco" : pessoa[1][1:], "processo" : pessoa[2][7:]}
                dic_linhas[i]["pessoas"].append(dic_pessoa)
        else:
            dic_pessoa = {"nome" : elem}
            dic_linhas[i]["pessoas"].append(dic_pessoa)

        
print(dic_linhas)
json_object = json.dumps(dic_linhas, indent=4)

with open("sample.json", "w") as outfile:
    outfile.write(json_object)