import pygame
from .Scene import Scene
from app.Elements.Button import Button

class StartingScreen(Scene):
    def __init__(self, screen: pygame.Surface, name: str = "StartingScreen"):
        super().__init__(screen, name)

    def enter(self):
        screen = self.SCREEN
        self.button = Button(100, 100, 50, 50, "red", screen)
        
        screen.fill("blue")
        self.button.display()

    def update(self):
        if self.button.is_clicked():
            print("Clicked")
            self.EVENTS.append(("change_scene", self, "TestScene"))

    def exit(self):
        pass
