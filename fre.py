import cowsay
import tkinter

def main():
    tk = tkinter.Tk()
    tk.title("Programa do Aure")
    tk.geometry("400x400")
    text = tkinter.Label(tk, text="Bom dia! Clique no botão para fechar")
    text.grid(column=3, row=3, padx=20, pady=30)
    click = tkinter.Label(tk, text="")
    click.grid(column=3, row=5, padx=20, pady=30)    
    botao = tkinter.Button(tk, text="Fechar", command=lambda: pegar(click))
    botao.grid(column=3, row=4, padx=20, pady=0)
    tk.mainloop()
    print("vamos")

def pegar(click:tkinter.Label()):
    click.config(text="vai")
    return "clicou"



bom_dia = "Bom dia, humano!"
cowsay.ghostbusters(bom_dia)

if __name__ == "__main__":
    main()