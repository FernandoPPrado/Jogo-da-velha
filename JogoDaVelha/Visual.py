from Botoes import botoes
from tkinter import *
janela = Tk()


class Visual(botoes):
    def __init__(self):
        super().__init__()
        self.janela = janela
        self.janela_prop()
        self.frame_1()
        self.botao1()
        # self.texte_bot()
        janela.mainloop()

    def janela_prop(self):
        self.janela.geometry('400x400+200+200')
        self.janela.config(bg='#252526')
        self.janela.resizable(False, False)
        self.janela.title('Jogo da Velha')

    def frame_1(self):
        self.frame1 = Frame(self.janela)
        self.frame1.config(bg='#3e3e42')
        self.frame1.place(x=50, y=50, width=299, height=299)


Visual()
