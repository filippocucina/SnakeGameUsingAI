import pygame 
from game import *
global game


class game_objects(pygame.draw.rect):
    def __init__(self, positionX, positionY, width, height, color, velocityX, velocityY):
        self.rect = pygame.draw.rect()
        self.positionX = positionX
        self.positionY = positionY
        self.width = width
        self.height = height
        self.color = color
        self.velocityX = velocityX
        self.velocityY = velocityY


    def draw_object(self):
        self.rect = pygame.draw.rect(game.Surface, (255,255,255))

     
    def increment_object(self):
        pass


    def random_position(self):
        pass


    def destroy_object(self):
        pass


#snakeAI = game_objects(400, 300, 40, 20, 10, 10)
#apple = game_objects(800, 600, 20, 20, 0, 0)