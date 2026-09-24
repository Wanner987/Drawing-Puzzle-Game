import pygame
from app.Button import Button

pygame.init()
screen = pygame.display.set_mode((850, 500))
pygame.display.set_caption("Drawing Puzzle Game")
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
        clock.tick(30)

run()