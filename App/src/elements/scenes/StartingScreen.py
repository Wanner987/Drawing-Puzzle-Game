import pygame
from .scene import Scene
from elements.button import ImageButton
from ..eventManager import EventManager

class StartingScreen(Scene):
    def __init__(self, screen: pygame.Surface, name: str = "StartingScreen"):
        super().__init__(screen, name)

    def enter(self):
        screen = self.SCREEN
        self.button = ImageButton(100, 100, pygame.image.load('src/assets/StartButtonPlaceholder.png'), self.SCREEN, 8)
        
        screen.fill("blue")
        self.button.display()

    def update(self):
        if self.button.is_clicked():
            EventManager.changeScene(self, "testScene")

    def exit(self):
        pass
