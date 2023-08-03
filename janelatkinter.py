import tkinter as tk

janela = tk.Tk()
""" canvas = tk.Canvas()
canvas.create_rectangle(20, 20, 200, 200)
canvas.grid(column=2, row=1)
canvas.create_oval(30,45,180,180)
check = tk.Checkbutton()
check.grid(column=1, row=1)
campo_texto = tk.Entry()
campo_texto.grid(column=2, row=2) """
img = tk.PhotoImage()
img.configure(file="convite1.png", format="png", width="300", height="300")
menu = tk.Menu()

janela.mainloop()