import pygame
window_game = None
game_is_running = False
background_game = None

 
class Game():
    def __init__(self, window, window_heigth, window_width, background, last_frame_time):
        self.window = window
        self.window_heigth = int(window_heigth)
        self.window_width = int(window_width)
        self.background = background
        self.last_frame_time = int(last_frame_time)

    def initialized_window(self):
       try:
            pygame.init()
            print("Pygame has started. Enjoy this AI Model")
       except:
            pygame.error("The Initialized_window does not work!")

       self.window = pygame.display.set_mode((self.window_width, self.window_heigth), 0, 0, 0, 0,)
       pygame.display.set_caption("Snake Game")



       return self.window


    def setup(self):
        pass
   

    def process_input(self):
        pass


    def update(self):
        pass


    def render(self):
        pygame.display.flip()
        pass


    def destroy_window(self):
        pygame.display.quit()
        pygame.quit()
        quit()

        
    pass

class Snake():
    def __init__(self, x, y, height, width):
        self.x = x
        self.y = y
        self.height = height
        self.width = width

    def draw():
        pygame.draw.rect(Game.window, (0, 0, 5), (Snake.x, Snake.y, Snake.width, Snake.heigth), (0))



game = Game(window_game, 1020, 1920, background_game, 0)

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
     