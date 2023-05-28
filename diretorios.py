import os
import json

path = input("Entre com o caminho do diretório: ")
list_dir = os.listdir(path)
print(list_dir)