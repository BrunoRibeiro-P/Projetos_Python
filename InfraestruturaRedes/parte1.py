class InicialDoPrograma:
    def __init__(self):
        self.ip = None
    
    def conectar_ip(self):
        self.ip = int(input('Qual enderesso de IP deseja conectar?'))



class InfraestruturaDeRedes(InicialDoPrograma):

    
    def __init__(self):

        self.password = None
        self.laptops = ['PC1','PC2','PC3','PC4','PC5']

    def Login(self):
            
        while True:
            for contador in range(4):
                self.conectar = input(f'Deseja-se conectar ao {self.laptops[contador]} [S/N]:').upper()
                if self.conectar == 'S':
                    self.password = input('Digite a senha: ')
                    if self.password != 'Testando':
                        while self.password != 'Testando':
                            print('Senha incorreta, digite novamente ')
                            self.password = input('Digite a senha: ')
                    else:
                        print(f'Computador {self.laptops[contador]} Logado. ')
                self.continuar = input('Deseja conectar a mais um computador [S/N]: ').upper()
                if self.continuar == 'N':
                    break
            break
        
InfraestruturaDeRedes().Login()
