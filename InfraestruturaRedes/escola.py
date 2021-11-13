from time import sleep
print("CISC (Complex Instruction Set Computer) ")
pc = int(input("Qual computador deseja usar o [1 ,2 ,3 ,4, 5]: "))
byte = int(input("Quantidade de bytes o qual deseja enviar: "))

for c in range(11):
    if c != 0:
        sleep(2)
        print('Analisando a informação ...')
        sleep(2)
        print('Analisando o repositório...')
        sleep(2)
        print('Enviando a informação ...')
        sleep(2)
        print(f'{c*10}% da informação enviada')
        if c == 10:
            print(f'Todos os {byte} bytes enviados com sucesso!')
