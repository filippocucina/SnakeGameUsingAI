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
BLUE = (0,0,255)
SIZE_SNAKE = 30
#--------------------------------------------


class Entity(pygame.rect.Rect):
    def __init__(self, command, display, color, heigth, width, x, y):
        self.command = command
        self.heigth = int(heigth)
        self.width = int(width)
        self.display = display
        self.color = color
        self.x = int(x)
        self.y = int(y)
        

    def draw_rect(self):
        return self.command(self.display, self.color, self.heigth, self.width, self.x, self.y)
    
#snake = Entity(pygame.draw.rect(Window), Window, BLUE, 80, 40, 300, 300)


def initialized_window(): 
    global Window, info, Background, Font, Text, Text_position, snake

    try:
        pygame.init()
        print("Pygame has started. Enjoy this AI Model")
    except:
        pygame.set_error()
        pygame.error("Pygame does not work")
        

    Window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), 0, 16)
    pygame.display.set_caption("Snake")
    

    Background = pygame.Surface(Window.get_size())
    Background = Background.convert() #Operation to convert the Surface to a Single Pixel Format
    Background = Background.fill((250, 250, 250))
    
    
    #Displaying some text
    Font = pygame.font.Font(None, 36)
    Text = Font.render("AI plays Snake Game", 1, (230, 230, 230))
    
    snake = Entity(pygame.draw.rect, Window, BLUE, 80, 40, 700, 300)
    #snake = Entity(pygame.draw.rect(Window, BLUE, pygame.Rect(30,30,70,70)), Window, BLUE, 80, 40, 300, 300)

    return Window


def setup():
    global snake
    snake.draw_rect()
    
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
