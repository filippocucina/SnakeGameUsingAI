import pygame
import gameObjects


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
    print("Se procesa Input del Usuario")


def update():
    print("Aqui se actualiza las Imagenes")


def render():
    print("Aqui va el Rendering")

    pygame.display.flip()
    

def destroy_window():
    pygame.quit()
    quit()


def main():
    global game_is_running

    game_is_running = inicializa_ventana()


    while game_is_running:
        process_input()
        update()
        render()
           

    destroy_window()


if __name__ == "__main__":
    main()
