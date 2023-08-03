import json
"""Programa para fazer análise de json
mais comentario
novo codigo atualizado
outra coisa"""
def main():
    with open("bigdado.json", "r") as file:
        conteudo_json = file.read()
    lista = json.loads(conteudo_json)
    dicio_names = coleta_dados("name", lista)
    dicio_phones = coleta_dados("phone", lista) #comentário 
    likey_names = list(dicio_names)
    likey_phones = list(dicio_phones)
    for i in range(len(likey_names)):
        print(f"Nome: {dicio_names[likey_names[i]]} | fone: {dicio_phones[likey_phones[i]]}")


def coleta_dados(dado:str, lista):    
    dicio = dict()
    for i in range(len(lista)):
        dicio[f"{dado} {i+1}"] = lista[i][dado]
    return dicio

if __name__=="__main__":
    main()