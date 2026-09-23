import random
import time


def fase1_caca_tesouro():
    print("\nFase 1 — Caça ao Tesouro")
    moedas = 0

    for escavar in range(1, 6):
        moedas_encontradas = random.randint(5, 20)
        moedas = moedas + moedas_encontradas
        print(
            f"Escavação {escavar}: você encontrou {moedas_encontradas} moedas de ouro!"
        )
        time.sleep(0.3)

    print(f"\nTotal encontrado: {moedas} moedas de ouro")
    return moedas


def fase2_kraken(moedas):
    print("\nFASE 2: KRAKEN")
    kraken_hp = 100
    navio_hp = 60
    turno = 1

    bonus_canhao = moedas // 10

    print(f"O kraken emergiu das profundezas! com {kraken_hp} pontos de vida!")
    print(f"Seu bônus de canhão é de {bonus_canhao}\n")

    while kraken_hp > 0 and navio_hp > 0:
        print(f"\nTurno {turno}")

        # ataque navio
        dano_navio = random.randint(8, 15) + bonus_canhao
        kraken_hp = kraken_hp - dano_navio
        kraken_hp = max(kraken_hp, 0)
        print(f"Seus canhões dispararam causando {dano_navio} de dano!")
        print(f"HP do Kraken: {kraken_hp}")

        if kraken_hp == 0:
            print("\nO Kraken foi derrotado!")
            break

        # Ataque do kraken
        dano_kraken = random.randint(5, 12)
        navio_hp = navio_hp - dano_kraken
        navio_hp = max(navio_hp, 0)
        print(f"O Kraken golpeia causando {dano_kraken} de dano ao seu navio")
        print(f"HP atual do seu navio: {navio_hp}")

        turno = turno + 1
        time.sleep(0.3)

    return navio_hp > 0


def fase3_reiniciar_viagem():
    while True:
        print("\nINÍCIO DA VIAGEM")

        moedas = fase1_caca_tesouro()
        vitoria = fase2_kraken(moedas)

        print("\nFIM DA VIAGEM")
        if vitoria:
            print("Parabéns! Você derrotou o Kraken e garantiu seu tesouro!")
            break
        else:
            print("Seu navio foi destruído pelo Kraken. Tente novamente!")

        resposta = input("Deseja reiniciar a viagem? (s/n)\n").strip().lower()
        if resposta != 's':
            print("Obrigado por jogar! Até a próxima!")
            break


if __name__ == "__main__":
    fase3_reiniciar_viagem()