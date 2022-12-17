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
   

    global Window, info
    Window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), 0, 16)
    pygame.display.set_caption("Snake")
    info = pygame.display.Info()    
    print(info)

    return Window


def process_input():
    pass


def update():
    pygame.display.update()


def render():
    pygame.display.flip()
    

def destroy_window():
    pygame.quit()
    quit()
