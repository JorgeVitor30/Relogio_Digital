from tkinter import *
import tkinter
from datetime import datetime
from time import sleep



###### Cores usadas #######
cor1 = "#3d3d3d"  # preta
cor2 = "#fafcff"  # branca
cor3 = "#21c25c"  # verde
cor4 = "#eb463b"  # vermelha
cor5 = "#dedcdc"  # cinza
cor6 = "#3080f0"  # azul

fundo = cor1
cor = cor3


janela = Tk()
janela.title("") 
janela.geometry('500x180')
janela.resizable(width=FALSE, height=FALSE)
janela.configure(bg=fundo)

def relogio():
    tempo=datetime.now()
    
    hora = tempo.strftime('%H:%M:%S')
    dia_da_semana = tempo.strftime('%A')
    dia = tempo.day
    mes = tempo.strftime('%B')
    ano = tempo.year
    mes_int = tempo.strftime('%m')
    

    l1.config(text=hora)
    l1.after(1000, relogio)
    l2.config(text=dia_da_semana + ', ' + str(dia) + ' ' + mes + ' ' + str(ano))
    l3.config(text=f'{dia}/{mes_int}/{ano}')



l1 = Label(janela, text='', font=('Arial 80'), bg=fundo, fg = cor)
l1.grid(row=0, column=0, sticky=NW, padx=5)


l2 = Label(janela, text='', font=('Arial 15'), bg=fundo, fg = cor)
l2.grid(row=1, column=0, sticky=NW, padx=5)

l3 = Label(janela, text='', font = ('Times 14'), bg = fundo, fg = cor)
l3.grid(row=2, column=0, sticky=NW, padx=5, columnspan=100)


relogio()




janela.mainloop()



    





