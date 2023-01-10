from cgi import print_form
import pygame


#--------------------------------------------
#Constants
game_is_running = False
WINDOW_WIDTH = 1152
WINDOW_HEIGHT = 864
Window = None
Surface = None
Background = None
Font = None
Text = None
Text_position = None
last_frame_time = 0
FPS = 60
FRAME_TARGET_TIME = (1000/FPS)  
#--------------------------------------------


def initialized_window():    
    pygame.init()
    #More code need to be added!

    global Window, info, Background, Font, Text, Text_position, backend_display, windowing_system, desktop_sizes, get_surface_game
    global list_modes_game, depth_window, modes

    
    Window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), 0, 16)
    pygame.display.set_caption("Snake")
    info = pygame.display.Info()    
    backend_display = pygame.display.get_driver()
    windowing_system = pygame.display.get_wm_info()
    desktop_sizes = pygame.display.get_desktop_sizes()
    get_surface_game = pygame.display.get_surface()
    list_modes_game = pygame.display.list_modes()
    depth_window = pygame.display.mode_ok((128,128), 0, 32)
    modes = pygame.display.list_modes()


    print(info)
    print(backend_display)
    print(windowing_system)
    print(desktop_sizes)
    print(get_surface_game)
    print(list_modes_game)
    print(depth_window)
    print(modes)


    Background = pygame.Surface(Window.get_size())
    Background = Background.convert() #Operation to convert the Surface to a Single Pixel Format
    Background = Background.fill((250, 250, 250))
    
    
    #Displaying some text
    Font = pygame.font.Font(None, 36)
    Text = Font.render("Hello Pygame!", 1, (230, 230, 230))
    #Text_position = Text.get_rect()
    #Text_position.centerx = Background.get_rect().centerx
    

    return Window


def setup():
    global snake, apple
    #snake = pygame.draw.rect()
    

    snake = pygame.draw.rect(Window, (255,0,0), pygame.Rect(300, 300, 90, 20))
    apple = pygame.draw.rect(Window, (148, 0, 211), pygame.Rect(700, 300, 20, 20))
    pass


def process_input():
    pass


def update():
    #pygame.display.update()
    pass


def render():
    Window.blit(Text, (0,0))
    #Background.blit(Text, Text_position)
    pygame.display.flip()
    

def destroy_window():
    pygame.quit()
    quit()


def main():
    global game_is_running


    game_is_running = initialized_window()


    setup()


    while game_is_running:
        process_input()
        update()
        render()
           

    destroy_window()


if __name__ == "__main__":
    main()
