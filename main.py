from gameObjects import *
import game


def main():
    global game_is_running


    game_is_running = game.inicializa_ventana()


    game.setup()


    while game_is_running:
        game.process_input()
        game.update()
        game.render()
           

    game.destroy_window()


if __name__ == "__main__":
    main()
