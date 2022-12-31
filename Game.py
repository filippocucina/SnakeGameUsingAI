import pygame
from game.gameObjects import *


#--------------------------------------------
#Constants
game_is_running = False
WINDOW_WIDTH = 1100
WINDOW_HEIGHT = 700
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
    Text = Font.render("Hello Pygame!", 1, (230, 230, 230))
    #Text_position = Text.get_rect()
    #Text_position.centerx = Background.get_rect().centerx
    

    return Window


def setup():
    gameObjects.snake.render_snake()
    apple.render_apple()


def process_input():
    pass


def update():
    pygame.display.update()


def render():
    Window.blit(Text, (0,0))
    #Background.blit(Text, Text_position)
    pygame.display.flip()
    

def destroy_window():
    pygame.quit()
    quit()
