import pygame


#--------------------------------------------
#Constants
game_is_running = False
WINDOW_WIDTH = 1152
WINDOW_HEIGHT = 864
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


class Entity(pygame.rect.Rect):
    def __init__(self, color, size, x, y):
        self.rect = pygame.rect.Rect(Window, color, size, x, y)
        self.color = color
        self.size = size
        self.x = x
        self.y = y

    def draw(self):
        return self.rect
        
snake = Entity((200, 0, 0), 30, 30, 30)

class Snake(Entity):
    def __init__(self):
        super().__init__()
        pass

    def draw():
        pass

#snake = Snake(())


class Apple(Entity):
    def __init__():
        pass

    def draw():
        pass


def initialized_window(): 
    global Window, info, Background, Font, Text, Text_position

    try:
        pygame.init()
        print("Pygame has started. Enjoy this AI Model")
    except:
        print("Pygame does not work")

    
    Window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), 0, 16)
    pygame.display.set_caption("Snake")
    

    Background = pygame.Surface(Window.get_size())
    Background = Background.convert() #Operation to convert the Surface to a Single Pixel Format
    Background = Background.fill((250, 250, 250))
    
    
    #Displaying some text
    Font = pygame.font.Font(None, 36)
    Text = Font.render("AI plays Snake Game", 1, (230, 230, 230))
    

    return Window


def setup():
    
    

    
    pass


def process_input():
    global user_event, game_is_running
        


    pass


def update():
    

    
    pass


def render():
    Window.blit(Text, (0,0))
    #Background.blit(Text, Text_position)
    pygame.display.flip()
    

def destroy_window():
    pygame.quit()
    quit()


def main():
    global game_is_running


    game_is_running = initialized_window()


    setup()


    while game_is_running:
        process_input()
        update()
        render()
           

    destroy_window()


if __name__ == "__main__":
    main()
