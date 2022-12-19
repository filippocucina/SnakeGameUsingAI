import pygame


#--------------------------------------------
#Constantes
game_is_running = False
WINDOW_WIDTH = 1100
WINDOW_HEIGHT = 700
Window = None
Surface = None
Background = None
Font = None
Text = None
Text_position = None
#--------------------------------------------


def inicializa_ventana():    
    pygame.init()
    

    global Window, info, Background, Font, Text, Text_position

    
    Window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), 0, 16)
    pygame.display.set_caption("Snake")
    info = pygame.display.Info()    
    print(info)
    

    Background = pygame.Surface(Window.get_size())
    Background = Background.convert() #Operation to convert the Surface to a Single Pixel Format
    Background = Background.fill((250, 250, 250))
    
    
    #Displaying some text
    Font = pygame.font.Font(None, 36)
    Text = Font.render("Hello Pygame!", 1, (10, 10, 10))
    Text_position = Text.get_rect()
    Text_position.centerx = Background.get_rect().centerx
    Background.blit(Text, Text_position)
    

    Window.blit(Background, (0,0))


    return Window


def process_input():
    pass


def update():
    pygame.display.update()


def render():
    global Window, info, Background, Font, Text, Text_position


    pygame.display.flip()
    

def destroy_window():
    pygame.quit()
    quit()
