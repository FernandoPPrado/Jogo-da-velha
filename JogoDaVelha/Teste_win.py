class Base_logica():
    def __init__(self):
        self.const = 0

    def principal(self):
        if self.const >= 5:
            self.ganhou()

    def novo_jogo(self):
        self.destravar_botoes()
        self.limpar_lista()
        self.const = 0

    def destravar_botoes(self):
        self.botao_A1.config(text='')
        self.botao_A2.config(text='')
        self.botao_A3.config(text='')
        self.botao_B1.config(text='')
        self.botao_B2.config(text='')
        self.botao_B3.config(text='')
        self.botao_C1.config(text='')
        self.botao_C2.config(text='')
        self.botao_C3.config(text='')

    def limpar_lista(self):
        self.A1 = ''
        self.A2 = ''
        self.A3 = ''
        self.B1 = ''
        self.B2 = ''
        self.B3 = ''
        self.C1 = ''
        self.C2 = ''
        self.C3 = ''

    def ganhou(self):
        if self.A1 == self.A2 == self.A3:
            if self.A1 == 'X':
                print('X Ganhou')
                self.novo_jogo()

            elif self.A1 == 'O':
                print('0 Ganhou')
                self.novo_jogo()

        elif self.B1 == self.B2 == self.B3:
            if self.B1 == 'X':
                print('X Ganhou')
                self.novo_jogo()
            elif self.B1 == 'O':
                print('0 Ganhou')
                self.novo_jogo()

        elif self.C1 == self.C2 == self.C3:
            if self.C1 == 'X':
                print('X Ganhou')
                self.novo_jogo()
            elif self.C1 == 'O':
                print('0 Ganhou')
                self.novo_jogo()

        elif self.A1 == self.B1 == self.C1:
            if self.A1 == 'X':
                print('X Ganhou')
                self.novo_jogo()
            elif self.A1 == 'O':
                print('0 Ganhou')
                self.novo_jogo()
        elif self.A2 == self.B2 == self.C2:
            if self.A2 == 'X':
                print('X Ganhou')
                self.novo_jogo()
            elif self.A2 == 'O':
                print('0 Ganhou')
                self.novo_jogo()

        elif self.A3 == self.B3 == self.C3:
            if self.A3 == 'X':
                print('X Ganhou')
                self.novo_jogo()
            elif self.A3 == 'O':
                print('0 Ganhou')
                self.novo_jogo()

        elif self.A1 == self.B2 == self.C3:
            if self.A1 == 'X':
                print('X Ganhou')
                self.novo_jogo()
            elif self.A1 == 'O':
                print('0 Ganhou')
                self.novo_jogo()

        elif self.A3 == self.B2 == self.C1:
            if self.C1 == 'X':
                print('X Ganhou')
                self.novo_jogo()
            elif self.C1 == 'O':
                print('0 Ganhou')
                self.novo_jogo()
        elif self.const == 9:
            print('Empate')
            self.novo_jogo()
