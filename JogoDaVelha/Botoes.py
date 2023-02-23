from tkinter import *
from Funções_botões import Funcao_botoes


class botoes(Funcao_botoes):
    def __init__(self):
        super().__init__()

    def botao_pai(self):
        return Button(self.frame1, text='',
                      bg='#252526', fg='red', font=(60), borderwidth=0)

    def botao1(self):
        # ---------------------------------------------------------
        # Coluna 1

        self.botao_A1 = self.botao_pai()
        self.botao_A1.place(x=0, y=0, height=93, width=93)
        # temp--------------------------------------------temp
        self.botao_A1.config(command=self.preencherA1)

        self.botao_B1 = self.botao_pai()
        self.botao_B1.place(x=0, y=103, height=93, width=93)
        # temp--------------------------------------------temp
        self.botao_B1.config(command=self.preencherB1)

        self.botao_C1 = self.botao_pai()
        self.botao_C1.place(x=0, y=206, height=93, width=93)
        # temp--------------------------------------------temp
        self.botao_C1.config(command=self.preencherC1)

        # ---------------------------------------------------------
        # Coluna 2
        self.botao_A2 = self.botao_pai()
        self.botao_A2.place(x=103, y=0, height=93, width=93)
        # temp--------------------------------------------temp
        self.botao_A2.config(command=self.preencherA2)

        self.botao_B2 = self.botao_pai()
        self.botao_B2.place(x=103, y=103, height=93, width=93)
        # temp--------------------------------------------temp
        self.botao_B2.config(command=self.preencherB2)

        self.botao_C2 = self.botao_pai()
        self.botao_C2.place(x=103, y=206, height=93, width=93)
        # temp--------------------------------------------temp
        self.botao_C2.config(command=self.preencherC2)
        # ---------------------------------------------------------

        # COLUNA 3

        self.botao_A3 = self.botao_pai()
        self.botao_A3.place(x=206, y=0, height=93, width=93)
        # temp--------------------------------------------temp
        self.botao_A3.config(command=self.preencherA3)

        self.botao_B3 = self.botao_pai()
        self.botao_B3.place(x=206, y=103, height=93, width=93)
        # temp--------------------------------------------temp
        self.botao_B3.config(command=self.preencherB3)

        self.botao_C3 = self.botao_pai()
        self.botao_C3.place(x=206, y=206, height=93, width=93)
        # temp--------------------------------------------temp
        self.botao_C3.config(command=self.preencherC3)
