import random

complete_bet = []
count = 0

def aposta():
    for i in range(0, 4):
        bet = int(input(f"Digite o {i+1}° número da sua aposta: "))
        complete_bet.append(bet)
    complete_bet.sort()
    return complete_bet


def resultado():
    result = [random.randint(1, 60) for i in range(4)]
    result.sort()
    return result


ap = aposta()
res = resultado()


while ap != res:
    res = resultado()
    count += 1
    print(f"Aposta n°: {count}")
    print(f"Resultado: {res}")

print("-"*45)
print(f"Seu jogo: {ap}\n"
          f"Resultado: {res}\n"
          f"Você teve que jogar {count} vezes para finalmente ganhar na Mega Sena!")
