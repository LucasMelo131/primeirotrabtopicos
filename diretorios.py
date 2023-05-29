"""
Faça um programa que leia uma string a qual representa um diretório. 
Gere um arquivo json com todos os arquivos deste diretório, 
dos seus diretórios filhos, dos filhos dos filhos, etc...
formato json: combinação de lista e dicionário
ITEM : nome, lista com todos os arquivos, diretórios(lista)
diretório é uma lista de ITEM
"""

import os
import json

def directory (caminho,pasta):
    item = {}
    item["Nome"] = os.path.basename(caminho)
    item["Arquivos"] = []
    item["Diretorios"] = []
    for entrada in os.scandir(caminho):
        if entrada.is_file():
            item["Arquivos"].append(entrada.name)
        if entrada.is_dir():
            item["Diretorios"] = directory(entrada.path,item["Diretorios"])
    pasta.append(item)
    return pasta

path = input("Entre com o caminho do diretório: ")
diretorio = []
diretorio = directory(path,diretorio)
with open("diretorios.json","w",encoding="UTF-8") as jsonfile:
    json_object = json.dumps(diretorio,indent=4,ensure_ascii=False)
    jsonfile.write(json_object)
