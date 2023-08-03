import json

with open("generated.json", "r") as arquivo:
    conteudo_arquivo = arquivo.read()

parsed = json.loads(conteudo_arquivo)
lista_chaves = None
if isinstance(parsed, list):
    for item in parsed:
        if isinstance(item, dict):
            if lista_chaves == None:
                lista_chaves = list(item)
            if lista_chaves != list(item):
                lista_chaves = None
                break

print(lista_chaves)