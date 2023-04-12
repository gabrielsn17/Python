import tkinter as tk
from  tkinter import *
from tkinter import ttk

# --- functions ---

def generate():
    try:
        resultado = float(peso.get()) / (float(altura.get())**2)
    except Exception as ex:
        print(ex)
        resultado = 'error'

    num3.set('%.2f'%resultado)

# --- main ---

janela = tk.Tk()
janela.title('Calculadora de Peso Ideal')
janela.geometry('800x500')

peso = tk.StringVar()
altura = tk.StringVar()
num3 = tk.StringVar()

tk.Label(janela, text=' O índice de massa corporal é uma medida internacional usada para calcular se uma pessoa está no peso ideal.').grid(column=0, row=0)
tk.Label(janela, text= ' O IMC é calculado dividindo o peso (em kg) pela altura ao quadrado (em m), de acordo com a seguinte fórmula: IMC = peso / (altura x altura).').grid(column=0, row=1)
tk.Label(janela, text=' Abaixo, irei calcular seu IMC e classifica-lo de acordo com a OMS(Organização Mundial da Saúde)').grid(column=0, row=2)

tk.Label(janela, text="Por favor, informe seu peso em quilos. Ex: 70").grid(row=3, column=0)
tk.Label(janela, text="Por favor, informe sua altura em metros. Ex: 1.70").grid(row=5, column=0)
tk.Label(janela, text="Seu IMC é:").grid(row=8, column=0)
tk.Entry(janela, textvariable=peso).grid(row=4, column=0)
tk.Entry(janela, textvariable=altura).grid(row=6, column=0)
tk.Entry(janela, textvariable=num3).grid(row=9, column=0)

button = tk.Button(janela, text="Calcular IMC", command=generate)
button.grid(row=7, column=0)

tk.Label(janela, text='').grid(row=10, column=0)

game_frame = Frame(janela)
game_frame.grid(row=11, column=0)

my_game = ttk.Treeview(game_frame)

my_game['columns'] = ('IMC', 'Classificação')

my_game.column("#0", width=0,  stretch=NO)
my_game.column("IMC",anchor=CENTER, width=200)
my_game.column("Classificação",anchor=CENTER,width=200)

my_game.heading("#0",text="",anchor=CENTER)
my_game.heading("IMC",text="IMC",anchor=CENTER)
my_game.heading("Classificação",text="Classificação",anchor=CENTER)

my_game.insert(parent='',index='end',iid=0,text='',
values=('Menor que 18.5' ,' Abaixo do peso normal'))
my_game.insert(parent='',index='end',iid=1,text='',
values=('18.5 - 24.9 ',' Peso normal'))
my_game.insert(parent='',index='end',iid=2,text='',
values=('25.0 - 29.9 ',' Excesso de peso'))
my_game.insert(parent='',index='end',iid=3,text='',
values=('30.0 - 34.9 ',' Obesidade classe 1'))
my_game.insert(parent='',index='end',iid=4,text='',
values=('35.0 - 39.9 ',' Obesidade classe 2'))
my_game.insert(parent='',index='end',iid=5,text='',
values=('Maior ou igual a 40 ',' Obesidade classe 3'))

my_game.grid(row=11, column=0)

janela.mainloop()