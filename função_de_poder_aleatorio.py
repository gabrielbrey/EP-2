
def poder_jogador(jogador):
    dano_minimo_jogador = jogador["poder minimo"]
    dano_maximo_jogador = jogador["poder maximo"]
    poder_jogador = random.randint(dano_minimo_jogador,dano_maximo_jogador)
    return poder_jogador

def poder_adversario(adversario):
    dano_minimo_adversario = adversario["poder minimo"]
    dano_maximo_adversario = adversario["poder maximo"]
    poder_adversario = random.randint(dano_minimo_adversario,dano_maximo_adversario)
    return poder_adversario