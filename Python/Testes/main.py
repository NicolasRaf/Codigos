import os

class Carro:
   
    def __init__(self, cor, modelo, ano):
        self.__cor = cor
        self.__modelo = modelo
        self.__ano = ano
        self.__ligado = False

    def ligar(self):
        if not self.__ligado:
            self.__ligado = True
            print("Carro ligado.")
        else:
            print("O carro já está ligado.")

    def desligar(self):
        if self.__ligado:
            self.__ligado = False
            print("Carro desligado.")
        else:
            print("O carro já está desligado.")

    def acelerar(self):
        if self.__ligado:
            print("Carro acelerando.")
        else:
            print("Você precisa ligar o carro primeiro.")

    def frear(self):
        print("Carro freando.")

# Criação de instâncias de carros
meu_carro = Carro(cor="azul", modelo="sedan", ano=2022)
print(meu_carro)
outro_carro = Carro(cor="vermelho", modelo="jeep", ano=2020)

# Solicitação do usuário para escolher um carro
carro_escolhido = input("Escolha um carro ('meu' ou 'outro'): ")

# Verifica qual carro o usuário escolheu
if carro_escolhido == 'meu':
    carro = meu_carro
elif carro_escolhido == 'outro':
    carro = outro_carro
else:
    print("Carro não reconhecido.")
    exit()

# Solicitação do usuário para escolher uma ação
acao = input("Escolha uma ação ('ligar', 'desligar', 'acelerar' ou 'frear'): ")

# Verifica qual ação o usuário escolheu e executa

def funcionamento(acao):

    if acao == 'ligar':
        carro.ligar()
    elif acao == 'desligar':
        carro.desligar()
    elif acao == 'acelerar':
        carro.acelerar()
    elif acao == 'frear':
        carro.frear()
    else:
        print("Ação não reconhecida.")

    continuar = int(input("\nDeseja continuar?(1-sim/2-não) "))

    if(continuar == 1):
       acao = input("Escolha uma ação ('ligar', 'desligar', 'acelerar' ou 'frear'): ")
       return funcionamento(acao)
    else:
        return  os.system('cls' if os.name == 'nt' else 'clear')

funcionamento(acao)
