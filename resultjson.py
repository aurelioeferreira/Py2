import json

with open("result.json", "r") as arq:
    conteudo_json = arq.read()

dicio_json = json.loads(conteudo_json)

print(dicio_json["eyeColor"])
print(dicio_json["age"])

dicio_json["eyeColor"] = "blue"
dicio_json["age"] = 28
json_alterado = json.dumps(dicio_json, indent=4)

with open("result.json", "w") as arq:
    arq.write(json_alterado)