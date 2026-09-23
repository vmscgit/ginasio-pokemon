import random

pontos_treino = 0

print("Bem-vindo ao Ginasio Pokemon!")
print("Fase 1: Treino do seu Pokemon")

for dia in range(1, 6):
    pontos = random.randint(5, 15)
    pontos_treino = pontos_treino + pontos
    print("Dia", dia, "de treino. Voce ganhou", pontos, "pontos.")

bonus_dano = pontos_treino // 20
print("Total de pontos de treino:", pontos_treino)
print("Bonus de dano: +", bonus_dano)

hp_jogador = 100
hp_lider = 100

print("A batalha contra o Lider comecou!")

turno = 1

while hp_jogador > 0 and hp_lider > 0:
    print("--- Turno", turno, "---")

    dano_jogador = random.randint(8, 15) + bonus_dano
    hp_lider = hp_lider - dano_jogador
    print("Seu Pokemon causou", dano_jogador, "de dano. HP do Lider:", hp_lider)

    if hp_lider > 0:
        dano_lider = random.randint(5, 12)
        hp_jogador = hp_jogador - dano_lider
        print("O Lider causou", dano_lider, "de dano. Seu HP:", hp_jogador)

    if hp_jogador < 30 and hp_jogador > 0:
        print("Cuidado! Seu HP esta baixo!")
    elif hp_jogador <= 0:
        print("Seu Pokemon esta prestes a desmaiar!")
    else:
        print("A batalha continua.")

    turno = turno + 1

if hp_lider <= 0:
    print("Voce venceu o Lider de Ginasio!")
elif hp_jogador <= 0:
    print("Seu Pokemon foi derrotado. Tente novamente!")
else:
    print("Empate!")