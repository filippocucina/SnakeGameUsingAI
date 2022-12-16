import pygame


class gameObject(pygame.sprite.Sprite):

    def __init__(self, positionX, positionY, width, height, velocityX, velocityY):
        #self.image = image
        self.positionX = positionX
        self.positionY = positionY
        self.width = width
        self.height = height
        self.velocityX = velocityX
        self.velocityY = velocityY


snakeAI = gameObject(400, 300, 40, 20, 10, 10)
apple = gameObject(800, 600, 20, 20, 0, 0)