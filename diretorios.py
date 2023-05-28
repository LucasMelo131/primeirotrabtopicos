"""
Faça um programa que leia uma string a qual representa um diretório. Gere um arquivo json com todos os arquivos deste diretório, dos seus diretórios filhos, dos filhos dos filhos, etc...
formato json: combinação de lista e dicionário
ITEM : nome, lista com todos os arquivos, diretórios(lista)
diretório é uma lista de ITEM
OS -> PESQUISAR
"""

import os
import json

path = input("Entre com o caminho do diretório: ")
diretorio = list()
item = dict()

for dpath,dirs,files in os.walk(path):
    print(dpath)
    for d in dirs:
        print(d)
    for f in files:
        print(f)

#list_dir = os.listdir(path)
#print(list_dir)