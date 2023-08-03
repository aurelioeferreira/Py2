import pyttsx3

eng = pyttsx3.init()
nome = input("Qual o seu nome? ")
texto = f"Bom te conhecer, {nome}!"
eng.say(texto)
print(texto)
eng.runAndWait()
print("oi, tudo bem")