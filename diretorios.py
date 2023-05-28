"""
Faça um programa que leia uma string a qual representa um diretório. 
Gere um arquivo json com todos os arquivos deste diretório, 
dos seus diretórios filhos, dos filhos dos filhos, etc...
formato json: combinação de lista e dicionário
ITEM : nome, lista com todos os arquivos, diretórios(lista)
diretório é uma lista de ITEM
"""

import os
#import json


path = input("Entre com o caminho do diretório: ")
directory = []
for dirpath,dirs,files in os.walk(path):
    item = {}
    item["Nome"] = os.path.basename(dirpath)
    item["Arquivos"] = []
    item["Diretorios"] = []
    for file in files:
        item["Arquivos"].append(file)
    for folder in dirs:
        item["Diretorios"].append(folder)
    directory.append(item)
print(directory)