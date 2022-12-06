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

    Window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.update()
    return Window


def process_input():
    print("Se procesa Input del Usuario")


def update():
    print("Aqui se actualiza las Imagenes")


def render():
    print("Aqui va el Rendering")


def main():
    global game_is_running
    game_is_running = inicializa_ventana()


    while game_is_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT():
                game_is_running = False
            
    pygame.quit()
    quit()


if __name__ == "__main__":
    main()
