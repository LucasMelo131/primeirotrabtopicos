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

def directories (caminho,lista):
    """_summary_

    Args:
        caminho (_string_): _description_
        lista (_list_): _description_

    Returns:
        _list_: _description_
    """
    for dirpath,dirs,files in os.walk(caminho):
        item = {}
        item["Nome"] = os.path.basename(dirpath)
        item["Arquivos"] = []
        item["Diretorios"] = []
        for file in files:
            item["Arquivos"].append(file)
        for folder in dirs:
            item["Diretorios"].append(folder)
        lista.append(item)
    return lista

path = input("Entre com o caminho do diretório: ")
directory = []
directory = directories(path,directory)
print(directory)