import pygame
from elements.scenes.startingScreen import StartingScreen
from elements.sceneManager import SceneManager

SCREEN_SIZE = (850, 500)
FPS = 60
WINDOW_NAME = "Drawing Puzzle Game"
START_SCREEN = "startingScreen"

pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption(WINDOW_NAME)
clock = pygame.time.Clock()
sceneManager = SceneManager(START_SCREEN, screen)

running = True
while running:
    # check for quit
    if pygame.event.peek(pygame.QUIT):
        running = False

    # update the current scene
    sceneManager.update()

    # update display and clock(delta)
    pygame.display.flip()
    clock.tick(FPS)