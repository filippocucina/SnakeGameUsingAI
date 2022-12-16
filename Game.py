import pygame


#--------------------------------------------
#Constantes
game_is_running = False
WINDOW_WIDTH = 1100
WINDOW_HEIGHT = 700
Window = None
Surface = None
#--------------------------------------------


def inicializa_ventana():    
    pygame.init()
    pygame.display.init()

    global Window

    Window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("Snake")
    pygame.display.update()
    return Window


def process_input():
    pass


def update():
    pass


def render():
    pygame.display.flip()
    

def destroy_window():
    pygame.quit()
    quit()
