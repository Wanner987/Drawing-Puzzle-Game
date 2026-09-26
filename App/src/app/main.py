import pkgutil
import importlib
import inspect
import pygame
from .Elements import Button
from app.Elements.Scenes import Scene


SCREEN_SIZE = (850, 500)
FPS = 30
WINDOW_NAME = "Drawing Puzzle Game"
START_SCENE = Scene()
CURRENT_SCENE = Scene()


pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption(WINDOW_NAME)
clock = pygame.time.Clock()
button = Button(100, 100, 50, 50, "red", screen)

def run():
    _ready()
    _process()

def _ready():
    screen.fill("blue")
    button.display()

def _process():
    running = True
    while running:
        # check for quit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        button.on_hover_color()

        # update display and clock(delta)
        pygame.display.flip()
        clock.tick(FPS)

run()