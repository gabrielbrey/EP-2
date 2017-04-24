with open("inspermons.json") as arquivo:
    inspermons = json.load(arquivo)
print("Bem vindo ao misterioso mundo de inspermon ")

começo = input("Digite 'passear' para começar o inspermon : ")
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
    else:
        print("digite um inspermon valido")
        
    inspermon_jogador = inspermons[escolha]
    insperdex.append(inspermon_jogador)
    print ("Inspermon : {0} , Vida: {1} , Poder Minimo :{2}, Poder maximo {3} , Defesa {4}".format(inspermon_jogador["nome"],inspermon_jogador["vida"],inspermon_jogador["poder minimo"],inspermon_jogador["poder maximo"],inspermon_jogador["defesa"]))

else:
    print("comando invalido")