import random

def jogar_forca():


    apresentacao() #chamando função de apresentação
    palavra_secreta = carregar_palavra()
    letras_acertadas = inicializa_letras(palavra_secreta) #definindo parametro de funçã palavra_secreta

    enforcou = False
    acertou = False
    erros = 0

    while(not enforcou and not acertou):

        chute = chute_pede()

        if(chute in palavra_secreta):
            marca_chute_correto(palavra_secreta, chute, letras_acertadas)
        else:
            erros += 1

        enforcou = erros == 6 # enforcou se torna true caso erros atinja  6
        acertou = "_" not in letras_acertadas # verificando se ainda possui espaço sem letras na lista

        print(letras_acertadas)
    if(acertou):
        print("voce ganhou")
    else:
        print("voce perdeu")

    print("fim de jogo")

def apresentacao():
    print("Bem vindo ao jogo de forca")

def carregar_palavra():
    arquivo = open("palavras.txt",
                       "r")  # abrindo arquivo no modo read, possuimos 3 formas, read r write w e a append(add no final)
    palavras = []

    for linha in arquivo:
        linha = linha.strip()  # formatando as linhas do arquivo para não ter espaço nas palavras e linhas
        palavras.append(linha)  # adicionando a plavra da linha solicitada na lista

    arquivo.close()  # fechando arquivo

    numero = random.randrange(0, len(palavras))  # escolhendo um local aleatorio dentro da lista
    palavra_secreta = palavras[numero].upper()  # atribuindo posição escolhida aleatoriamente da lista na variavel
    return palavra_secreta

def inicializa_letras(palavra):
    return ["_" for letra in palavra]  # adicionando "_" para cada letra dentro da palavra na lista
    """for letra in palavra_secreta: #realizando a mesma função porem fora da lista
        letras_acertadas.append("_")"""

def chute_pede():
    chute = input("Qual letra : ")
    chute = chute.strip().upper()  # strip formata o texto tirando os caracteres indesejados
    return chute

def marca_chute_correto(palavra_secreta, chute, letras_acertadas):
    index = 0;  # variavel para mostrar posição
    for letra in palavra_secreta:  # procurando local da letra na str
        if (chute.upper() == letra.upper()):  # comparando valor de str
            letras_acertadas[index] = letra  # pegando a letra e colocando conforme a  variavel letra indica
        index += 1  # incrementando a cada final do laço

if (__name__ == "__main__"):
    jogar_forca()