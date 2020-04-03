##Jogo Craps 

#Importar Biblioteca
import random 

#Dinheiro Inicial do jogador
player_money = 100

#Introdução ao jogo
print('Bem vindo(a) ao CRAPS INSPER!')

Point = False
fase = 'Comeout' 

#Função While que roda o jogo enquanto o jogador possui dinheiro para apostar
while player_money > 0:
    if fase == 'Comeout':
        game = input('\nIniciar o jogo (sim/não) ')
    if game == 'sim':
        #Mostra ao jogador a quantia inicial de dinheiro
        print('Seu dinheiro total é: {}'.format(player_money))
        if fase == 'Comeout':
            #Avisa ao jogador que ele está na fase Come out
            print('\nVocê está na fase COME OUT ')
            #Pergunta ao jogador qual tipo de aposta ele deseja realizar