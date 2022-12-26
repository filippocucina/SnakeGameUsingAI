import pygame 
from game import *
global game


class Entity(pygame.draw.rect):

    def __init__(self, positionX, positionY, width, height):
        self.positionX = positionX
        self.positionY = positionY
        self.width = int(width)
        self.height = int(height)
        

class Snake(Entity):

    def __init__(self, color_red, color_green, color_blue):
        Entity.__init__(self, self.positionX, self.positionY, self.width, self.height)
        self.color_red = int(color_red)
        self.color_green = int(color_green)
        self.color_blue = int(color_blue)
    
    
    def render_snake(self):
        pygame.draw.rect(Window, (self.color_red, self.color_green, self.color_blue), self.positionX, self.positionY, self.width, self.height)
        pass
    
    
    def expand_snake(self):
        pass

    
    def destroy_snake(self):
        self.kill()
        pass


class Apple(Entity):

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
