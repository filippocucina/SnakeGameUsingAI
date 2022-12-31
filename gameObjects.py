import pygame 
from game import Window
global game


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
