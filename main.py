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
            pygame.error("Pygame does not work!")

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

class Entity(Game):
    def __init__(self, entity_width, entity_heigth, entity_x, entity_y, velocity_x, velocity_y):
        self.entity_width = int(entity_width)
        self.entity_heigth = int(entity_heigth)
        self.entity_x = int(entity_x)
        self.entity_y = int(entity_y)

    def render():

        pass

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