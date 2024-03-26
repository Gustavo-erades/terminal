import tkinter as tk
from tkinter import *
import os
janela = tk.Tk()
janela.title("Terminal Python")
largura=800
altura=500
largura_screen=janela.winfo_screenwidth()
altura_screen=janela.winfo_screenheight()
posx=(largura_screen/2)-(largura/2)
posy=(altura_screen/2)-(altura/2)
janela.geometry("%dx%d+%d+%d"%(largura, altura, posx, posy))
janela.resizable(True, True)
janela.configure(background="#0D0D0D")
texto=">> your are from into path: %s"%(os.path.dirname(__file__))
label = Label (janela, text= ">> Hello user! Welcome to your new python terminal develpment by Gustavo Êrades", font = ("verdana", 10),fg='#04BF55', bg='#0D0D0D')
label.grid (column = 0, row = 0)
label = Label (janela, text= texto, font = ("verdana", 10),fg='#04BF55', bg='#0D0D0D')
label.grid (column = 0, row = 1)
codigo = Entry(janela, width=100, bg="#0D0D0D", fg="#fff", borderwidth=0, insertbackground="#fff")
codigo.grid(column=0, row=2)
'''codigo.configure(bg="#1C6C0B", insertbackground='white')'''
tk.mainloop()