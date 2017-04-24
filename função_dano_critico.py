import random

x=80
y=60
v=80
def dano_critico(x):
    critico = random.randint(0, 100)
    if critico in range(0, x):
        return True
    else:
        return False
def dano_critic(v):
    critico = random.randint(0, 100)
    if critico in range(0, v):
        return True
    else:
        return False
    