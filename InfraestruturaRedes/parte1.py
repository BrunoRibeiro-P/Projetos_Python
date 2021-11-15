class InicialDoPrograma:
    
    def __init__(self, laptops, hostswitchs, hostrs, servers):

        self.laptops = laptops
        self.hostswitchs = hostswitchs
        self.hostrs = hostrs
        self.servers = servers
        self.nome_laptops_armazenar = list()
        self.local_laptops_armazenar = list()
        self.passwordw = list()

    def nomes_locais_laptops(self):

        for inteiro in range(self.laptops):
            nome = input(f'Digite o nome do laptop {inteiro+1}: ')
            local = input(f'Digite o local do laptop {nome}: ')
            self.nome_laptops_armazenar.append(nome)
            self.local_laptops_armazenar.append(local)
            self.armazenar_laptops = {k: v for k, v in zip(self.nome_laptops_armazenar, self.local_laptops_armazenar)}
            print(self.armazenar_laptops)

    def login_laptops(self, conectar_laptop):
        pass

ligar = input('Deseja ligar o programa? [S/N]: ').upper()
if ligar == 'S':
    acrescentar = input('Deseja acrecentar algo? [S/N]: ').upper()
    if acrescentar == 'S':
        laptop = int(input('Digite o número de laptops que deseja conectar: '))
        hosts_switch = int(input('Digite o número de switch que deseja conectar: '))
        r = int(input('Digite o número de host R que deseja conectar: '))
        server = int(input('Digite o número de servers que deseja conectar: '))
        início = InicialDoPrograma(laptop, hosts_switch, r, server)
        início.nomes_locais_laptops()
    else:
        conectar_laptop = int(input('Digite qual laptop deseja contectar'))
        print('continua...')






