import pygame

game_is_running = False


class Game:

    def __init__(self, width, heigth):
        self.width = width
        self.heigth = heigth
        self.window = pygame.display.set_mode(self.width, self.heigth, 0, 0, 0)

    def initialized_window(self):
        try:
            pygame.init()
            print("Pygame has started. Enjoy this AI Model")
        except:
            pygame.error("The Initialized_window does not work!")

        pygame.display.set_caption("Snake Game")


    def setup():

        pass

    def process_input():
        #inherited class will execute the code of this function
        pass

    def update():
        #inherited class will execute the code of this function
        pass

    def render():
        pygame.display.flip()
        pass

    def destroy_window():
        pygame.display.quit()
        pygame.quit()
        quit()


class Snake(Game):

    def __init__(self, x, y, height, width, color):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color

    def setup_snake(self):
        super().setup()
        pass

    def render_snake(self):
        pygame.draw.rect(Game.window, self.color, self.rect)
        super().render()
        

    def expand_snake(self):
        pass

    pass

class Apple(Game):

    def __init__(self, x, y, height, width, color):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color

    def setup_apple():
        super().setup()
        pass

    def render_apple(self):
        pygame.draw.rect(Game.window, self.color, self.rect)
        super().render()
        

    def change_position():
        pass

    pass

game = Game(800, 600)
snake = Snake(500, 500, 50, 50, (0, 0, 255))
apple = Apple(1000, 1000, 20, 30, (100, 50, 200))

def main():

    game_is_running = game.initialized_window()

    game.setup()

    while game_is_running:
        game.process_input()
        game.update()
        game.render()


    game.destroy_window()

if __name__ == "__main__":
    main()
     