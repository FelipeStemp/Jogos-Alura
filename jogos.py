import adivinhacao
import forca

def escolher_jogo():
    print("Escolha o jogo")

    print("1 forca | 2 advinhação")
    jogo = int(input("digite o numero referente ao jogo que deseja : "))

    if(jogo == 1):
        print("jogando forca")
        forca.jogar_forca()
    elif(jogo == 2):
        print("jogando advinhação")
        adivinhacao.jogar_advinhacao()

if (__name__ == "__main__"): # função para realizar execução independente no console
    escolher_jogo()