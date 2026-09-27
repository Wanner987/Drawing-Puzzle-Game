import pygame

class Scene:
    def __init__(self, screen: pygame.Surface, name: str = "default"):
        self.SCREEN = screen
        self.NAME = name

    def enter(self):
        pass

    def update(self):
        raise NotImplementedError("Must have a process")

    def exit(self):
        pass
