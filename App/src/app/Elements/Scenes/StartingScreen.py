import pygame
from .Scene import Scene
from app.Elements.Button import Button

class StartingScreen(Scene):
    def __init__(self, screen: pygame.Surface):
        super().__init__(screen, "StartingScreen")

    def enter(self):
        screen = self.SCREEN
        self.button = Button(100, 100, 50, 50, "red", screen)
        
        screen.fill("blue")
        self.button.display()

    def update(self):
        self.button.on_hover_color()

    def exit(self):
        pass
