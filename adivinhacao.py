import random

def jogar_advinhacao():

    print("Bem vindo ao jogo de adivinhação")

    # numero_secreto = round(random.random() * 100) # criando numero aleatorio e arredondando ele com round
    numero_secreto = random.randrange(0, 101) # definindo range de numero random
    print(numero_secreto)
    total_de_tentativas = 0
    pontos = 1000
    rod = 1

    print("1 facil | 2 normal | 3 dificil")
    nivel = int(input("Digite o numero referente a dificuldade escolhida : "))

    if(nivel == 1):
        total_de_tentativas = 20
    elif(nivel == 2):
        total_de_tentativas = 15
    else:
        total_de_tentativas = 10

    print("total de tentativas", total_de_tentativas)

    """
    # Laço while
    
    while(rod <= total_de_tentativas):
        print("Tentativa {} de {}".format(rod, total_de_tentativas))  # usado para adicionar variaveis em texto
    
        chute = input("Digite um numero entre 1 e 100 : ")  # input sempre colhe como STR
        chute = int(chute)  # transformando em int
    
        if(chute < 1 or chute > 100):
            print("Você deve digitar um numero entre 1 e 100")
            continue
    
        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto
    
        if (acertou):
            print("Você acertou e fez {} pontos".format(pontos))
            break
        else:
            if (maior):
                print("Seu chute foi maior")
            elif (menor):
                print("seu chute foi menor")
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos
        rod = rod + 1
    """
        # laço for

    for rod in range(1, total_de_tentativas + 1):
        print("Tentativa {} de {}".format(rod, total_de_tentativas))  # usado para adicionar variaveis em texto

        chute = input("Digite um numero entre 1 e 100 : ")  # input sempre colhe como STR
        chute = int(chute)  # transformando em int

        if(chute < 1 or chute > 100):
            print("Você deve digitar um numero entre 1 e 100")
            continue

        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if (acertou):
            print("Você acertou e fez {} pontos".format(pontos))
            break
        else:
            if (maior):
                print("Seu chute foi maior")
            elif (menor):
                print("seu chute foi menor")
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos

    print("fim de jogo")

if(__name__ == "__main__"):
    jogar_advinhacao()