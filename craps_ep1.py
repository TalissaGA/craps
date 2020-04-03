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
            if fase == 'Comeout':
            #Avisa ao jogador que ele está na fase Come out
            print('\nVocê está na fase COME OUT ')
            #Pergunta ao jogador qual tipo de aposta ele deseja realizar
            tipo = str(input('Qual tipo de aposta deseja realizar? (Pass Line Bet, Field, Any Craps, Twelve) '))
            #Tipo Pass Line Bet na fase Come out
            if tipo == 'Pass' or tipo=='pass' or tipo=='pass line bet':
                #Mostra ao jogador a quantia atual de dinheiro
                print('Seu dinheiro atual é: {}'.format(player_money))
                #Pergunta ao jogador quanto deseja apostar
                bet = int(input('Quanto deseja apostar? '))
                #Sorteio dos dados 
                d1 = random.randint(1,6)
                d2 = random.randint(1,6)
                soma = d1+d2
                #Mostra a soma dos dados
                print('A soma deu {}'.format(soma))
                #Relaciona a soma dos dados com as regras do tipo Pass Line Bet
                if soma == 7 or soma == 11:
                    print('Parabéns! Você Ganhou!\n')
                    #Caso ele ganhe, adiciona-se o valor da aposta à sua quantia atual de dinheiro
                    player_money += bet
                    #Retorna à fase Come Out, para outra rodada
                    fase = 'Comeout'
                    print('Seu dinheiro atual é: {}'.format(player_money))
                if soma == 2 or soma == 3 or soma == 12:
                    print('CRAPS! Você perdeu!')
                    #Caso ele Perca, subtrai-se o valor da aposta à sua quantia atual de dinheiro
                    player_money -= bet
                    #Retorna à fase Come Out, para outra rodada
                    fase = 'Comeout'
                if soma==4 or soma==5 or soma==6 or soma==8 or soma==9 or soma==10:
                    #Ativa o While do Point
                    Point = True
                    #O valor do point é o valor da soma sorteada no Come out
                    point = soma
                    #Avisa ao jogador que está indo para a fase Point
                    print('Próxima fase : POINT!') 
            
            #Pass Line Bet na fase Point
            while Point:
                #Sorteia os dados
                d1 = random.randint(1,6)
                d2 = random.randint(1,6)
                soma2 = d1+d2
                #Mostra a soma dos dados
                print('A soma dos dados é igual a {}'.format(soma2))
                #Compara a soma obtida às regras do Point 
                if soma2 == point:
                    print('Parabéns você ganhou')
                    player_money += bet 
                    fase = 'Comeout'
                    Point = False
                if soma2 == 7:
                    player_money = 0
                    fase = 'Comeout'
                    Point = False
                #else:
                    #print('Nova tentativa!')
