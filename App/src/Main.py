import pygame
from elements.sceneManager import SceneManager
from elements.config import Config

SCREEN_SIZE = Config.SCREEN_SIZE
FPS = Config.FPS
WINDOW_NAME = "Drawing Puzzle Game"
# START_SCREEN = "startingScreen"
START_SCREEN = "testPuzzle"

pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption(WINDOW_NAME)
clock = pygame.time.Clock()
sceneManager = SceneManager(START_SCREEN, screen)
deltaTime = 0.0

running = True
while running:
    # check for quit
    if pygame.event.peek(pygame.QUIT):
        running = False

    # update the current scene
    sceneManager.update(deltaTime)

    # update display and clock(delta)
    pygame.display.flip()
    deltaTime = clock.tick(FPS) / 1000.0