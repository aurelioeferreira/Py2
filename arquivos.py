import os

if os.path.exists("fruteiras.txt"):
    os.remove("fruteiras.txt")
else:
    print("Arquivo não encontrado")