import pygame
from app.Elements.Scenes.StartingScreen import StartingScreen
from app.Elements.SceneManager import SceneManager

SCREEN_SIZE = (850, 500)
FPS = 30
WINDOW_NAME = "Drawing Puzzle Game"
START_SCREEN = "StartingScreen"

pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption(WINDOW_NAME)
clock = pygame.time.Clock()
sceneManager = SceneManager(START_SCREEN, screen)

running = True
while running:
    # check for quit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # update the current scene
    sceneManager.update()

    # update display and clock(delta)
    pygame.display.flip()
    clock.tick(FPS)