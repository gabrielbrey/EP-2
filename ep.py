                      # -- coding: utf-8 --
"""
Created on Mon Apr 24 19:19:32 2017

@author: Leonardo
"""

import random
import json
x=10
y=60
v=10
lista_fuga = [1,2,3,4,5,6,7,8,9,10]

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
    

    

'''def poder_jogador(jogador):
    dano_minimo_jogador = jogador["poder minimo"]
    dano_maximo_jogador = jogador["poder maximo"]
    poder_jogador = random.randint(dano_minimo_jogador,dano_maximo_jogador)
    return poder_jogador

def poder_adversario(adversario):
    dano_minimo_adversario = adversario["poder minimo"]
    dano_maximo_adversario = adversario["poder maximo"]
    poder_adversario = random.randint(dano_minimo_adversario,dano_maximo_adversario)
    return poder_adversario'''
    
def batalha(jogador, adversario):
    vida_jogador = jogador["vida"]
    vida_adversario = adversario["vida"]
    dano_jogador = jogador["poder maximo"] - adversario["defesa"]
    if dano_jogador < 0:
        dano_jogador=0
    dano_adversario = adversario["poder maximo"] - jogador["defesa"]
    if dano_adversario < 0:
        dano_adversario = 0
    while vida_jogador > 0 and vida_adversario > 0:
        atacar_fugir = input("Para atacar o inspermon selvagem aperte 'Enter' , ou para tentar fugir dessa batalha digite 'fugir' :  ")
        if atacar_fugir == "fugir" :
            fuga = random.choice(lista_fuga)
            if fuga > 2:
                print("Você conseguiu escapar desse inspermon selvagem!")
                break
            else:
                print("Ixi , hoje não é o seu dia de sorte :( ")
        else :
            if dano_critico(x) == True:
                vida_adversario = vida_adversario - dano_jogador * 1.5
                if vida_adversario < 1:
                    vida_adversario = 0
                    print("você ganhou!")
                    return "xp"
    
                print("Ataque critico de {0} no {1} ".format(dano_jogador*1.5,adversario["nome"]))
                print("A vida do {0} é {1}".format(adversario["nome"],vida_adversario))
                
            else:
                vida_adversario = vida_adversario - dano_jogador
                print("{0} sofreu {1} de dano ".format(adversario["nome"],dano_jogador))
                
                if vida_adversario < 1:
                    vida_adversario = 0
                print("a vida do {0} é de {1}".format(adversario["nome"],vida_adversario))
                if vida_adversario < 0:
                    print("voce ganhou o jogo e recebeu xp")
                    return "xp"
            if dano_critic(v) == True:
                vida_jogador = vida_jogador - dano_adversario * 1.5
                print("Ataque critico de {0} no {1} ".format(dano_adversario*1.5,jogador["nome"]))

            else:
                vida_jogador = vida_jogador - dano_adversario
                print("{0} sofreu {1} de dano ".format(jogador["nome"],dano_adversario))
                if vida_jogador <1:
                    vida_jogador = 0
                print(" A sua vida é {0} é de {1}".format(jogador["nome"],vida_jogador))    
                if vida_jogador < 1:
                    print("ixi , o seu inspermon é muito fraco e precisa de treino")
                    return "fim"   
        
  
with open("inspermons.json") as arquivo:
    inspermons = json.load(arquivo)
print("Bem vindo ao misterioso mundo de inspermon ")

começo = input("Digite 'passear' para começar o inspermon: ")

if começo == "passear":
    print("escolha o seu inspermon")
    insperdex=[]
    for ipmon in inspermons :
        print ("Inspermon : {0} , Vida: {1} , Poder Minimo :{2}, Poder maximo {3} , Defesa {4}".format(ipmon["nome"],ipmon["vida"],ipmon["poder minimo"],ipmon["poder maximo"],ipmon["defesa"]))
    escolha = input("Qual é o inspermon escolhido ?: ").lower()
    if escolha == "crackmon":
        escolha = 0
    elif escolha == "chuitionmon" :
        escolha = 1
    elif escolha == "raposamon" :
        escolha = 2    
    elif escolha == "sujomon" :
        escolha = 3  
    elif escolha == "fabliiit" :
        escolha = 4 
    elif escolha == "ligeiromon" :
        escolha = 5
    elif escolha == "pufmon" :
        escolha = 6
    elif escolha == "breyzinha" :
        escolha = 7
    elif escolha == "ratatatatatatata" :
        escolha = 8
    elif escolha == "natitubemon" :
        escolha = 9
   
    inspermon_jogador = inspermons[escolha]
    insperdex.append(inspermon_jogador)
    print ("Inspermon : {0} , Vida: {1} , Poder Minimo :{2}, Poder maximo {3} , Defesa {4}".format(inspermon_jogador["nome"],inspermon_jogador["vida"],inspermon_jogador["poder minimo"],inspermon_jogador["poder maximo"],inspermon_jogador["defesa"]))
else:
    print("comando invalido")

while True:
    funsao = input("você quer 'dormir' , 'hunt '  ou 'insperdex' : ")
    if funsao == "dormir":
        break
    
    elif funsao == "insperdex":
        print("o seu Inspermon : {0} , Vida: {1} , Poder Minimo :{2}, Poder maximo {3} , Defesa {4} ".format(inspermon_jogador["nome"],inspermon_jogador["vida"],inspermon_jogador["poder minimo"],inspermon_jogador["poder maximo"],inspermon_jogador["defesa"]))
        
        print("INSPERDÉX")
        for ipmon in insperdex :
            print ("Inspermon : {0} , Vida: {1} , Poder Minimo :{2}, Poder maximo {3} , Defesa {4}".format(ipmon["nome"],ipmon["vida"],ipmon["poder minimo"],ipmon["poder maximo"],ipmon["defesa"]))

    elif funsao == "hunt":
        inspermon_adversario = random.choice(inspermons)
        if inspermon_adversario not in insperdex:
            insperdex.append(inspermon_adversario)
        print ("Inspermon : {0} , Vida: {1} , Poder Minimo :{2}, Poder maximo {3} , Defesa {4}".format(inspermon_adversario["nome"],inspermon_adversario["vida"],inspermon_adversario["poder minimo"],inspermon_adversario["poder maximo"],inspermon_adversario["defesa"]))
        resultado_batalha = batalha(inspermon_jogador,inspermon_adversario)
        if resultado_batalha == "fim":
            print("jogo acabou , o seu inspermon era muito fraco e acabou morrendo ")
            break
        elif resultado_batalha == "xp":
            print("Voce derrotou o inspermon selvagem e ganhou xp")
    else:
        print ("digite algum comando valido ")