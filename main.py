#Projetar uma classe player que inicialize variáveis (nome, número, time e posição) e que possua duas 
#funções (kick() e run()). Dentro da classe player deve-se inicializar a classe behavior com variáveis 
#(mood, mode e ball_owner), a variável ball_owner deve ser capaz de influenciar na decisão da função 
#kick() do player. Ainda, deve-se projetar uma função ‘receive_msg’ com ‘while True’ que simule a
#espera de uma mensagem por meio de uma threading

#classe player - variavies nome, numero, posicao-funcao kick() - distancia da bola e se o jogador ta
#com a bola - e run()
#classe behaviour- mood e mode - funcao ball_owner() ve se jogador tem a bola
#threading

import player
import behaviour
import threading
import time

def main():
    jogador1 = player.player()
    jogador1.kick(distance_to_ball= 0.8)
    jogador2 = player.player(name = "Hugo", number = 2, position=(4,5))

    TH = threading.Thread(target = jogador1.receive_msg)
    TH.start()
    TH = threading.Thread(target = jogador2.receive_msg)
    TH.start()
    jogador2.kick(distance_to_ball = 0.2)

if __name__ == main():
    main()