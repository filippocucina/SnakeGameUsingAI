import pygame
from gameObjects import *
import game


class Entity(pygame.draw.rect):

    def __init__(self, positionX, positionY, width, height):
        self.positionX = int(positionX)
        self.positionY = int(positionY)
        self.width = int(width)
        self.height = int(height)
        

class Snake(Entity, pygame.draw.rect()):

    def __init__(self, color_red, color_green, color_blue):
        Entity.__init__(self, self.positionX, self.positionY, self.width, self.height)
        self.color_red = int(color_red)
        self.color_green = int(color_green)
        self.color_blue = int(color_blue)
    
    
    def render_snake(self):
        return pygame.draw.rect(Window, (self.color_red, self.color_green, self.color_blue), self.positionX, self.positionY, self.width, self.height)
    
    
    def expand_snake(self):
        pass

    
    def destroy_snake(self):
        pass


class Apple(Entity, pygame.draw.rect):

    def __init__(self, color_red, color_green, color_blue):
        Entity.__init__(self, self.positionX, self.positionY, self.width, self.height)
        self.color_red = int(color_red)
        self.color_green = int(color_green)
        self.color_blue = int(color_blue)
        pass


    def render_apple(self):
        pygame.draw.rect(Window, (self.color_red, self.color_green, self.color_blue), self.positionX, self.positionY, self.width, self.height)
        pass


    def random_position(self):
        pass


    def destroy_apple(self):
        pass


snake = Snake(500, 500, 50, 50, 255, 255, 255)
apple = Apple(800, 700, 25, 25, 255, 0, 0)


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


def main():
    global game_is_running


    game_is_running = game.initialized_window()


    game.setup()


    while game_is_running:
        game.process_input()
        game.update()
        game.render()
           

    game.destroy_window()


if __name__ == "__main__":
    main()
