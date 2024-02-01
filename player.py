import threading
import time
from behaviour import behaviour

class player:
    def __init__(self,name = "Ronaldo", number = "7", position = (3,2)):
        self.name = name
        self.number = number
        self.position = position
        self.behavior = behaviour()
        print(f"O jogador {self.name}-{self.number}, está na posição {self.position}")

    def run(self):
        print( f"Estou correndo, estou na posicao {self.position}")

    def kick(self, distance_to_ball):
        if distance_to_ball <= 0.6 and self.behavior.is_ball_owner:
            print("Chuto a bola")
        elif distance_to_ball <= 0.6:
            print("Não estou com a bola")
        elif self.behavior.is_ball_owner:
            print( f"Bola a uma distancia de {distance_to_ball}, não consigo alcançar")
        else:
            print( f"Não estou com a bola e bola a uma distancia de {distance_to_ball}")

    
    def receive_msg(self):
        while True:
            print (f"Jogador {self.name}-{self.number} esperando mensagem")
            time.sleep(1)




