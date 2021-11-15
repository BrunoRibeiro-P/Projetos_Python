import time

class caixa_água():

    def __init__(self, tamanho_caixa):

        self.tamanho_caixa = tamanho_caixa
        self.pulso = 0 #clock zero, pois o circuito está desligado
        self.circuito = False 
        self.litros_água = 0

    def iniciando(self, ligar):
        
        if ligar == 0:
            print('Circuito desligado...')
        if ligar == 1:
                self.pulso = 1 #se o pulso for igual a 1 liga o circuito
                print('Dando o pulso ao circuito...')
                print('Circuito não danificado, iniciando o circuito...')
                time.sleep(1)
                self.circuito = True #ligando o circuito
                self.pulso = 0 # Tirando o pulso
                print('Pulso tirado! Não necessita pressionar o botão. ')
        
    def processo(self):

        while self.circuito == True:
            self.litros_água += 1
            print(f'Passou um minuto, {self.litros_água} litros foi colocado. ')
            time.sleep(1)
            if self.litros_água == (self.tamanho_caixa - 2):
                print('Caixa quase lotada! Desligando o circuito...')
                time.sleep(1)
                print('Desligando...')
                time.sleep(1)
                self.circuito = False

def main():
    programa = True
    while programa == True:
        deseja_ligar = str(input('Deseja ligar o circuito? [S/N]: ')).upper()    
        if deseja_ligar == 'N':
            caixa = caixa_água(0)
            caixa.iniciando(0)
        elif deseja_ligar == 'S':
            caixa = caixa_água(int(input('Qual o tamanho da caixa de água? ')))
            caixa.iniciando(1)
            caixa.processo()
        desligar_programa = input('Deseja desligar o programa? [S/N]: ').upper()
        if desligar_programa == 'S':
            programa = False #desligando o programa        

if __name__ == "__main__":
    main()