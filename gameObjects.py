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

    def __init__(self):
        
        Entity.__init__(self, self.positionX, self.positionT, self.width, self.height)
        pass
    
    
    def draw_snake(self):
        pass
    
    
    def expand_snake(self):
        pass

    
    def destroy_snake(self):
        pass


class Apple(Entity):

    def __init__(self):
        pass


    def draw_apple(self):
        pass


    def destroy_apple(self):
        pass
