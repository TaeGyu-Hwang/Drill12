from pico2d import load_image, delay, clear_canvas, update_canvas, get_events, get_time, pico2d
from sdl2 import SDL_QUIT, SDL_KEYDOWN, SDLK_ESCAPE, SDLK_SPACE


import game_framework
import play_mode
import game_world
import pannel
from pannel import Pannel

def init():
    global image
    pannel = Pannel()
    game_world.add_object(pannel, 3)

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.pop_mode(play_mode)
        elif event.type == SDL_KEYDOWN:
            match event.key:
                case pico2d.SDLK_1:
                    play_mode.boy.item = 'Ball'
                    game_framework.pop_mode()
                case pico2d.SDLK_2:
                    play_mode.boy.item = 'BigBall'
                    game_framework.pop_mode()
                case pico2d.SDLK_0:
                    play_mode.boy.item = None
                    game_framework.pop_mode()


def update():
    game_world.update()

def draw():
    clear_canvas()
    game_world.render()
    update_canvas()

def finish():
    game_world.remove_object(pannel)
    pass

def pause():
    pass
def resume():
    pass