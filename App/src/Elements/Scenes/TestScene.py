import pygame
from .Scene import Scene
from ..Drawing import Drawing

class TestScene(Scene):
    def __init__(self, screen: pygame.Surface, name: str = "TestScene"):
        super().__init__(screen, name)

    def enter(self):
        self.SCREEN.fill("white")
        self.drawing = Drawing(self.SCREEN, 10)
    
    def update(self):
        if pygame.mouse.get_pressed()[0]:
            self.drawing.draw()

    def exit(self):
        pass
