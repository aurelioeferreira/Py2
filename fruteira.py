import os

class Fruteira():
    def __init__(self, lista: list[str]):
        self.frutas_lista = lista #["banana", "maçã", "abacaxi", "caqui", "laranja", "jaca", "mirtilo", "nona", "melancia", "melao"]
        self.QUANTIDADE_MAXIMA = 12

    def frutas(self): # transforma a lista de frutas numa string
        if len(self.frutas_lista) > 0:
            frutas = self.frutas_lista[0]
            for fruta in self.frutas_lista[1:]:
                frutas = frutas + ", " + fruta
            return frutas
        else:            
            return None
        
    def esta_cheia(self):
        quant = self.quantidade_frutas()
        if quant == self.QUANTIDADE_MAXIMA:
            return True
        else:
            return False

    def esta_vazia(self):
        if self.quantidade_frutas() == 0:
            return True
        else:
            return False
        
    def funcao():
        print("")

    def escolhe_fruta(self):
        print(f"\nQual fruta você deseja comer? Na fruteira tem: {self.frutas()}")
        fruta = input("Digite o nome da fruta(ou 1 para desistir de comer): ")
        return fruta

    def valida_fruta(self, fruta):
        for f in self.frutas_lista:
            if fruta == f:
                return True
        return False

    def retira_fruta(self, fruta):
        indice = 0
        for f in self.frutas_lista:
            if fruta == f:
                self.frutas_lista.pop(indice)
                break
            indice = indice+1

    def adiciona_fruta(self, fruta):

        self.frutas_lista.append(fruta)
    
    def quantidade_frutas(self):
        return len(self.frutas_lista)
    
    def joga_fora(self):
        self.frutas_lista = []


def menu_inicial(fruteira: Fruteira):
    disponibilidade_opcao_comer_fruta = ""
    disponibilidade_opcao_adicionar_fruta = ""
    disponibilidade_jogar_frutas_fora = ""
    fruta = "frutas" if fruteira.quantidade_frutas() > 1 else "fruta"
    if fruteira.quantidade_frutas() > 0:
        print(f"\nVocê tem {fruteira.quantidade_frutas()} {fruta} na fruteira: {fruteira.frutas()}")        
    else:
        disponibilidade_opcao_comer_fruta = "(indisponível)"
        disponibilidade_jogar_frutas_fora = "(indisponível)"
        print("\nA fruteira está vazia")
    if fruteira.quantidade_frutas() >= 12:
        disponibilidade_opcao_adicionar_fruta = "(indisponível)"
    

    print("\nO que você pretende fazer?")
    print(f"1 - Comer uma fruta {disponibilidade_opcao_comer_fruta}")
    print(f"2 - Colocar nova fruta na fruteira {disponibilidade_opcao_adicionar_fruta}")
    print(f"3 - Jogar todas as frutas fora {disponibilidade_jogar_frutas_fora}")
    print("4 - Sair do programa")

def valida_escolha(escolha):        
    if escolha != "1" and escolha != "2" and escolha != "3" and escolha != "4":
        return False
    else:
        return True

def le_arquivo(nome):
    with open(nome, mode="r", encoding="utf-8") as arquivo:
        texto = arquivo.readline().replace(" ","").split(",")
        if texto != ["None"]:
            return texto
        else:
            return []
        
def confirma_escolha(nome_escolha):
    while True:
        escolha = (input(f"Tem certeza que deseja {nome_escolha}? (s/n): ")).lower()
        if escolha == "s" or escolha == "n":
            if escolha == "s":
                return True
            else:
                return False
        else:
            print("Opção inválida. Digite s ou n.\n")
     
    

def main():
    #início do programa   
    nome_arquivo = "fruteiras.txt" 
    if os.path.exists(nome_arquivo):
        fruteira = Fruteira(le_arquivo(nome_arquivo))
    else:
        fruteira = Fruteira([])
    while True:
        menu_inicial(fruteira)
        escolha = input("Sua escolha: ")
        if(valida_escolha(escolha)):
            if escolha == "1":
                if fruteira.esta_vazia():
                    print("\nOpção indisponível no momento por não haver nenhuma fruta na fruteira")
                    
                    continue
                while True:
                    fruta = fruteira.escolhe_fruta().lower()
                    if fruta == "1":
                        print("\nDesistiu de comer - Retornando ao menu inicial...")
                        
                        break
                    if fruteira.valida_fruta(fruta):
                        fruteira.retira_fruta(fruta)
                        print(f"\nA fruta {fruta} foi comida com sucesso! - Retornando ao menu inicial...")
                        
                        break
                    else:
                        print(f"\n{fruta} não está presente na sua fruteira")
                        print("Por favor, escolha uma fruta válida, ou digite 1 para desistir de comer uma fruta")
            elif escolha == "2":
               if fruteira.esta_cheia():
                    print(f"\nOpção indisponível no momento porque a fruteira está cheia (máximo de {fruteira.QUANTIDADE_MAXIMA} frutas)")
                    
                    continue
               fruta = str(input("\nDigite o nome da fruta que você deseja adicionar(ou 1 para desistir): ")).lower()
               if fruta == "1":
                   
                   continue
               fruteira.adiciona_fruta(fruta)
               print(f"\nVc adicionou a fruta {fruta} - Retornando ao menu inicial...")
               
            elif escolha == "3":
                if fruteira.esta_vazia():
                    print("\nOpção indisponível no momento por não haver nenhuma fruta na fruteira")
                    
                    continue
                if confirma_escolha("jogar todas as frutas fora"):
                    fruteira.joga_fora()
                    print("\nVocê jogou todas as frutas fora...")
                    
                else:
                    print("\nDesistiu de jogar as frutas fora - Retornando ao menu inicial...")
                    
                    continue
            elif escolha == "4":
                print("Programa finalizado...")
                break
        else:
            print(f"\n{escolha} não é uma escolha válida")
            print("Escolha entre 1, 2, 3 e 4")
            

    
    arquivo_texto = open("fruteiras.txt", "w", 1, "utf-8")
    texto = f"{fruteira.frutas()}"
    arquivo_texto.write(texto)
    arquivo_texto.close()

if __name__=="__main__":
    main()