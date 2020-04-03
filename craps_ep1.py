##Jogo Craps 
#Eduardo Papandrea
#Talissa Albertini

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
                    #Caso o jogador ganhe, ele ganha o valor apostado
                    player_money += bet 
                    #Ao ganhar ou perder, ele finaliza a rodada
                    Point = False
                    #Retorna à fase Comeout para nova rodada
                    fase = 'Comeout'
                if soma2 == 7:
                    #Ao perder, ele perde todo o dinheiro
                    player_money = 0
                    #Ao ganhar ou perder, ele finaliza a rodada
                    Point = False
                    #Retorna à fase Comeout para nova rodada
                    fase = 'Comeout'
            
            #Caso ele não tenha escolhido o tipo Pass
            #Tipo Field
            if tipo == 'Field' or tipo=='field':
                #Mostra ao jogador a quantidade atual de dinheiro
                print('Seu dinheiro atual é: {}'.format(player_money))
                bet2 = int(input('Quanto deseja apostar? '))
                #Sorteia os dados
                d1 = random.randint(1,6)
                d2 = random.randint(1,6)
                soma3 = d1+d2
                #Mostra a soma dos dados
                print('A soma dos dados é igual a {}'.format(soma3))
                #Compara a soma obtida com as regras do Field
                if soma3 == 5 or soma3 == 6 or soma3 == 7 or soma3 == 8:
                    #Caso o jogador perca, ele perde tudo
                    player_money = 0 
                    print('Você perdeu!')
                    #Retorna à fase Come out
                    fase = 'Comeout'
                elif soma3 == 3 or soma3 == 4 or soma3 == 9 or soma3 == 10 or soma3 == 11:
                    #Jogador ganha o que apostou
                    player_money += bet2
                    print('Parabéns')
                    #Retorna à fase Come Out, para outra rodada
                    fase = 'Comeout'
                    #Mostra ao jogador sua quantidade atual de dinheiro
                    print('Agora seu dinheiro atual é: {}'.format(player_money))
                elif soma3 == 2:
                    #Jogador ganha o dobro do que apostou
                    player_money += bet2*2
                    #Retorna à fase Come Out, para outra rodada 
                    fase = 'Comeout'
                    print('Parabéns')
                    print('Agora seu dinheiro atual é: {}'.format(player_money))
                elif soma3 == 12:
                    #Jogador ganha o dobro do que apostou
                    player_money += bet2*3
                    #Retorna à fase Come Out, para outra rodada
                    fase = 'Comeout'
                    print('Parabéns')
                    print('Seu dinheiro atual é: {}'.format(player_money))
                    
            #Tipo Any Craps
            if tipo ==  'Any Craps'  or tipo == 'any' or tipo == 'any craps': 
                print('Seu dinheiro atual é: {}'.format(player_money))
                # Pergunta quanto ele quer apostar
                bet3 = int(input('Quanto deseja apostar? '))
                #Sorteia os dados
                d1 = random.randint(1,6)
                d2 = random.randint(1,6)
                soma4 = d1+d2
                #Mostra a soma dos dados
                print('A soma dos dados é igual a {}'.format(soma4))
                #Compara a soma às regras de Any Craps
                if soma4 == 2 or soma4 == 3 or soma4 == 12:
                    #Caso ele ganhe, ele ganha 7x o que apostou
                    player_money += bet3*7
                    print('Parabéns')
                    #Retorna à fase Come Out, para outra rodada
                    fase = 'Comeout'
                    print('Seu dinheiro atual é: {}'.format(player_money))
                else:
                    #Caso ele perca. ele perde o valor que apostou
                    player_money -= bet3
                    print('Você perdeu a aposta!')
                    #Retorna à fase Come Out, para outra rodada
                    fase = 'Comeout'
                    print('Seu dinheiro atual é: {}'.format(player_money))

            #Tipo Twelve
            if tipo == 'Twelve' or tipo == 'twelve':
                #Mostra ao jogador a quantidade atual de dinheiro
                print('Seu dinheiro atual é: {}'.format(player_money))
                bet4 = int(input('Quanto deseja apostar? '))
                #Sorteia os dados
                d1 = random.randint(1,6)
                d2 = random.randint(1,6)
                soma5 = d1+d2
                #Mostra a soma dos dados
                print('A soma dos dados é igual a {}'.format(soma5))
                #Compara a soma dos dados às regras da Twelve
                if soma5 == 12:
                    #Caso ele ganhe, ele ganha 30x o que apostou
                    player_money += bet5*30
                    print('Parabéns')
                    #Retorna à fase Come Out, para outra rodada
                    fase = 'Comeout'
                    print('Seu dinheiro atual é: {}'.format(player_money))
                else:
                    player_money = 0
                    print('Você perdeu a aposta!')
                    #Retorna à fase Come Out, para outra rodada
                    fase = 'Comeout'

    #Caso o jogador não queira jogar 
    else: 
        break

#Mensagem final ao jogador, mostrando seu saldo final.
if player_money > 0:
    print('Seu saldo final é de: {} '.format(player_money))
else:
    print('Hoje não é seu dia de sorte, seu saldo final é 0!')

