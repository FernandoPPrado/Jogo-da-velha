from Teste_win import Base_logica


class Funcao_botoes(Base_logica):
    def __init__(self):
        super().__init__()
        self.A1 = ''
        self.A2 = ''
        self.A3 = ''
        self.B1 = ''
        self.B2 = ''
        self.B3 = ''
        self.C1 = ''
        self.C2 = ''
        self.C3 = ''

    def preencherA1(self):
        self.botao_A1.config(
            text='X') if self.const % 2 == 0 else self.botao_A1.config(text='O')
        self.A1 = self.botao_A1['text']
        self.const += 1
        self.principal()

    def preencherA2(self):
        self.botao_A2.config(
            text='X') if self.const % 2 == 0 else self.botao_A2.config(text='O')
        self.A2 = self.botao_A2['text']
        self.const += 1
        self.principal()

    def preencherA3(self):
        self.botao_A3.config(
            text='X') if self.const % 2 == 0 else self.botao_A3.config(text='O')
        self.A3 = self.botao_A3['text']
        self.const += 1
        self.principal()

    def preencherB1(self):
        self.botao_B1.config(
            text='X') if self.const % 2 == 0 else self.botao_B1.config(text='O')
        self.B1 = self.botao_B1['text']
        self.const += 1
        self.principal()

    def preencherB2(self):
        self.botao_B2.config(
            text='X') if self.const % 2 == 0 else self.botao_B2.config(text='O')
        self.B2 = self.botao_B2['text']
        self.const += 1
        self.principal()

    def preencherB3(self):
        self.botao_B3.config(
            text='X') if self.const % 2 == 0 else self.botao_B3.config(text='O')
        self.B3 = self.botao_B3['text']
        self.const += 1
        self.principal()

    def preencherC1(self):
        self.botao_C1.config(
            text='X') if self.const % 2 == 0 else self.botao_C1.config(text='O')
        self.C1 = self.botao_C1['text']
        self.const += 1
        self.principal()

    def preencherC2(self):
        self.botao_C2.config(
            text='X') if self.const % 2 == 0 else self.botao_C2.config(text='O')
        self.C2 = self.botao_C2['text']
        self.const += 1
        self.principal()

    def preencherC3(self):
        self.botao_C3.config(
            text='X') if self.const % 2 == 0 else self.botao_C3.config(text='O')
        self.C3 = self.botao_C3['text']
        self.const += 1
        self.principal()
