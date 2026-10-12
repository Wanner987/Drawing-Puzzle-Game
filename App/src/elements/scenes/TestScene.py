import pygame
from .scene import Scene
from ..drawing import Drawing
from ..eventManager import EventManager

class TestScene(Scene):
    def __init__(self, screen: pygame.Surface, name: str = "TestScene"):
        super().__init__(screen, name)

    def enter(self):
        self.SCREEN.fill("white")
        self.drawing = Drawing(self.SCREEN, 10)
        EventManager.onShapeRecognized.append(self.changeBackground)

    
    def update(self):
        for event in pygame.event.get():
            self.drawing.drawUpdate(event)

    def exit(self):
        pass

    def changeBackground(self, shape : str):
        colors = {
        "line-up": (173, 216, 230),     # Light blue
        "line-down": (0, 0, 139),       # Dark blue
        "line-left": (139, 0, 0),       # Dark red
        "line-right": (255, 182, 193),  # Light red
        "u-up": (144, 238, 144),        # Light green
        "u-down": (0, 100, 0),          # Dark green
        "u-left": (128, 128, 128),
        "u-right": (255, 255, 255),
    }

        color = colors.get(shape.lower())

        if color is not None:
            self.SCREEN.fill(color)
