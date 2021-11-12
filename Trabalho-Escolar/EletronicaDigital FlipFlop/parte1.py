import time

class caixa_água():

    def __init__(self):

        self.estado_de_clock = False
        self.circuito = False 
        self.litros_água = 0
        self.tamanho_caixa = 50
        self.pulso = 0
        self.contador_de_litros = 0

    def ligando(self):

        while self.estado_de_clock == True:
            print('Clock desligado...')
            self.pulso = str(input('Deseja ligar o circuito? [S/N]: ')).upper()
            if self.pulso == 'S':
                self.pulso = 1
                self.estado_de_clock = True
                print('Clock Ligado...')
                print('Circuito não danificado, iniciando o circuito...')
                time.sleep(1)
                self.circuito = True
                print('Clock tirado...')
                self.estado_de_clock = False
                break #acho que não precisava disso, mas tá bugado

    def processo(self):

        self.circuito = True #Tenho que declarar isso
        while self.circuito == True:
            self.contador_de_litros += 1
            self.litros_água += 1
            print(f'Passou um minuto, {self.contador_de_litros} litros foi colocado. ')
            time.sleep(1)
            if self.litros_água == (self.tamanho_caixa - 2):
                print('Caixa quase lotada! Desligando o circuito...')
                time.sleep(1)
                self.circuito == False
                print('Desligando...')
                break #acho que não precisava disso, mas tá bugado
    
caixa_água().ligando()
caixa_água().processo()
