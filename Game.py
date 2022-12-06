import pygame 
from Images import *


#Constantes
game_is_running = False
WIDTH = 1100
HEIGHT = 700
Window = None
Surface = None
CULEBRITA = pygame.image_load("Snake.png")
CULEBRITA_RECT = CULEBRITA.get_rect()

def inicializa_ventana():    
    pygame.init()

    Window = pygame.display.set_mode((WIDTH, HEIGHT))
    Window = pygame.display.update()
    return Window

  
def main():
    inicializa_ventana()


if __name__ == "__main__":
    main()