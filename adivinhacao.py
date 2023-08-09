import random

def jogar():

    print("*********************************")
    print("Bem vindo ao jogo de Adivinhação!")
    print("*********************************")

    numero_secreto = random.randrange(1, 101)
    print(numero_secreto)
    total_tentativas = 0
    pontos = 1000

    print("qual nível de dificuldade?")
    print("(1)- Baixo (2)- Médio  (3)- Alto")
    nivel = int(input("Defina o nível de dificuldade: "))

    if (nivel ==1):
        total_tentativas = 20
    elif (nivel ==2):
        total_tentativas = 10
    else:
        total_tentativas = 5

    # while  (rodada <= total_tentativas):
    for rodada in range (1, total_tentativas +1):
        print("tentativa {} de {}".format(rodada,total_tentativas))
        chute_str = input("Digite um número entre 1 e 100:")
        print("Você digitou:", chute_str)
        chute = int(chute_str)
        if (chute < 1 or chute > 100):
            print("digite entre 1 e 100")
            continue


        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if (acertou):
            print("Acertou e fez {}!". format(pontos))
            break
        else:
            if (maior):
                print("numero maior")
            elif (menor):
                print("numero menor")
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos


        # rodada = rodada + 1

if(__name__ == "__main__"):
    jogar()
